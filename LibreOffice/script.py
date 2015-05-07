import os
import sys
import subprocess

"""Имена исполняемых файлов"""
INSTALLER1 = 'LibreOffice_Win_x86.msi'
INSTALLER2 = 'LibreOffice_Win_x86_helppack_ru.msi'

"""Текущая директория"""
DIR = os.path.dirname(sys.argv[0])

"""Полный путь к исполняемым файлам"""
BNINSTALLER1 = os.path.join('', DIR, INSTALLER1)
BNINSTALLER2 = os.path.join('', DIR, INSTALLER2)


def check_files():
    if not os.path.isfile(BNINSTALLER1) or not os.path.isfile(BNINSTALLER2):
        sys.exit()


def taskkill():
    subprocess.call(['taskkill.exe', '/F', '/T',
        '/IM', INSTALLER1, '/IM', INSTALLER2],
        shell=False, stdout=None)


def remove():
    p1=subprocess.call(['msiexec', '/qn', '/x', BNINSTALLER1],
        shell=True, stdout=None)
    p2=subprocess.call(['msiexec', '/qn', '/x', BNINSTALLER2],
        shell=True, stdout=None)


def install():
    p1=subprocess.call(['msiexec', '/qn', '/i', BNINSTALLER1,
        'RebootYesNo=No', 'REGISTER_ALL_MSO_TYPES=0', 'UI_LANGS=ru_RU'],
        shell=True, stdout=None)
    p2=subprocess.call(['msiexec', '/qn', '/i', BNINSTALLER2],
        shell=True, stdout=None)

check_files()
taskkill()


if sys.argv[1] == 'install':
    install()
elif sys.argv[1] == 'remove':
    remove()