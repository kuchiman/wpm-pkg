# -*- coding: utf-8 -*-
import sys

sys.path.append(sys.argv[1])
from scriptlib import *

"""Файлы пакета"""
FILES = (
    'LibreOffice_4.4.3_Win_x86.msi',
    'LibreOffice_4.4.3_Win_x86_helppack_ru.msi'
)

"""Имена исполняемых файлов"""
INSTALLER0 = os.path.join('', DIR, FILES[0])
INSTALLER1 = os.path.join('', DIR, FILES[1])


def install():
    run_msi('/i', INSTALLER0, 'RebootYesNo=No', 'REGISTER_ALL_MSO_TYPES=0',
        'UI_LANGS=ru_RU', 'REMOVE=gm_o_Onlineupdate', 'ADDLOCAL=ru')
    run_msi('/i', INSTALLER1)


def remove():
    run_msi('/x', INSTALLER0)
    run_msi('/x', INSTALLER1)

check_files(FILES)

if ACTION == 'install':
    install()
elif ACTION == 'remove':
    remove()