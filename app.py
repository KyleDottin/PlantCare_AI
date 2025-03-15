import os
from flask import Flask, redirect, render_template, request
from PIL import Image
import torchvision.transforms.functional as TF
import CNN
import numpy as np
import torch
import pandas as pd
import socket


disease_info = pd.read_csv('disease_info.csv' , encoding='cp1252')

model = CNN.CNN(39)    
model.load_state_dict(torch.load("plant_disease_model_1_latest.pt"))
model.eval()

def prediction(image_path):
    image = Image.open(image_path)
    image = image.resize((224, 224))
    input_data = TF.to_tensor(image)
    input_data = input_data.view((-1, 3, 224, 224))
    output = model(input_data)
    output = output.detach().numpy()
    index = np.argmax(output)
    return index


app = Flask(__name__)

@app.route('/')
def index():
    file_path = "./static/image_test.jpg"
    pred = prediction(file_path)
    title = disease_info['disease_name'][pred]
    description =disease_info['description'][pred]
    prevent = disease_info['Possible Steps'][pred]
    image_url = disease_info['image_url'][pred]
    return render_template('index.html', title = title, desc = description, prevent = prevent, image_url = image_url , pred = pred)

@app.route('/data')
def data():
    file_path = "image_test.jpg"
    pred = prediction(file_path)
    title = disease_info['disease_name'][pred]
    description =disease_info['description'][pred]
    prevent = disease_info['Possible Steps'][pred]
    image_url = disease_info['image_url'][pred]
    return {"title":title, "desc": description, "prevent": prevent, "image_url":image_url , "pred":pred}

if __name__ == '__main__':
    local_ip=socket.gethostbyname(socket.gethostname())
    print(f"server accessible on http://{local_ip}:5000")
    app.run(debug=False,  host='0.0.0.0', port=5000,use_reloader=False)
