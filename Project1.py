from PIL import Image
import os
import statistics
# link to github account: https://github.com/coparker/CST205Project1/edit/master/Project1.py
fp = "C:/Users/Cody/Downloads/Project1Images/" # could make user input filepath
pic = [Image.open(fp + file) for file in os.listdir(fp)] # list comp to add images to list
temp = Image.new('RGB', (pic[0].width, pic[0].height))
for (x, y) in [(x, y) for x in range(temp.width) for y in range(temp.height)]: # nested for loop in 1 line
	list = [a.getpixel((x, y)) for a in pic] # adding ixel data to a list using list comp
	temp.putpixel((x, y), statistics.median(list)) # add the pixel data to the created image
temp.show()
