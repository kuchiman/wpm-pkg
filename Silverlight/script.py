# -*- coding: utf-8 -*-
import sys

sys.path.append(sys.argv[1])
from scriptlib import *

"""Файлы пакета"""
FILES = (
    'silverlight_64.msi',
    'Silverlight_64.msp',
    'silverlight_32.msi',
    'Silverlight_32.msp'
)

"""Имена исполняемых файлов"""
if ARCH == '64':
    INSTALLER = os.path.join('', DIR, FILES[0])
    UPDATE = os.path.join('', DIR, FILES[1])
else:
    INSTALLER = os.path.join('', DIR, FILES[2])
    UPDATE = os.path.join('', DIR, FILES[3])


def install():
    run_msi('/i', INSTALLER, '/update', UPDATE)


def remove():
    run_msi('/x', INSTALLER)

check_files(FILES)

if ACTION == 'install':
    install()
elif ACTION == 'remove':
    remove()