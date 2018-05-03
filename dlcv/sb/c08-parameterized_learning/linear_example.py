import numpy as np 
import cv2

labels = ["dog", "cat", "panda"]
np.random.seed(1)


# Randomly initialize our weight matrix and bias vector, in  a *real* training and
# classification task. These parameters would be learned by our model but for the 
# sake of this example... let's use random values
W = np.random.randn(3, 3072)
b = np.random.randn(3)

# Load the imagea, resize and faltten it
orig =  cv2.imread("beagle.png")
image = cv2.resize(orig, (32, 32)).flatten()


scores = W.dot(image) + b

for (label, score) in zip(labels, scores):
    print("[INFO] {}: {:.2f}".format(label, score))

# draw the label with the highest score on the image as our pred
cv2.putText(orig, "Label: {}".format(labels[np.argmax(scores)]), (10, 30),
    cv2.FONT_HERSHEY_TRIPLEX, 0.9, (0, 255, 0), 2)

cv2.imshow("Image", orig)
cv2.waitKey(0)