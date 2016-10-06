import os
import shutil
import zipfile
import time

Internet_adress = "https://github.com/GQDeltex/Magic_Shapes/raw/master/Magic_Shapes_postLudum.zip"
install_location = "./Magic_Shapes/"
dir_location = "./"

error = False

def createShortcut(path, target='', wDir='', icon=''):
    ext =path[-3:]
    if ext == 'url':
        shortcut = file(path, 'w')
        shortcut.write('[InternetShortcut]\n')
        shortcut.write('URL=%s' % target)
        shortcut.close()
    else:
        shell = Dispath('WScript.Shell')
        shortcut = shell.CeateShortCut(path)
        shortcut.TargetPath = targetshortcut.WorkingDirectory = wDir
        if icon == '':
            pass
        else:
            shortcut.IconLocation = icon
        shortcut.save()

def unzip(target_file, output_file):
    fh = open(target_file, 'rb')
    z = zipfile.ZipFile(fh)
    for name in z.namelist():
        z.extract(name, output_file)
    fh.close()

def copy(src, dst):
    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
    shutil.copytree(src, dst)

def download(down_url, down_url_num="https://github.com/GQDeltex/Magic_Shapes/raw/master/Version.txt"):
    os.sytsem('wget -q ' + down_url_num)
    verf = open("Version.txt", "r")
    version = verf.read()
    version = float(version)
    verf.close()
    os.system('wget -N ' + down_url)

if __name__ == '__main__':
    print "Downloading"
    download(Internet_adress)
    print "Unzipping"
    unzip('Magic_Shapes_postLudum.zip', './')
    print "Finished!"
