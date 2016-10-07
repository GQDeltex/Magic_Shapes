import os
import shutil

os.system("pyinstaller --onefile linux_install.py")
shutil.rmtree("./build")
os.rename("./dist/linux_install", "./linux_install")
shutil.rmtree("./dist")
os.remove("linux_install.spec")
