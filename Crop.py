# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 22:17:59 2021

@author: Dipti
"""
import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt

origImg = img.imread("pic.jpg")
plt.imshow(origImg)
plt.show()


w, h = origImg.shape[:2]

print("Original Width : {}".format(w))
print(" Original Height : {}".format(h))


start_x = int(input("Enter start x: "))
start_y = int(input("Enter start y: "))
newWidth = int(input("Enter new width: "))
newHeight = int(input("Enter new height: "))

newImg = np.zeros([newWidth,newHeight])
print("Shape of new Img : {}".format(newImg.shape))


newImg = origImg[start_x : start_x + newWidth , start_y : start_y + newHeight]

plt.imshow(newImg)
plt.show()
