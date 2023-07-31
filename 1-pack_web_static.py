#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo
"""
from fabric.api import local
import os
import datetime


def do_pack():
    """
    function to pack
    """
    if not os.path.isdir('versions'):
        os.mkdir('versions')
    date = datetime.datetime.now()
    archive = '''versions/web_static_{}{}{}{}{}{}.tgz'''.format(
        date.year,
        date.month,
        date.day,
        date.hour,
        date.minute,
        date.second
    )
    try:
        print("Packing web_static to {}".format(archive))
        local('tar -cvzf {} web_static'.format(archive))
        size = os.stat(archive).st_size
        print("web_static packed: {} -> {} Bytes".format(archive, size))
    except Exception:
        archive = None
    return archive
