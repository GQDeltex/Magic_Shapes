import os
import shutil
import zipfile
import time
import shutil

filename = "Magic_Shapes_linux_postLudum.zip"
Internet_adress = ("https://github.com/GQDeltex/Magic_Shapes/raw/master/" + filename)
dir_location = ("./Magic_Shapes")
unzip_location  = "./"
global update
global version

def createShortcut(here, there):
    os.system("ln -s " + str(here) + " " + str(there))

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

def getVersion(down_url_num="https://github.com/GQDeltex/Magic_Shapes/raw/master/Version.txt"):
    os.system('wget -q ' + down_url_num)
    verf = open("./Version.txt", "r")
    version = verf.read()
    version = float(version)
    verf.close()
    if os.path.isdir(dir_location):
        chf = open((dir_location + '/Version.txt'))
        check = chf.read()
        check = float(check)
        chf.close()
        print "Your current Version: " + str(check)
    else:
        check = 0.0
    if check == version:
        update = False
        return False, version
    else:
        update = True
        return True, version

def download(down_url):
    if update == True:
        print "Downloading newer Version" + str(version)
        os.system('wget ' + down_url)
        print "Unzipping"
        unzip(filename, dir_location)
        print "Tidying up"
        os.rename('./Version.txt', (dir_location + '/Version.txt'))
        os.remove(filename)
    else:
        print "Already on the newest version"

def main():
    global update
    global version
    update = False
    version = 0.0
    getVersion()
    print "Welcome to the Magic_Shapes Installer!"
    print ""
    if os.path.isdir(dir_location) and not update:
        print "You have two options:"
        answer = raw_input("1. Reinstalling 2. Uninstalling        [1/2]")
        if answer == '1':
            version = 0.0
            update = True
            shutil.rmtree(dir_location)
            download(Internet_adress)
            os.system("cd Magic_Shapes && sudo chmod +x Magic_Shapes && ./Magic_Shapes")
        elif answer == '2':
            shutil.rmtree(dir_location)
    elif os.path.isdir(dir_location) and update:
        print "Update for Magic_Shapes to Version " + str(version) + " available. Do you want to update? [y/n]"
        answer = raw_input("")
        if answer == 'y':
            shutil.rmtree(dir_location)
            download(Internet_adress)
            os.system("cd Magic_Shapes && sudo chmod +x Magic_Shapes && ./Magic_Shapes")
    else:
        print "Do you want to install now?"
        answer = raw_input("y/n \n")
        if answer == 'y':
            download(Internet_adress)
            print "Installing dependecies"
            try:
                os.system('sudo apt-get install python python-pygame libsdl1.2-dev')
            except:
                print "Couldn't install dependecies!"
                print "The Game may not work properly!"
            os.system("cd Magic_Shapes && sudo chmod +x Magic_Shapes && ./Magic_Shapes")
        else:
            print "Aborting"


if __name__ == '__main__':
    main()
    #download(Internet_adress)
