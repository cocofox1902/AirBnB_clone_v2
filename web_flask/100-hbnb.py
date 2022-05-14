#!/usr/bin/python3
""" 10 - hbnb_filters.py """
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Return result """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place).items()
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exc):
    """ Return result """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
