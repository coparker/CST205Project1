from PIL import Image
import os
import statistics
fp = "C:/Users/Cody/Downloads/Project1Images/" # could make user input filepath
pic = [Image.open(fp + file) for file in os.listdir(fp)] # list comp to add images to list
temp = Image.new('RGB', (pic[0].width, pic[0].height))
for x in range(temp.width): # I want to make my nested for loop 1 line
	for y in range(temp.height): # using an itertools function
		list = [a.getpixel((x, y)) for a in pic] # adding ixel data to a list using list comp
		temp.putpixel((x, y), statistics.median(list)) # add the pixel data to the created image
temp.show()
