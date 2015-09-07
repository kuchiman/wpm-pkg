# -*- coding: utf-8 -*-
import sys

sys.path.append(sys.argv[1])
from scriptlib import *

"""Файлы пакета"""
FILES = (
    'gajim-0.16.3-2.exe',
)

"""Имена исполняемых файлов"""
INSTALLER = os.path.join('', DIR, FILES[0])
UNINSTALLER = os.path.join('', SYSDIR, 'Gajim', 'Uninstall.exe')


def install():
    run_exe(INSTALLER, '/S')


def remove():
    run_exe(UNINSTALLER, '/S')

check_files(FILES)

if ACTION == 'install':
    install()
elif ACTION == 'remove':
    remove()