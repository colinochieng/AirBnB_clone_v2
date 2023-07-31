#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo
"""
from fabric import Connection, task
import fabric
import os
import datetime

@task
def do_pack(c):
    """
    function to pack
    """
    if not os.path.isdir('versions'):
        os.mkdir('versions')
    date = datetime.datetime.now()
    archive = '''web_static_{}{}{}{}{}{}.tgz'''.format(
        date.year,
        date.month,
        date.day,
        date.hour,
        date.minute,
        date.second
    )
    try:
        conn = Connection(host='localhost')
        conn.local(f'tar -cvzf {archive} web_static')
        size = os.stat(archive).st_size
        print("web_static packed: {} -> {} Bytes".format(archive, size))
    except Exception:
        archive = None
    return archive
