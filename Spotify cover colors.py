#Spotify cover colors
from PIL import Image
import numpy as np
import operator
import pymeanshift as pms
from matplotlib import pyplot as plt

height = 0 
width = 0
freq = {}


def meanShiftFilter(original_image):
    #We need to homogenize tonality of the image to get the most repeated colors. 
    #If we dont do that we get tons of diferent pixels that have minimal differences in their RGB and
    #we can't consider them as the same color, resulting an error to our project.

    (segmented_image, labels_image, number_regions) = pms.segment(original_image, spatial_radius=6, 
                                                              range_radius=4.5, min_density=50)
    img = Image.fromarray(segmented_image)
    return img    


def storePixelsCol(pix):

    for i in range(0,width-1):
        for j in range(0,height-1):
            if pix[i,j] not in freq: 
                freq[pix[i,j]] = 1
            else:
                freq[pix[i,j]] += 1 
              

def showValues():
    value = max(freq.items(), key=operator.itemgetter(1))[0]  #Gets the key with maximum value
    freq.pop(value)
    secval = max(freq.items(), key=operator.itemgetter(1))[0]
    print('(RGB) Primary color: '+str(value)+'Secondary color: '+str(secval))

if __name__ == "__main__":

    original = Image.open("images/cover.jpg")
    original.show()
    img = meanShiftFilter(original)
    img.show()
    pix = img.load()
    width = img.size[0]
    height = img.size[1]
    storePixelsCol(pix)
    showValues()
     