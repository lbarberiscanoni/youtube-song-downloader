import subprocess
import sys
import time
import ast

url = sys.argv[1]

def convert(x):
    subprocess.call("ffmpeg -i " + x + ".mp4 -c:a copy -vn -sn " + x + ".m4a", shell=True)
    new = str(x).replace("_", "\ ")
    subprocess.call("mv " + str(x) + ".m4a " + new + ".m4a", shell=True)
    subprocess.call("rm " + x + ".mp4", shell=True)

def download(a, b):
    subprocess.call("youtube-dl " + a + " -f mp4 -o " + b + ".mp4", shell=True)
    print "----------------------"
    convert(b)

def getSongName(a):
    af = subprocess.Popen("youtube-dl -f mp4 --get-filename -o '%(title)s.%(ext)s' " +  a + " --restrict-filenames", stdout=subprocess.PIPE, shell=True)
    download(url, af.communicate()[0].replace("\n", "").replace(".mp4", ""))
            
getSongName(url)
