# -*- coding: utf-8 -*-
import sys

sys.path.append(sys.argv[1])
from scriptlib import *

"""Файлы пакета"""
FILES = (
    'gimp-2.8.14-setup-1.exe',
    'gimp-help-2-2.8.1-ru-setup.exe',
)

"""Имена исполняемых файлов"""
INSTALLER0 = os.path.join('', DIR, FILES[1])
INSTALLER1 = os.path.join('', DIR, FILES[0])

UNINSTALLER = os.path.join('', SYSDIR, 'GIMP',
    'uninst', 'unins000.exe')


def install():
    run_exe(INSTALLER0, '/verysilent', '/norestart')
    run_exe(INSTALLER0, '/silent', '/norestart')


def remove():
    run_exe(UNINSTALLER, '/verysilent', '/norestart')

check_files(FILES)

if ACTION == 'install':
    install()
elif ACTION == 'remove':
    remove()