import os

def listDir(dir):
    for files in os.listdir(dir):
        print(files)