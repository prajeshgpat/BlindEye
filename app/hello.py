from flask import Flask, render_template
import io
from gtts import gTTS
import os
from pygame import mixer
from google.cloud import vision
import time
import cv2
import numpy


app = Flask(__name__, template_folder='template')  # still relative to module
# webcode = open('webcode.html').read() - not needed


vision_client = vision.Client('hacknyu-blind-vision')

def function(file_name):
    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        file_name) #<<<------the path

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
        image = vision_client.image(content=content)

    # Performs label detection on the image file
    labels = image.detect_labels()

    img = cv2.imread(file_name)
    imgrs = cv2.resize(img,(400,400))
    image = cv2.imshow('LOOK',imgrs)
    tts = gTTS('This is a' + label.description, lang='en')
    a = tts.save(file_name + '.mp3')
    os.system("mpg321 " + file_name + ".mp3")
    #print(label.description)
    mixer.init()
    mixer.music.load(file_name + '.mp3')
    mixer.music.play()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    time.sleep(10)
    return label.description
   

    #Text-to-Speech
    #print('Labels:')
##    for label in labels:
##        img = cv2.imread(file_name)
##        imgrs = cv2.resize(img,(400,400))
##        image = cv2.imshow('LOOK',imgrs)
##        tts = gTTS('This is a' + label.description, lang='en')
##        a = tts.save(file_name + '.mp3')
##        os.system("mpg321 " + file_name + ".mp3")
##        #print(label.description)
##        mixer.init()
##        mixer.music.load(file_name + '.mp3')
##        mixer.music.play()
##        cv2.waitKey(0)
##        cv2.destroyAllWindows()
##        time.sleep(10)
##        break

    
@app.route('/')
def home():
    # Instantiates a client

    result = function('crosswalk.png')    
    return render_template('results.html', result=result)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)
