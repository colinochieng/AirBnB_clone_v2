#!/usr/bin/python3
"""
script that starts a Flask web application:
- The web application is listening on 0.0.0.0, port 5000
- Uses storage for fetching data from the storage engine (FileStorage or DBStorage)
- Routes:
- /states: display a HTML page: (inside the tag BODY)
- /states/<id>: display a HTML page: (inside the tag BODY)
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states():
    """display a HTML page"""
    from models.state import State
    states_list = list(storage.all(State).values())
    states_list.sort(key=lambda state: state.name)
    return render_template('9-states.html', sorted_states=states_list)


@app.route('/states/<id>')
def state_with_id(id):
    """returns state with its cities based on state id"""
    import os
    from models.state import State
    state = storage.all(State).get(f'State.{id}')

    if not state:
        return render_template('9-states.html', not_found='Not found!')  

    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = state.cities
    else:
        cities = state.cities()
    cities.sort(key=lambda city: city.name)
    return render_template('9-states.html', cities=cities, state=state, id=1)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
