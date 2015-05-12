import os
import sys
import platform
import subprocess

"""http://www.itninja.com/software/gougelet-pierre-e/xnview/1-8655"""

if platform.machine() == 'AMD64':
    PROGRAMDIR = 'C:\Program Files (x86)\XnView'
else:
    PROGRAMDIR = 'C:\Program Files\XnView'

"""Имена исполняемых файлов"""
INSTALLER = 'XnView-win-full.exe'
UNINSTALLER = 'unins000.exe'
ASSOCIATE = 'associate.reg'

"""Текущая директория"""
DIR = os.path.dirname(sys.argv[0])

"""Полный путь к исполняемым файлам"""
BNINSTALLER = os.path.join('', DIR, INSTALLER)
BNUNINSTALLER = os.path.join('', PROGRAMDIR, UNINSTALLER)
BNASSOCIATE = os.path.join('', DIR, ASSOCIATE)

def check_files():
    if not os.path.isfile(BNINSTALLER) or not os.path.isfile(BNASSOCIATE):
        print("Отсутствует инсталлятор!!")
        sys.exit()


def taskkill():
    subprocess.call(['taskkill.exe', '/F', '/T',
        '/IM', INSTALLER, '/IM', UNINSTALLER],
        shell=False, stdout=subprocess.PIPE, stderr=sys.stdout)


def remove():
    if os.path.isfile(BNUNINSTALLER):
        subprocess.call([BNUNINSTALLER, '/verysilent'],
            shell=False, stdout=subprocess.PIPE, stderr=sys.stdout)


def install():
    subprocess.call(['regedit', '/S', BNASSOCIATE],
        shell=False, stdout=subprocess.PIPE, stderr=sys.stdout)
    subprocess.call([BNINSTALLER, '/verysilent'],
        shell=False, stdout=subprocess.PIPE, stderr=sys.stdout)

check_files()
taskkill()

if sys.argv[1] == 'install':
    install()
elif sys.argv[1] == 'remove':
    remove()