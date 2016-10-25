# -*- coding: utf-8 -*-
import sys

sys.path.append(sys.argv[1])
from scriptlib import *

"""Файлы пакета"""
FILES = (
    'VMware-Horizon-Client-x86-4.2.0-4336726.exe',
    'VMware-Horizon-Client-x86_64-4.2.0-4336726.exe',
)

"""Имена исполняемых файлов"""
if ARCH == '64':
    INSTALLER = os.path.join('', DIR, FILES[1])
else:
    INSTALLER = os.path.join('', DIR, FILES[0])


def install():
    run_exe(INSTALLER,
        '/s /v "/qn ADDLOCAL=ALL REBOOT=ReallySuppress VDM_SERVER=view-cs.smmc"')


def remove():
    run_exe(INSTALLER, '/s /v "/qx REBOOT=ReallySuppress"')

check_files(FILES)

if ACTION == 'install':
    install()
elif ACTION == 'remove':
    remove()
