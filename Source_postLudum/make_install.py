import os
import shutil

os.system("pyinstaller --onefile Magic_Shapes.py")
shutil.copytree("./Game-Files", "./dist/Game-Files")
shutil.rmtree("./build")
os.remove("Magic_Shapes.spec")
