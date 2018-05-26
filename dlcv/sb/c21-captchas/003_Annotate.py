
# coding: utf-8

# In[1]:


from imutils import paths
import imutils
import cv2
import os


# In[2]:


INPUT = "downloads"
ANNOT = "dataset"


# In[3]:


imagePaths = list(paths.list_images(INPUT))
counts = {}


# In[15]:


# Loop over the image paths
for(i, imagePath) in enumerate(imagePaths):
    # Display an update to the user
    print("[INFO] processing image {}/{}".format(i + 1, len(imagePaths)))
    
    try:
        # Load the image and conver it to grapyscale then pad the image to ensure
        # digits caught only the border of the image and retained
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.copyMakeBorder(gray, 8, 8, 8 , 8, cv2.BORDER_REPLICATE)
        
        # Threshold the image to reveal the digits
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        
        # Find contours in the image, keeping only the four largest ones
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:4]
        
        # Loop over the contours
        for c in cnts:
            # Compute the bounding box for the contour then extract the digit
            (x, y, w, h) =cv2.boundingRect(c)
            roi = gray[y-5:y+h, x-5:x+w+5]
            
            # Display the characters
            cv2.imshow("ROI", imutils.resize(roi, width=28))
            key = cv2.waitKey(0)
            
            # If the ` key is pressed, then ignore the character
            if key == ord("`"):
                print("[INFO] ignoring character")
                continue
                
            # Grab the key that was pressed and contruct the path the output directory
            key = chr(key).upper()
            dirPath = os.path.sep.join([ANNOT, key])
            
            # If the output directory does not exist, create it 
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)
                
            # Write the labeled character to file
            count = counts.get(key, 1)
            p = os.path.sep.join([dirPath, "{}.png".format(
                str(count).zfill(6))])
            cv2.imwrite(p, roi)
            
            # Increment teh count for the current key
            counts[key] = count + 1
            
        # We are trying to control-c out of the script, so break from the loop (you
        # still need to press a key for the active window to trigger this)
    except KeyboardInterrupt:
        print("[INFO] manually leaving script")
        break
            
    # An unkown error has occured for this particular image
    #except:
     #   print("[INFO] skipping image...")