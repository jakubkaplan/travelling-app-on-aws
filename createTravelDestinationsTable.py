import os

import boto3

# Need to copy credentials from environment variables
# Cannot store in local AWS config because I have that on WSL Ubuntu, while IntelliJ is running from Windows
ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
dynamodb = boto3.resource('dynamodb', aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY,
                          region_name="us-east-1")

try:
    dynamodb.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'DestinationID',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'OptimalQuarter',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'Priority',
                'AttributeType': 'N'
            },
        ],
        TableName='TravelDestinations',
        KeySchema=[
            {
                'AttributeName': 'DestinationID',
                'KeyType': 'HASH'
            }
        ],
        GlobalSecondaryIndexes=[
            {
                'IndexName': 'OptimalQuarterGSI',
                'KeySchema': [
                    {
                        'AttributeName': 'OptimalQuarter',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName':'Priority',
                        'KeyType': 'RANGE'
                    }
                ],
                'Projection':{
                    'ProjectionType':'ALL'
                },
                'ProvisionedThroughput':{
                    'ReadCapacityUnits':1,
                    'WriteCapacityUnits':1
                }
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits':1,
            'WriteCapacityUnits':1
        }
    )

    print("Table created successfully")
except Exception as e:
    print("Error creating table:")
    print(e)


