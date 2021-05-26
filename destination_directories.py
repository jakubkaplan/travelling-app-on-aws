import os

import boto3
from werkzeug.exceptions import abort

ACCESS_KEY = "ACCESS_KEY"
SECRET_KEY = "SECRET_KEY"
REGION_NAME = "us-east-1"


class DynamoDestinationDirectory:
    def __init__(self):
        dynamodb = boto3.resource('dynamodb', aws_access_key_id=(os.getenv(ACCESS_KEY)),
                                  aws_secret_access_key=(os.getenv(SECRET_KEY)),
                                  region_name=REGION_NAME)
        self.travel_destinations_table = dynamodb.Table('TravelDestinations')

    @staticmethod
    def convert_ddb_item_to_destination(item):
        return Destination(destination_id=item["DestinationID"],
                           optimal_quarter=item["OptimalQuarter"],
                           priority=item["Priority"],
                           name=item["DestinationName"])

    def get_all_destinations(self):
        _all_travel_destinations = [DynamoDestinationDirectory.convert_ddb_item_to_destination(item) for item in
                                    self.travel_destinations_table.scan()['Items']]
        return _all_travel_destinations

    def get_destination(self, destination_id):
        response = self.travel_destinations_table.get_item(
            Key={
                'DestinationID': destination_id
            }
        )
        if "Item" not in response:
            abort(404)
        return DynamoDestinationDirectory.convert_ddb_item_to_destination(response["Item"])


class Destination:
    def __init__(self, destination_id, optimal_quarter, priority, name):
        self.destination_id = destination_id
        self.optimal_quarter = optimal_quarter
        self.priority = priority
        self.name = name
