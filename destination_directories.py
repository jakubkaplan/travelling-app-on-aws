import boto3
import random
from werkzeug.exceptions import abort

from credentials import AWS_SECRET_ACCESS_KEY, AWS_ACCESS_KEY_ID

DESTINATION_NAME = "DestinationName"
PRIORITY = "Priority"
OPTIMAL_QUARTER = "OptimalQuarter"
DESTINATION_ID = "DestinationID"

REGION_NAME = "us-east-1"


class Destination:
    def __init__(self, destination_id, optimal_quarter, priority: int, name):
        self.destination_id = destination_id
        self.optimal_quarter = optimal_quarter
        self.priority = priority
        self.name = name


class DynamoDestinationDirectory:
    def __init__(self):
        dynamodb = boto3.resource('dynamodb', aws_access_key_id=AWS_ACCESS_KEY_ID,
                                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                                  region_name=REGION_NAME)
        self.travel_destinations_table = dynamodb.Table('TravelDestinations')

    @staticmethod
    def convert_ddb_item_to_destination(item):
        return Destination(destination_id=item[DESTINATION_ID],
                           optimal_quarter=item[OPTIMAL_QUARTER],
                           priority=item[PRIORITY],
                           name=item[DESTINATION_NAME])

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

    def add_new_destination(self, optimal_quarter, priority, name):
        destination_id = DynamoDestinationDirectory.createNewDestinationId(destination_name=name)
        destination = Destination(destination_id=destination_id, optimal_quarter=optimal_quarter, priority=priority,
                                  name=name)
        self.travel_destinations_table.put_item(Item=DynamoDestinationDirectory.
                                                convertToDynamoItem(destination=destination))

    # Returns number of items deleted
    def delete_destination(self, destination_id):
        deleted_item = self.travel_destinations_table.delete_item(Key={DESTINATION_ID: destination_id},
                                                                  ReturnValues='ALL_OLD')
        if "Attributes" in deleted_item:
            return 1
        else:
            return 0

    @staticmethod
    def createNewDestinationId(destination_name):
        return destination_name + str(random.randint(0, 100000))

    @staticmethod
    def convertToDynamoItem(destination):
        dynamo_item = {DESTINATION_ID: destination.destination_id, OPTIMAL_QUARTER: destination.optimal_quarter,
                       PRIORITY: destination.priority, DESTINATION_NAME: destination.name}
        return dynamo_item
