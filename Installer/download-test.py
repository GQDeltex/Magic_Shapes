import urllib2
 
url = 'https://github.com/GQDeltex/Magic_Shapes/raw/master/Magic_Shapes_postLudum.zip'
print "downloading with urllib2"
f = urllib2.urlopen(url)
data = f.read()
with open("test.txt", "wb") as code:
    code.write(data)
print "Finished!"