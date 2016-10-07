import os
import shutil
import zipfile
import time
import shutil

Internet_adress = "https://github.com/GQDeltex/Magic_Shapes/raw/master/Magic_Shapes_postLudum.zip"
dir_location = "./Magic_Shapes_postLudum"

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

def download(down_url, verify=True, down_url_num="https://github.com/GQDeltex/Magic_Shapes/raw/master/Version.txt"):
    os.system('wget -q ' + down_url_num)
    verf = open("./Version.txt", "r")
    version = verf.read()
    version = float(version)
    verf.close()
    if verify:
        if os.path.isdir(dir_location):
            chf = open((dir_location + '/Version.txt'))
            check = chf.read()
            check = float(check)
            chf.close()
            print "Your current Version: " + str(check)
        else:
            check = 0.0
    else:
        check = 0.0
    if not version == check:
        print "Downloading newer Version" + str(version)
        os.system('wget ' + down_url)
        print "Unzipping"
        unzip('./Magic_Shapes_postLudum.zip', dir_location)
        print "Tidying up"
        os.rename('./Version.txt', (dir_location + '/Version.txt'))
        os.remove('./Magic_Shapes_postLudum.zip')
    else:
        os.remove("./Version.txt")
        print "Already on the newest version"

def main():
    print "Welcome to the Magic_Shapes Installer!"
    print ""
    if os.path.isdir(dir_location):
        print "You have two options:"
        answer = raw_input("1. Reinstalling 2. Uninstalling        [1/2]")
        if answer == '1':
            shutil.rmtree(dir_location)
            download(Internet_adress, False)
            #os.system('cd ' + dir_location + ' && python Magic_Shapes.py')
        elif answer == '2':
            shutil.rmtree(dir_location)
    else:
        print "Do you want to install now?"
        answer = raw_input("y/n \n")
        if answer == 'y':
            download(Internet_adress)
            #os.system('cd ' + dir_location + ' && python Magic_Shapes.py')
        else:
            print "Aborting"


if __name__ == '__main__':
    main()
    #download(Internet_adress)
