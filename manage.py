#!/usr/bin/env python

from flask.ext.script import Manager
from subprocess import call

import run
import os

manager = Manager(run.app)

@manager.command
def update():
    call(['pip', 'install', '-r', 'requirements.txt'])
    print('Done updating.')


if __name__ == '__main__':
    manager.run()
