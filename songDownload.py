import subprocess
import sys
import time
import ast

url = sys.argv[1]
url = str(url).split("&")[0]


class Downloader():

    def __init__(self, url):
        self.url = url

    def convert(self, x):
        subprocess.call("ffmpeg -i " + x + ".mp4 -c:a copy -vn -sn " + x + ".m4a", shell=True)
        new = str(x).replace("_", "\ ")
        subprocess.call("mv " + str(x) + ".m4a " + new + ".m4a", shell=True)
        subprocess.call("rm " + x + ".mp4", shell=True)

    def download(self, name):
        subprocess.call("youtube-dl " + self.url + " -f mp4 -o " + name + ".mp4", shell=True)
        print "----------------------"
        self.convert(name)

    def getSongName(self):
        af = subprocess.Popen("youtube-dl -f mp4 --get-filename -o '%(title)s.%(ext)s' " +  self.url + " --restrict-filenames", stdout=subprocess.PIPE, shell=True)
        self.download(af.communicate()[0].replace("\n", "").replace(".mp4", ""))
            
Downloader(url).getSongName()
