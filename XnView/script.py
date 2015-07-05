# -*- coding: utf-8 -*-
import sys

sys.path.append(sys.argv[1])
from scriptlib import *

"""http://www.itninja.com/software/gougelet-pierre-e/xnview/1-8655"""

"""Файлы пакета"""
FILES = (
    'XnView-win-full.exe',
    'associate.reg'
)

"""Имена исполняемых файлов"""
INSTALLER = os.path.join('', DIR, FILES[0])
UNINSTALLER = os.path.join('', SYSDIR, 'XnView', 'unins000.exe')

"""Файл реестра"""
ASSOCIATE = os.path.join('', DIR, FILES[1])


def install():
    run_exe(INSTALLER, '/verysilent')
    run_exe('regedit', '/S', ASSOCIATE)


def remove():
    run_exe(UNINSTALLER, '/verysilent')

check_files(FILES)

if ACTION == 'install':
    install()
elif ACTION == 'remove':
    remove()