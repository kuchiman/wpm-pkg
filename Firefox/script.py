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

"""Файлы пакета"""
FILES = (
    INSTALLER,
    UNINSTALLER)

"""Текущая директория"""
DIR = os.path.dirname(sys.argv[0])

"""Полный путь к исполняемым файлам"""
BNINSTALLER = os.path.join('', DIR, INSTALLER)
BNUNINSTALLER = os.path.join('', PROGRAMDIR, 'uninstall', UNINSTALLER)


def check_files(files):
    i = []
    current_dir = os.path.dirname(sys.argv[0])
    for f in files:
        if not os.path.isfile(os.path.join('', current_dir, f)):
            i.append(f)

    if len(i):
        print("Отсутствуют файлы!!")
        for s in i:
            print(s)
        sys.exit()


def run(*command):
    p = subprocess.call(list(command),
        shell=False, stdout=subprocess.PIPE, stderr=sys.stdout)
    return p


def taskkill(*names):
    command = ['taskkill.exe', '/F', '/T']
    for n in names:
        command += ['/IM', n]
    run(*command)


def remove():
    run(BNUNINSTALLER, '/s')


def install():
    run(BNINSTALLER, '/s')

check_files(FILES)
taskkill(INSTALLER, UNINSTALLER)

if sys.argv[1] == 'install':
    install()
elif sys.argv[1] == 'remove':
    remove()