# -*- coding: utf-8 -*-
#http://ftp.mozilla.org/pub/firefox/releases
import sys

sys.path.append(sys.argv[1])
from scriptlib import *

"""Файлы пакета"""
FILES = (
    'Firefox Setup 37.0b7.exe',
    'all.js'
)

"""Имена исполняемых файлов"""
INSTALLER = os.path.join('', DIR, FILES[0])
UNINSTALLER = os.path.join('', SYSDIR, 'Mozilla Firefox',
    'uninstall', 'helper.exe')

"""Конфиг"""
CONFDIR = os.path.join('', SYSDIR, 'Mozilla Firefox', 'defaults', 'pref')


def install():
    run_exe(INSTALLER, '/s')
    copy(FILES[1], CONFDIR)


def remove():
    run_exe(UNINSTALLER, '/s')

check_files(FILES)

if ACTION == 'install':
    install()
elif ACTION == 'remove':
    remove()