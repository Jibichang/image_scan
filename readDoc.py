from pytesseract import image_to_string
import pytesseract
from PIL import Image
import argparse
import cv2
import os

# image = cv2.cvtColor(cv2.imread("folder/image3.png"), cv2.COLOR_BGR2RGB)
image = cv2.imread("folder/image5.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# check to see if we should apply thresholding to preprocess the
# image
# if args["preprocess"] == "thresh":
# 	gray = cv2.threshold(gray, 0, 255,
# 		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
 
# make a check to see if median blurring should be done to remove
# noise
# elif args["preprocess"] == "blur":
# 	gray = cv2.medianBlur(gray, 3)
 
# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
# filename = "{}.png".format(os.getpid())

fileImage = "folder/resultImage6.jpg"
cv2.imwrite(fileImage, gray)


# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file

img = Image.open(fileImage)
text = pytesseract.image_to_string(img, config='')
os.remove(fileImage)
print(text)
 
# show the output images
cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)

