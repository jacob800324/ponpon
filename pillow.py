# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 10:53:53 2017

@author: jacob0324
"""

from PIL import Image
image = Image.open('C:\\Users\\jacob0324.WIN-SGGPL3SUTAK\\Desktop\\rose.jpg')

r, g, b = image.split()
convert_image = Image.merge("RGB" , (r, g, r))
convert_image.show() 










