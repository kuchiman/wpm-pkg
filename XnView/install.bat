@echo off
set PATH=%SYSTEMROOT%\SYSTEM32;%SYSTEMROOT%;%SYSTEMROOT%\SYSTEM32\WBEM;

:: http://biblprog.org.ua/ru/net_framework/
set INSTALLER=XnView-win-full.exe
set UNINSTALLER=unins000.exe

:UnInstall
taskkill.exe      >nul 2>nul /F /T /IM "%INSTALLER%" /IM "%UNINSTALLER%"
"%SYSTEMROOT%\XnView\%UNINSTALLER%">nul 2>nul /silent
if /I "%~1"=="-u" goto Finish

:Install
"%~dp0%INSTALLER%">nul 2>nul /silent

:Finish
