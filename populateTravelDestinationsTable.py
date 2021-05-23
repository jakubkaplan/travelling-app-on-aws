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
    response=dynamodb.batch_write_item(
        RequestItems={
            'TravelDestinations':[
                {
                    'PutRequest':{
                        'Item':{
                            'DestinationID':'BigBendNP43290342',
                            'OptimalQuarter':'Q1',
                            'Priority': 2
                        }
                    }
                },
                {
                    'PutRequest':{
                        'Item':{
                            'DestinationID':'SaguaroNP9059834',
                            'OptimalQuarter':'Q1',
                            'Priority': 4
                        }
                    }
                }
            ]
        }
    )

    print('Items added')
    print(response)
except e as Exception:
    print(e)