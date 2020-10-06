from PIL import Image
from io import BytesIO

import numpy as np
from numpy.lib.type_check import imag
import tensorflow as tf
from tensorflow.keras.applications.imagenet_utils import decode_predictions

input_shape = (224, 224)

def load_model():
    model = tf.keras.applications.MobileNetV2(weights="imagenet")
    print("Model Loaded")
    return model

model = load_model()

def read_image(image_encoded):
    pil_image = Image.open(BytesIO(image_encoded))
    return pil_image

def preprocess(image: Image.Image):
    image = image.resize(input_shape)
    image = np.asfarray(image)
    image = image / 255.0
    
    image = np.expand_dims(image , 0)
    
    return image

def predict(image: np.ndarray):
    predictions = model.predict(image)
    
    result = decode_predictions(model.predict(image), 2)[0]
    
    response = []
    for i, res in enumerate(result):
        response = {}
        response['class'] = res[1]
        response['confidence'] = f'{res[2] * 100:0.2f}'
        
        response.append(resp)
        
    return response
    