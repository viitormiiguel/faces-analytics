
from unicodedata import name
import numpy as np 
import os 
from os import path
import subprocess
import shutil

def createFileVideo():

    entries = os.listdir('./data/video/')

    for ent in entries:

        try:
            if not os.path.exists('./output/' + ent):
                os.makedirs('./output/' + ent)
        except OSError:
            print('Error: Creating directory of data')

        exec1 = path + 'data\\video\\' + ent
        exec2 = path + 'output\\' + ent

        comando = ' -f ' + '"' +  exec1 + '"'

        os.system('"C:\\OpenFace\\FeatureExtraction.exe' + comando + ' -out_dir ' + exec2 + '"')


if __name__ == '__main__':

    # mudar path
    path = "D:\\PythonProjects\\faces-analytics\\"

    createFileVideo()