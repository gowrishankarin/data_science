
# coding: utf-8

# In[1]:


from keras.preprocessing.image import img_to_array
from keras.models import load_model
from imutils import contours
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2


# In[2]:


IMG_HELP_PATH = '/Users/shankar/dev/code/ds/studies/data_science/dlcv/sb/c07-first_image_classifier'
import os
import sys
sys.path.append(os.path.abspath(IMG_HELP_PATH))
from pyimagesearch.utils.captchahelper import preprocess
from pyimagesearch.nn.conv import LeNet


# In[3]:


INPUT = "downloads"
MODEL = "output/lenet.hdf5"

print("[INFO] loading pre-trained network...")
model = load_model(MODEL)


# In[4]:


imagePaths = list(paths.list_images(INPUT))
imagePaths = np.random.choice(imagePaths, size=(10,), replace=False)


# In[5]:


for imagePath in imagePaths:
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.copyMakeBorder(gray, 20, 20, 20, 20, cv2.BORDER_REPLICATE)
    
    thresh = cv2.threshold(gray, 0, 255, 
        cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    
    # Find contours
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:4]
    cnts = contours.sort_contours(cnts)[0]
    
    
    output = cv2.merge([gray] * 3)
    predictions = []
    
    for c in cnts:
        # Compute the bounding box for the contours and extract the digit
        (x, y, w, h) = cv2.boundingRect(c)
        roi = gray[y-5:y+h+5, x-5:x+w+5]
        
        # Preprocess the ROI and classify it then classify it
        roi = preprocess(roi, 28, 28)
        roi = np.expand_dims(img_to_array(roi), axis=0)
        pred = model.predict(roi).argmax(axis=1)[0] + 1
        predictions.append(str(pred))
        
        # Draw the predicion on the output image
        cv2.rectangle(output, (x-2, y-2), (x+w+4, y+h+4), (0, 255, 0), 1)
        cv2.putText(output, str(pred), (x-5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)
        
    # Show the output image
    print("[INFO] captcha: {}".format("".join(predictions)))
    cv2.imshow("Output", output)
    cv2.waitKey()

