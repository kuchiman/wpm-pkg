# -*- coding: utf-8 -*-
import sys

sys.path.append(sys.argv[1])
from scriptlib import *

"""Файлы пакета"""
FILES = (
    '7z920-x64.msi',
    '7z920.msi'
)

"""Имена исполняемых файлов"""
if ARCH == '64':
    INSTALLER = os.path.join('', DIR, FILES[0])
else:
    INSTALLER = os.path.join('', DIR, FILES[1])


def install():
    run_msi('/i', INSTALLER)


def remove():
    run_msi('/x', INSTALLER)

check_files(FILES)

if ACTION == 'install':
    install()
elif ACTION == 'remove':
    remove()