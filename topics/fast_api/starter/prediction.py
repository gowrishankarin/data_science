from PIL import Image
from io import BytesIO

import numpy as np
from numpy.lib.type_check import imag
import tensorflow as tf
from tensorflow.keras.applications.imagenet_utils import decode_predictions

input_shape = (224, 224)

model = None

def load_model():
    global model;
    if(model is None):
        model = tf.keras.applications.MobileNetV2(weights="imagenet")
        print("Model Loaded")
    return model



def read_image(file) -> Image.Image:
    print("Reading the image")
    pil_image = Image.open(BytesIO(file))
    return pil_image

def preprocess(image: Image.Image):
    print("Preprocessing the Image")
    image = image.resize(input_shape)
    image = np.asarray(image)[..., :3]
    
    
    image = np.expand_dims(image , 0)
    image = image / 127.5 - 1.0
    
    return image

def predict(image: Image.Image):
    
    model = load_model()
    
    image = preprocess(image)

    predictions = model.predict(image)
    
    results = decode_predictions(predictions, 2)[0]
    
    response = {}
    for i, res in enumerate(results):
        result = {}
        result['class'] = res[1]
        result['confidence'] = f'{res[2] * 100:0.2f}'
        
        response[i] = result
        
    print(response)   
    return response
    