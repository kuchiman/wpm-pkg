# -*- coding: utf-8 -*-
import sys

sys.path.append(sys.argv[1])
from scriptlib import *

"""Файлы пакета"""
FILES = (
    'Firefox_Setup.exe',
)

"""Имена исполняемых файлов"""
INSTALLER = os.path.join('', DIR, FILES[0])
UNINSTALLER = os.path.join('', SYSDIR, 'Mozilla Firefox',
    'uninstall', 'helper.exe')


def install():
    run_exe(INSTALLER, '/s')


def remove():
    run_exe(UNINSTALLER, '/s')

check_files(FILES)

if ACTION == 'install':
    install()
elif ACTION == 'remove':
    remove()