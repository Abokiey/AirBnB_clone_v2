#!/usr/bin/python3

import os
from fabric.api import env, put, run, local
from datetime import datetime


env.hosts = ['54.236.44.210', '52.86.185.202']

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

def do_deploy(archive_path):
    """deploy archive path to the web servers"""
    if not os.path.exists(archive_path):
        return False

    file_name = os.path.basename(archive_path)
    dir_name = file_name.replace(".tgz", "")
    dir_path = "/data/web_static/releases/{}/".format(dir_name)
    success = False

    try:
        """Uploads the archive to the /tmp/ directory of theserver"""
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(dir_path))
        """extract files to tmp dir"""
        run("tar -xzf /tmp/{} -C {}".format(file_name, dir_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(dir_path, dir_path))
        run("rm -rf {}web_static".format(dir_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(dir_path))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success

def deploy():
    """creates and distributes archive files to the web servers.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
