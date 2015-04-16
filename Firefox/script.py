import os, sys, platform, subprocess

if platform.machine() == 'AMD64':
    PROGRAMDIR = 'C:\Program Files (x86)\Mozilla Firefox'
else:
    PROGRAMDIR = 'C:\Program Files\Mozilla Firefox'

INSTALLER = 'Firefox_Setup.exe'
UNINSTALLER = 'helper.exe'

DIR = os.path.dirname(sys.argv[0])
BNINSTALLER = os.path.join('', DIR, INSTALLER)
BNUNINSTALLER = os.path.join('', PROGRAMDIR, 'uninstall', UNINSTALLER)


def check_files():
    if not os.path.isfile(BNINSTALLER):
        print("Отсутствует инсталлятор!!")
        raise SystemExit(1)


def taskkill():
    subprocess.call(['taskkill.exe', '/F', '/T',
        '/IM', INSTALLER, '/IM', UNINSTALLER],
        shell=False, stdout=subprocess.PIPE, stderr=STDOUT)


def remove():
    if not os.path.isfile(BNUNINSTALLER):
        print("Программа уже удалена!!")
    else:
        print("Программа удаляется...")
        subprocess.call([BNUNINSTALLER, '/s'],
            shell=False, stdout=subprocess.PIPE, stderr=STDOUT)


def install():
    print("Установка...")
    subprocess.call([BNINSTALLER, '/s'],
        shell=False, stdout=subprocess.PIPE, stderr=STDOUT)

check_files()
taskkill()

if sys.argv[1] == 'install':
    install()
elif sys.argv[1] == 'remove':
    remove()