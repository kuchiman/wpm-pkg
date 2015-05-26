# -*- coding: utf-8 -*-
import sys

sys.path.append(sys.argv[1])
from scriptlib import *

"""Файлы пакета"""
FILES = (
    'AcroRead.msi',
)

"""Имена исполняемых файлов"""
INSTALLER = os.path.join('', DIR, FILES[0])


def install():
    run_msi('/i', INSTALLER)


def remove():
    run_msi('/x', INSTALLER)

check_files(FILES)

if ACTION == 'install':
    install()
elif ACTION == 'remove':
    remove()