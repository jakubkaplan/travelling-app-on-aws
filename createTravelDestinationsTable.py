import boto3
from dynamoDbResource import create_dynamodb_resource_instance

dynamodb = create_dynamodb_resource_instance()


# Travel Destinations DB design
#
# Use cases:
# P0:
# -I view all travel destinations
# -I view all travel destinations for which optimal quarter is Q1/Q2/Q3/Q4, ordered by priority ascending
#
# P1:
# -I view top priority destinations for which optimal quarter is TK
#
# I can save a travel destination with ID, name, priority, quarter, country, state, description
#
# Primary key
# HASH Key: DestinationID
# Sort Key: None
#
# Optimal Quarter GSI
# HASH Key: optimal_quarter
# Sort key: priority
#


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


