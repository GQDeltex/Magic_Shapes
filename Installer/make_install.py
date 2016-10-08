import os
import shutil


if os.name == 'nt':
    os.system("pyinstaller --onefile windows_install.py")
    shutil.rmtree("./build")
    os.rename("./dist/windows_install.exe", "./windows_install.exe")
    shutil.rmtree("./dist")
    os.remove("windows_install.spec")
else:
    os.system("pyinstaller --onefile linux_install.py")
    shutil.rmtree("./build")
    os.rename("./dist/linux_install", "./linux_install.exe")
    shutil.rmtree("./dist")
    os.remove("linux_install.spec")    