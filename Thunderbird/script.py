import os, sys, platform, subprocess

if platform.machine() == 'AMD64':
    PROGRAMDIR = 'C:\Program Files (x86)\Mozilla Thunderbird'
else:
    PROGRAMDIR = 'C:\Program Files\Mozilla Thunderbird'

INSTALLER = 'Thunderbird_Setup.exe'
UNINSTALLER = 'helper.exe'


def taskkill():
    subprocess.call(['taskkill.exe',
        '/F', '/T',
        '/IM', INSTALLER,
        '/IM', UNINSTALLER],
        shell=False, stdout=subprocess.PIPE)


def remove():
    tmp = os.path.join('', PROGRAMDIR, 'uninstall', UNINSTALLER)
    if not os.path.isfile(tmp):
        print("Программа уже удалена!!")
    else:
        print("Программа удаляется...")
        subprocess.call([os.path.join('', PROGRAMDIR, 'uninstall', UNINSTALLER),
        '/s'], shell=False, stdout=subprocess.PIPE)


def install():
    if not os.path.isfile(INSTALLER):
        print("Отсутствует установщик!!")
    else:
        print("Установка...")
        subprocess.call([INSTALLER, '/s'], shell=False, stdout=subprocess.PIPE)

taskkill()

if sys.argv[1] == 'install':
    install()
elif sys.argv[1] == 'remove':
    remove()