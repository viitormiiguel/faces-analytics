
from pytube import YouTube
import os
import cv2, pafy
import numpy as np 
import os 
import math 
import csv
from moviepy.editor import *
import datetime

def downloadYouTube(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)


def downloadFrames():

    entries = os.listdir('./data/video/')

    for ent in entries:

        vidcap      = cv2.VideoCapture('./data/video/' + ent)
        
        clip        = VideoFileClip('./data/video/' + ent) 
        duration    = clip.duration    

        video_time = str(datetime.timedelta(seconds = int(duration)))

        n_frames    = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps         = int(vidcap.get(cv2.CAP_PROP_FPS))

        try:
            if not os.path.exists('./data/images/' + ent):
                os.makedirs('./data/images/' + ent)
        except OSError:
            print('Error: Creating directory of data')


        currentFrame = 0
        while(True):
            
            # Capture frame-by-frame
            ret, frame = vidcap.read()

            if not ret:
                break

            # Saves image of the current frame in jpg file
            name = './data/images/' + ent + '/frame_' + str(currentFrame) + '.jpg'
            # print ('Creating...' + name)
            cv2.imwrite(name, frame)

            # To stop duplicate images
            currentFrame += 1

        vidcap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":

    downloadYouTube('https://youtu.be/esfChb49_Rk', 'data/video/')

    downloadFrames()