import imutils
import cv2

class AspectAwarePreprocessor():
    def __init__(self, width, height, inter=cv2.INTER_AREA):
        self.width = width
        self.height = height
        self.inter = inter
        
    def preprocess(self, image):
        # Grab the dimensions of the image and then intialize the deltas to use when cropping
        (h, w) = image.shape[:2]
        dW = 0
        dH = 0
        
        # If the width is smaller than the height, then resize along the width (ie the smaller dimension)
        # and then update the deltas to crop the height to the deired dimension
        
        if(w < h):
            image = imutils.resize(image, width=self.width, inter=self.inter)
            dH = int((image.shape[0] - self.height) / 2.0)
            
        # Otherwise the height is smaller than the width so resize along the height
        # and then update the deltas crop along the width
        else:
            image = imutils.resize(image, height=self.height, inter=self.inter)
            dW = int((image.shape[1] - self.height) / 2.0)
            
        # Now that our images have been resized, we need to regrab the width
        # and height, followed by performning the crop
        
        (h, w) = image.shape[:2]
        image = image[dH:h - dH, dW:w - dW]
        
        # Finally resize the image to the provided spatial dimensions to 
        # ensure our output image is always a fixed size
        return cv2.resize(image, (self.width, self.height), interpolation=self.inter)