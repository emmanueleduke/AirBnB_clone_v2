#!/usr/bin/python3
import os
from datetime import datetime
from fabric.api import local

def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(timestamp)

    if not os.path.exists("versions"):
        os.makedirs("versions")

    result = local("tar -czvf {} web_static".format(file_name))
    if result.failed:
        return None
    return file_name


