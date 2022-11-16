#!/usr/bin/python3
# Fabfile to distribute to a web server.
from fabric.api import *
from datetime import datetime
from fabric.decorators import runs_once


@runs_once
def do_pack():
    """ script that generates a .tgz archive from web_static """
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(filename))
    
    if result.failed:
        return None
    return filename
