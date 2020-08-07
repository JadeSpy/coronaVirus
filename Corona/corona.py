from PIL import Image
import math
from random import seed
from random import random
from random import randint
import win32gui
import win32api
from win32api import GetSystemMetrics

dc = win32gui.GetDC(0)
red = win32api.RGB(255, 0, 0)

def makeVortex2(xInput, yInput, radius, usedSeed, layers):
	seed(usedSeed)
	lengthOfLayer = radius/layers
	colorListR = []
	colorListG = []
	colorListB = []
	for color in range (0, layers):
		colorListR.append(randint(0, 255))
		colorListG.append(randint(0, 255))
		colorListB.append(randint(0, 255))
	for x in range (round(xInput-radius), round(xInput+radius)):
		for y in range (round(yInput-radius), round(yInput+radius)):
			for layerCount in range (0, layers):
				if( math.sqrt(math.pow(abs(abs(x)-abs(xInput)),2)+math.pow(abs(abs(y)-abs(yInput)),2)) < lengthOfLayer*layerCount):
					color = win32api.RGB(colorListR[layerCount], colorListG[layerCount], colorListB[layerCount])
					try:
						win32gui.SetPixel(dc, x, y, color)
					except:
						pass
					#workWithImage[x,y] = (colorListR[layerCount], colorListG[layerCount], colorListB[layerCount])
					break
count = 0
while True:
	count+=1
	makeVortex2((GetSystemMetrics(0)*(randint(10, 90)/100)), (GetSystemMetrics(1)*(randint(10, 90)/100)), (randint(2, 25)/100)*GetSystemMetrics(1)/3, count, randint(5, 25))