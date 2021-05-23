from flask import Flask, render_template
from werkzeug.exceptions import abort
import os
import boto3

ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
dynamodb = boto3.resource('dynamodb', aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY,
                          region_name="us-east-1")
travel_destinations_table = dynamodb.Table('TravelDestinations')


def get_all_destinations():
    all_travel_destinations = travel_destinations_table.scan()['Items']
    return all_travel_destinations


def get_destination(destination_id):
    response = travel_destinations_table.get_item(
        Key={
            'DestinationID': destination_id
        }
    )
    if "Item" not in response:
        abort(404)
    return response["Item"]


all_travel_destinations = get_all_destinations()
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', travelDestinations=all_travel_destinations)


@app.route("/destination/<destination_id>")
def destination(destination_id):
    return render_template('destination.html', destination=get_destination(destination_id))
