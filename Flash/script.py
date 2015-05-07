import os
import sys
import subprocess

"""Имена исполняемых файлов"""
INSTALLER1 = 'flash_player_active_x.exe'
INSTALLER2 = 'flash_player.exe'

"""Текущая директория"""
DIR = os.path.dirname(sys.argv[0])

"""Полный путь к исполняемым файлам"""
BNINSTALLER1 = os.path.join('', DIR, INSTALLER1)
BNINSTALLER2 = os.path.join('', DIR, INSTALLER2)


def check_files():
    if not os.path.isfile(BNINSTALLER1) or not os.path.isfile(BNINSTALLER2):
        sys.exit()


def taskkill():
    subprocess.call(['taskkill.exe', '/F', '/T', '/IM', INSTALLER1,
        '/IM', INSTALLER2], shell=False, stdout=subprocess.PIPE)


def remove():
    p1=subprocess.call([BNINSTALLER1, '/uninstall'],
        shell=False, stdout=subprocess.PIPE)
    p2=subprocess.call([BNINSTALLER2, '/uninstall'],
        shell=False, stdout=subprocess.PIPE)


def install():
    p1=subprocess.call([BNINSTALLER1, '/install'],
        shell=False, stdout=subprocess.PIPE)
    p2=subprocess.call([BNINSTALLER2, '/install'],
        shell=False, stdout=subprocess.PIPE)

taskkill()
check_files()

if sys.argv[1] == 'install':
    install()
elif sys.argv[1] == 'remove':
    remove()