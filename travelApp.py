from flask import Flask, render_template

from destination_directories import DynamoDestinationDirectory

destination_directory = DynamoDestinationDirectory()
all_travel_destinations = destination_directory.get_all_destinations()
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', travelDestinations=all_travel_destinations)


@app.route("/destination/<destination_id>")
def destination(destination_id):
    return render_template('destination.html', destination=destination_directory.get_destination(destination_id))
