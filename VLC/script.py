# -*- coding: utf-8 -*-
import sys

sys.path.append(sys.argv[1])
from scriptlib import *

"""Файлы пакета"""
FILES = (
    'vlc-2.2.1-win32.exe',
    'vlc-2.2.1-win64.exe'
)

"""Имена исполняемых файлов"""
if ARCH == '64':
    INSTALLER = os.path.join('', DIR, FILES[1])
else:
    INSTALLER = os.path.join('', DIR, FILES[0])

UNINSTALLER = os.path.join('', SYSDIR, 'VideoLAN', 'VLC', 'uninstall.exe')


def install():
    run_exe(INSTALLER, '/S')


def remove():
    run_exe(UNINSTALLER, '/S')

check_files(FILES)

if ACTION == 'install':
    install()
elif ACTION == 'remove':
    remove()