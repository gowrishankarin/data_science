import imutils
import cv2

def preprocess(image, width, height):
    # Grab the dimensions of the image then intialize the padding values
    (h, w) = image.shape[:2]
    
    # If the width is greater than the height then resize along the width
    if w > h:
        image = imutils.resize(image, width=width)
    
    # Otherwise the height is greater than the width so resize along the height
    else:
        image = imutils.resize(image, height=heights)
        
    # Determine the padding values for the width and height to obtain
    # target dimensions
    padW = int((width - image.shape[1]) / 2.0)
    padH = int((height - image.shape[0]) / 2.0)
    
    # Pad the image then apply one more resizing to handle any rounding issues
    image = cv2.copyMakeBorder(image, padH, padH, padW, padW, cv2.BORDER_REPLICATE)
    image = cv2.resize(image, (width, height))
    
    return image