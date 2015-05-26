# -*- coding: utf-8 -*-
import sys

sys.path.append(sys.argv[1])
from scriptlib import *

"""Файлы пакета"""
FILES = (
    'flash_player_active_x.exe',
    'flash_player.exe'
)

"""Имена исполняемых файлов"""
INSTALLER0 = os.path.join('', DIR, FILES[0])
INSTALLER1 = os.path.join('', DIR, FILES[1])


def install():
    run_exe(INSTALLER0, '/install')
    run_exe(INSTALLER1, '/install')


def remove():
    run_exe(INSTALLER0, '/uninstall')
    run_exe(INSTALLER1, '/uninstall')

check_files(FILES)

if ACTION == 'install':
    install()
elif ACTION == 'remove':
    remove()