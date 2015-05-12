import os
import sys
import platform
import subprocess

if platform.machine() == 'AMD64':
    PROGRAMDIR = 'C:\Program Files (x86)\Mozilla Firefox'
else:
    PROGRAMDIR = 'C:\Program Files\Mozilla Firefox'

"""Имена исполняемых файлов"""
INSTALLER = 'Firefox_Setup.exe'
UNINSTALLER = 'helper.exe'

"""Текущая директория"""
DIR = os.path.dirname(sys.argv[0])

"""Полный путь к исполняемым файлам"""
BNINSTALLER = os.path.join('', DIR, INSTALLER)
BNUNINSTALLER = os.path.join('', PROGRAMDIR, 'uninstall', UNINSTALLER)


def check_files():
    if not os.path.isfile(BNINSTALLER):
        print("Отсутствует инсталлятор!!")
        sys.exit()


def taskkill():
    subprocess.call(['taskkill.exe', '/F', '/T',
        '/IM', INSTALLER, '/IM', UNINSTALLER],
        shell=False, stdout=subprocess.PIPE, stderr=sys.stdout)


def run(*command):
    p = subprocess.call(list(command),
        shell=False, stdout=subprocess.PIPE, stderr=sys.stdout)
    return p


def remove():
    if os.path.isfile(BNUNINSTALLER):
        run(BNUNINSTALLER, '/s')
        #subprocess.call([BNUNINSTALLER, '/s'],
            #shell=False, stdout=subprocess.PIPE, stderr=sys.stdout)


def install():
    run(BNINSTALLER, '/s')
    #subprocess.call([BNINSTALLER, '/s'],
        #shell=False, stdout=subprocess.PIPE, stderr=sys.stdout)

check_files()
taskkill()

if sys.argv[1] == 'install':
    install()
elif sys.argv[1] == 'remove':
    remove()