import os
import sys
import platform
import subprocess

if platform.machine() == 'AMD64':
    PROGRAMDIR = 'C:\Program Files (x86)\XnView'
else:
    PROGRAMDIR = 'C:\Program Files\XnView'

"""Имена исполняемых файлов"""
INSTALLER = 'XnView-win-full.exe'
UNINSTALLER = 'unins000.exe'

"""Текущая директория"""
DIR = os.path.dirname(sys.argv[0])

"""Полный путь к исполняемым файлам"""
BNINSTALLER = os.path.join('', DIR, INSTALLER)
BNUNINSTALLER = os.path.join('', PROGRAMDIR, UNINSTALLER)


def check_files():
    if not os.path.isfile(BNINSTALLER):
        print("Отсутствует инсталлятор!!")
        sys.exit()


def taskkill():
    subprocess.call(['taskkill.exe', '/F', '/T',
        '/IM', INSTALLER, '/IM', UNINSTALLER],
        shell=False, stdout=subprocess.PIPE, stderr=STDOUT)


def remove():
    if os.path.isfile(BNUNINSTALLER):
        subprocess.call([BNUNINSTALLER, '/silent'],
            shell=False, stdout=subprocess.PIPE, stderr=STDOUT)


def install():
    subprocess.call([BNINSTALLER, '/silent'],
        shell=False, stdout=subprocess.PIPE, stderr=STDOUT)

check_files()
taskkill()

if sys.argv[1] == 'install':
    install()
elif sys.argv[1] == 'remove':
    remove()