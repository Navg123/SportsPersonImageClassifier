import numpy as np
import cv2
import matplotlib
from matplotlib import pyplot as plt
#%matplotlib inline
img=cv2.imread('./test_images/sharapova1.jpg')
print(img.shape)
print(plt.imshow(img))

