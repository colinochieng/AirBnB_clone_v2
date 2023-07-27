#!/usr/bin/python3
"""
script that starts a Flask web application:
- the web application listen on 0.0.0.0, port 5000
- Routes: /states_list: display a HTML page: (inside the tag BODY)
"""
from flask import Flask, render_template
from models import storage
import os


app = Flask(__name__)
app.url_map.strict_slashes = False


def state_cities(query, state):
    """Return list of cities based on state"""
    return [[city.id, city.name] for city in query if city.state_id == state.id]


if os.environ.get("HBNB_TYPE_STORAGE") == 'db':
    @app.teardown_appcontext
    def session_closure(error):
        """
        remove the current SQLAlchemy Session
        """
        if storage is not None:
            storage.close()


@app.route('/states_list')
def states():
    """
    display a HTML page for states
    description of one State: <state.id>: <B><state.name></B>
    """
    from models.state import State
    from models.city import City

    dictionary = storage.all(State)
    list_states = []
    cities = []
    query = storage.all(City).values()
    i = 0
    for value in dictionary.values():
        cities = state_cities(query, value)
        cities.sort(key=lambda city: city[1])
        list_states.append([value.id, value.name, cities])
    sorted_states = sorted(list_states, key=lambda state: state[1])

    print(sorted_states[:2])
    return render_template('8-cities_by_states.html', states_list=sorted_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
