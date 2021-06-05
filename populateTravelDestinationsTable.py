import os
import boto3
from dynamoDbResource import create_dynamodb_resource_instance

dynamodb = create_dynamodb_resource_instance()

try:
    response=dynamodb.batch_write_item(
        RequestItems={
            'TravelDestinations':[
                {
                    'PutRequest':{
                        'Item':{
                            'DestinationID':'BigBendNP43290342',
                            'OptimalQuarter':'Q1',
                            'Priority': 2,
                            'DestinationName':'Big Bend National Park'
                        }
                    }
                },
                {
                    'PutRequest':{
                        'Item':{
                            'DestinationID':'SaguaroNP9059834',
                            'OptimalQuarter':'Q1',
                            'Priority': 4,
                            'DestinationName':'Saguaro National Park'
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