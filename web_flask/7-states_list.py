#!/usr/bin/python3
"""
script that starts a Flask web application:
- the web application listen on 0.0.0.0, port 5000
- Routes: /states_list: display a HTML page: (inside the tag BODY)
- 
"""
from flask import Flask, render_template
from models import storage
import os


app = Flask(__name__)
app.url_map.strict_slashes = False

if os.environ.get("HBNB_TYPE_STORAGE") == 'db':
    @app.teardown_appcontext
    def session_closure():
        """
        remove the current SQLAlchemy Session
        """
        storage.close()


@app.route('/states_list')
def states():
    """
    display a HTML page for states
    description of one State: <state.id>: <B><state.name></B>
    """
    from models.state import State
    dictionary = storage.all(State)
    list_states = []

    for values in dictionary.values:
        list_states.append([values.id, values.name])
    sorted_states = sorted(list_states, key=lambda state: state[1])
    return render_template('7-states_list.html', states_list=sorted_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=500)