#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 20:38:48 2022

@author: shayla
"""
import matplotlib.pyplot as plt
from skimage import data

#####################################################
img = data.cell()
plt.imshow(img)









































#####################################################
import skimage
shrper_contrast = skimage.exposure.rescale_intensity(img)
#####################################################
import numpy as np
import io
v_min, v_max = np.percentile(img, (0.2, 96.8))
better_contrast = skimage.exposure.rescale_intensity(img, in_range=(v_min, v_max))
plt.imshow(better_contrast)
imfile = io.BytesIO()
plt.imsave(imfile, better_contrast, format="png")
#####################################################
hrs = data.horse()
plt.imshow(hrs, cmap=plt.cm.gray)
#####################################################
hrs_size = np.shape(hrs)
#####################################################
import copy

hrs1 = copy.deepcopy(hrs)
#####################################################

im = data.brick()
plt.imshow(im, cmap=plt.cm.gray)

hrs_rescaled = skimage.transform.rescale(hrs, 0.4)
plt.imshow(hrs_rescaled, cmap=plt.cm.gray)

from skimage import data
from skimage import transform
from skimage import img_as_float
tform = transform.EuclideanTransform(rotation=np.pi / 4., translation = (180, -180))
tf_img = transform.warp(hrs, tform) 

plt.imshow(tf_img, cmap=plt.cm.gray)



from skimage import feature


#edges = feature.canny(im)
#plt.imshow(edges, cmap=plt.cm.gray)

#from scipy import ndimage
#fill_im = ndimage.binary_fill_holes(edges)
#plt.imshow(fill_im, cmap=plt.cm.gray)


