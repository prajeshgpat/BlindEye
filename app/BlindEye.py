import io
from gtts import gTTS
import os
from pygame import mixer
from google.cloud import vision
import time
import cv2
import numpy

# Instantiates a client
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

    #Text-to-Speech
    print('Labels:')
    for label in labels:
        img = cv2.imread(file_name)
        imgrs = cv2.resize(img,(400,400))
        image = cv2.imshow('LOOK',imgrs)
        tts = gTTS('This is a' + label.description, lang='en')
        a = tts.save(file_name + '.mp3')
        os.system("mpg321 " + file_name + ".mp3")
        print(label.description)
        mixer.init()
        mixer.music.load(file_name + '.mp3')
        mixer.music.play()
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        time.sleep(10)
        break

function('crosswalk.png')
##function('backpack.jpg')
##function('phone2.jpg')
##function('dog.jpg')




