from PIL import Image
import os
import statistics
# link to github account: https://github.com/coparker/CST205Project1/edit/master/Project1.py
fp = input("Please enter the desired filepath: ")
pic = [Image.open(fp + file) for file in os.listdir(fp) if file.endswith(".png")] # list comp to add images to list
temp = Image.new('RGB', (pic[0].width, pic[0].height)) # will throw error is pic is empty (file path entry error?)
for (x, y) in [(x, y) for x in range(temp.width) for y in range(temp.height)]: # nested for loop in 1 line
	temp.putpixel((x, y), statistics.median([a.getpixel((x, y)) for a in pic])) # add the pixel data to the created image
temp.show()
