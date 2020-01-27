import sys
from cx_Freeze import setup, Executable

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"

exe = Executable(
        script = "GTA-5-Private-Public-Lobby.py",
        icon = "icon2.ico",
        targetName = "GTA-5-Private-Public-Lobby.exe",
        base = base
       
        )
includefiles = ["icon2.ico"]

setup(
    name = "GTA-5-Private-Public-Lobby",
    version = "0.1",
    description = "GTA-5-Private-Public-Lobby",
    author = "Mirrorble",
    options = {'build_exe': {'include_files':includefiles}},
    executables = [exe]
)