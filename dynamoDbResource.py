import boto3


# On local dev, storing access key in environment variables in run configuration
def create_dynamodb_resource_instance():
    dynamodb = boto3.resource('dynamodb',
                              region_name="us-east-1")
    return dynamodb
