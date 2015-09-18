# -*- coding: utf-8 -*-
import sys

sys.path.append(sys.argv[1])
from scriptlib import *

"""Файлы пакета"""
FILES = (
    'SETUP.EXE',
    'library.MSP',
)

"""Имена исполняемых файлов"""
INSTALLER = os.path.join('', DIR, FILES[0])

"""Файл настроек"""
"""setup.exe /admin   - administrativ installation
In key page set none for interface"""
MSP = os.path.join('', DIR, FILES[1])


def install():
    run_exe(INSTALLER, '/adminfile', MSP)


def remove():
    run_exe(INSTALLER, '/uninstall')

check_files(FILES)

if ACTION == 'install':
    install()
elif ACTION == 'remove':
    remove()
