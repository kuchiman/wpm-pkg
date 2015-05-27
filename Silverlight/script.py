# -*- coding: utf-8 -*-
import sys

sys.path.append(sys.argv[1])
from scriptlib import *

"""Файлы пакета"""
FILES = (
    'Silverlight.exe',
    'Silverlight_x64.exe',
)

"""Имена исполняемых файлов"""
if ARCH == '64':
    INSTALLER = os.path.join('', DIR, FILES[1])
else:
    INSTALLER = os.path.join('', DIR, FILES[0])


def install():
    run_exe(INSTALLER, '/q')


def remove():
    run_exe(INSTALLER, '/qu')

check_files(FILES)

if ACTION == 'install':
    install()
elif ACTION == 'remove':
    remove()