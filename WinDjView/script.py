# -*- coding: utf-8 -*-
import sys

sys.path.append(sys.argv[1])
from scriptlib import *

"""Файлы пакета"""
FILES = (
    'WinDjView-2.1-Setup.exe',
)

"""Имена исполняемых файлов"""
INSTALLER = os.path.join('', DIR, FILES[0])
UNINSTALLER = os.path.join('', SYSDIR, 'WinDjView', 'uninstall.exe')


def install():
    run_exe(INSTALLER, '/S')


def remove():
    #нужно подумать как вывести эту проверку в библиотечный файл
    if os.path.isfile(UNINSTALLER):
        run_exe(UNINSTALLER, '/S')

check_files(FILES)

if ACTION == 'install':
    install()
elif ACTION == 'remove':
    remove()