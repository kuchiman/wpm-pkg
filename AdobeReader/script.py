# -*- coding: utf-8 -*-
import os
import sys
import subprocess

"""Имена исполняемых файлов"""
"""msi получен из оригинально exe файла, от туда же необходим Data1.cab"""
INSTALLER = 'AcroRead.msi'

"""Текущая директория"""
DIR = os.path.dirname(sys.argv[0])

"""Полный путь к исполняемым файлам"""
BNINSTALLER = os.path.join('', DIR, INSTALLER)


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