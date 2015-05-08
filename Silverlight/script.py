import os
import sys
import platform
import subprocess

"""Имена исполняемых файлов"""
if platform.machine() == 'AMD64':
    INSTALLER = 'silverlight_64.msi'
    UPDATE = 'Silverlight_64.msp'
else:
    INSTALLER = 'silverlight_32.msi'
    UPDATE = 'Silverlight_32.msp'

"""Текущая директория"""
DIR = os.path.dirname(sys.argv[0])

"""Полный путь к исполняемым файлам"""
BNINSTALLER = os.path.join('', DIR, INSTALLER)
BNUPDATE = os.path.join('', DIR, UPDATE)


def taskkill():
    subprocess.call(['taskkill.exe', '/F', '/T', '/IM', INSTALLER],
        shell=False, stdout=subprocess.PIPE)


def remove():
    if os.path.isfile(BNINSTALLER):
        subprocess.call(['msiexec', '/qn', '/x', BNINSTALLER],
            shell=False, stdout=subprocess.PIPE)


def install():
    if os.path.isfile(BNINSTALLER):
        subprocess.call(['msiexec', '/qn', '/i', BNINSTALLER,
            '/update', BNUPDATE], shell=False, stdout=subprocess.PIPE)

taskkill()

if sys.argv[1] == 'install':
    install()
elif sys.argv[1] == 'remove':
    remove()