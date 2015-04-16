import os, sys, platform, subprocess

if platform.machine() == 'AMD64':
    INSTALLER = 'silverlight_64.msi'
    UPDATE = 'Silverlight_64.msp'
else:
    INSTALLER = 'silverlight_32.msi'
    UPDATE = 'Silverlight_32.msp'


def taskkill():
    subprocess.call(['taskkill.exe',
        '/F', '/T',
        '/IM', INSTALLER],
        shell=False, stdout=subprocess.PIPE)


def remove():
    if not os.path.isfile(INSTALLER):
        print("Отсутствует установщик!!")
    else:
        print("Программа удаляется...")
        subprocess.call(['msiexec', '/qn', '/x',
            os.path.join('', os.getcwd(), INSTALLER)],
            shell=False, stdout=subprocess.PIPE)


def install():
    if not os.path.isfile(INSTALLER):
        print("Отсутствует установщик!!")
    else:
        print("Установка...")
        subprocess.call(['msiexec', '/qn',
            '/i', INSTALLER,
            '/update', UPDATE], shell=False, stdout=subprocess.PIPE)

taskkill()

if sys.argv[1] == 'install':
    install()
elif sys.argv[1] == 'remove':
    remove()