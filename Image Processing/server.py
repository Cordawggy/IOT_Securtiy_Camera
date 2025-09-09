import cv2 #Library for image processing
from flask import Flask, Response #Importing Flask

CamLink = "" #Need the cameras IP to insert as the link for now

app = Flask(__name__)

def generate_frames():

    cap = cv2.VideoCapture(CamLink) #Will open the video stream from the camera

