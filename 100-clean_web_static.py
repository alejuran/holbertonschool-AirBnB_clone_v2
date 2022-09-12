#!/usr/bin/python3
""" Cleans deployment"""

from fabric.api import *
import os
from datetime import datetime
import tarfile


env.hosts = ['52.87.221.123', '52.23.223.26']


def do_clean(num=0):
    """ Removes all but given number of archives"""
    num = int(num)
    if num < 2:
        num = 1
    num += 1
    num = str(num)
    with lcd("versions"):
        local("ls -1t | grep web_static_.*\.tgz | tail -n +" +
              num + " | xargs -I {} rm -- {}")
    with cd("/data/web_static/releases"):
        run("ls -1t | grep web_static_ | tail -n +" +
            num + " | xargs -I {} rm -rf -- {}")
