from flask import Flask, render_template, request, flash
from credentials import FLASK_SECRET_KEY
from destination_directories import DynamoDestinationDirectory

destination_directory = DynamoDestinationDirectory()
all_travel_destinations = destination_directory.get_all_destinations()

app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_SECRET_KEY


@app.route("/")
def index():
    return render_template('index.html', travelDestinations=all_travel_destinations)


@app.route("/destination/<destination_id>")
def destination(destination_id):
    return render_template('destination.html', destination=destination_directory.get_destination(destination_id))


@app.route("/destination/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        destination_name = request.form["destinationName"]
        optimal_quarter = request.form["optimalQuarter"]
        priority = int(request.form["priority"])

        if not destination_name:
            flash("Destination name is required!")
        elif not optimal_quarter:
            flash("Optimal quarter is required!")
        elif not priority:
            flash("Priority is required!")
        else:
            destination_directory.add_new_destination(optimal_quarter=optimal_quarter, priority=priority,
                                                      name=destination_name)

    return render_template("createDestination.html")
