import base64
from PIL import Image
import io
import cv2
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pandas as pd
model=load_model('sign_mnist_train.h5')

def solve1(img):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=cv2.resize(img,(28,28))
    img=img.reshape(28,28,1)
    img=img/255.0
    img=np.array([img])
    model=load_model('sign_mnist_train.h5')
    ch=(chr(ord('A')+np.argmax(model.predict(img))))
    print("abhiaps"+ch)
    return ch

    
def solve(imgstring):
    image = base64.b64decode(str(imgstring)) 
    imagePath = ("test.jpeg")      
    img = Image.open(io.BytesIO(image))
    img.save(imagePath, 'jpeg')
    imagefinal=cv2.imread("test.jpeg")
    return solve1(imagefinal)

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/solve")
def hello():
    img=str(request.args['image'])
    res=solve(img)
    return jsonify({'prediction':res})

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)