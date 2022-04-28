#!/usr/bin/python3
""" 1 - pack_web_static.py """
from fabric.api import local
from datetime import datetime


def do_pack():
    """do_pack"""
    now = datetime.now()
    now = now.strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_' + now + '.tgz'

    local('mkdir -p versions/')
    result = local('tar -cvzf {} web_static/'.format(archive_path))

    if result.succeeded:
        return archive_path
    return None
