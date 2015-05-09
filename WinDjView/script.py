# -*- coding: utf-8 -*-
import os
import sys
import platform
import subprocess

if platform.machine() == 'AMD64':
    PROGRAMDIR = 'C:\Program Files (x86)\WinDjView'
else:
    PROGRAMDIR = 'C:\Program Files\WinDjView'

"""Имена исполняемых файлов"""
INSTALLER = 'WinDjView-2.0.2-Setup.exe'
UNINSTALLER = 'uninstall.exe'

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
        subprocess.call([BNUNINSTALLER, '/s'],
            shell=False, stdout=subprocess.PIPE, stderr=STDOUT)


def install():
    subprocess.call([BNINSTALLER, '/s'],
        shell=False, stdout=subprocess.PIPE, stderr=STDOUT)

check_files()
taskkill()

if sys.argv[1] == 'install':
    install()
elif sys.argv[1] == 'remove':
    remove()