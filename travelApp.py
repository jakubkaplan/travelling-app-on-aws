from flask import Flask, render_template
import os
import boto3

def getAllTravelDestinations():
    ACCESS_KEY = os.getenv("ACCESS_KEY")
    SECRET_KEY = os.getenv("SECRET_KEY")
    dynamodb = boto3.resource('dynamodb', aws_access_key_id=ACCESS_KEY,
                              aws_secret_access_key=SECRET_KEY,
                              region_name="us-east-1")
    travelDestinationsTable = dynamodb.Table('TravelDestinations')
    allTravelDestinations = travelDestinationsTable.scan()['Items']
    return allTravelDestinations


allTravelDestinations = getAllTravelDestinations()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', travelDestinations=allTravelDestinations)


