import os
import sys
import platform
import subprocess

if platform.machine() == 'AMD64':
    PROGRAMDIR = 'C:\Program Files (x86)\Mozilla Thunderbird'
else:
    PROGRAMDIR = 'C:\Program Files\Mozilla Thunderbird'

"""Имена исполняемых файлов"""
INSTALLER = 'Thunderbird_Setup.exe'
UNINSTALLER = 'helper.exe'

"""Текущая директория"""
DIR = os.path.dirname(sys.argv[0])

"""Полный путь к исполняемым файлам"""
BNINSTALLER = os.path.join('', DIR, INSTALLER)
BNUNINSTALLER = os.path.join('', PROGRAMDIR, 'uninstall', UNINSTALLER)


def taskkill():
    subprocess.call(['taskkill.exe', '/F', '/T', '/IM', INSTALLER,
        '/IM', UNINSTALLER], shell=False, stdout=subprocess.PIPE)


def remove():
    if os.path.isfile(BNUNINSTALLER):
        subprocess.call([BNUNINSTALLER, '/s'],
            shell=False, stdout=subprocess.PIPE)


def install():
    if os.path.isfile(BNINSTALLER):
        subprocess.call([BNINSTALLER, '/s'],
            shell=False, stdout=subprocess.PIPE)

taskkill()

if sys.argv[1] == 'install':
    install()
elif sys.argv[1] == 'remove':
    remove()