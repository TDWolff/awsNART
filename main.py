import threading
from flask import render_template, request, jsonify  # Import necessary Flask modules


# Import "packages" from "this" project
from __init__ import app, db  # Definitions initialization
from model.jokes import initJokes
from model.users import initUsers
from model.players import initPlayers
from model.encode import initEncode
from flask_cors import CORS


# Setup APIs
from api.covid import covid_api  # Blueprint import API definition
from api.joke import joke_api  # Blueprint import API definition
from api.player import player_api
from api.encode import encode_api
from api.database import login_api

# Initialize the SQLAlchemy object to work with the Flask app instance
db.init_app(app)

app.register_blueprint(login_api)


# Setup App pages
from projects.projects import app_projects  # Blueprint directory import projects definition

# Initialize the SQLAlchemy object to work with the Flask app instance
db.init_app(app)

# Register URIs
app.register_blueprint(joke_api)  # Register API routes
app.register_blueprint(covid_api)  # Register API routes
app.register_blueprint(player_api)
app.register_blueprint(app_projects)  # Register app pages
app.register_blueprint(encode_api)  # Register encode API routes

@app.errorhandler(404)  # Catch for URL not found
def page_not_found(e):
    # Note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # Connects the default URL to index() function
def index():
    return render_template("index.html")

@app.route('/table/')  # Connects /stub/ URL to stub() function
def table():
    return render_template("table.html")


@app.before_first_request
def activate_job():  # Activate these items
    initJokes()
    initPlayers()
    initEncode()

# This runs the application on the development server
if __name__ == "__main__":
    # Change name for testing
    from flask_cors import CORS
    cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:8120"}})
    app.run(debug=True, host="0.0.0.0", port="8120")
