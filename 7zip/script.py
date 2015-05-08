import os
import sys
import platform
import subprocess

"""Имена исполняемых файлов"""
if platform.machine() == 'AMD64':
    INSTALLER = '7z920-x64.msi'
else:
    INSTALLER = '7z920.msi'

"""Текущая директория"""
DIR = os.path.dirname(sys.argv[0])

"""Полный путь к исполняемым файлам"""
BNINSTALLER = os.path.join('', DIR, INSTALLER)


def check_files():
    if not os.path.isfile(BNINSTALLER):
        print("Отсутствует инсталлятор!!")
        sys.exit()


def taskkill():
    subprocess.call(['taskkill.exe', '/F', '/T', '/IM', INSTALLER],
        shell=False, stdout=subprocess.PIPE)


def remove():
    if os.path.isfile(BNINSTALLER):
        subprocess.call(['msiexec', '/qn', '/x', BNINSTALLER],
            shell=False, stdout=subprocess.PIPE)


def install():
    if os.path.isfile(BNINSTALLER):
        subprocess.call(['msiexec', '/qn', '/i', BNINSTALLER],
            shell=False, stdout=subprocess.PIPE)

taskkill()

if sys.argv[1] == 'install':
    install()
elif sys.argv[1] == 'remove':
    remove()