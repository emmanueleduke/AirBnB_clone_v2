#!/usr/bin/env python3
from invoke import task
@task

import os
import tarfile
from datetime import datetime

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{timestamp}.tgz"
    archive_path = f"versions/{archive_name}"

    os.makedirs("versions", exist_ok=True)
    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add("web_static", arcname=os.path.basename("web_static"))

    return archive_path

archive_path = do_pack()
if archive_path:
    print(f"Archive created successfully: {archive_path}")
else:
    print("Archive creation failed.")

