#!/usr/bin/python3
"""generate a tgz file from archive"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """compress files in a directory"""
    now = datetime.now()
    now = now.strftime('%Y%m%d%H%M%S')
    path = 'versions/web_static_' + now + '.tgz'

    local('mkdir -p versions/')
    res = local('tar -cvzf {} web_static/'.format(path))

    if res.succeeded:
        return path
    return None
