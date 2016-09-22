from PIL import Image
import sys

# Following only runs once to get decode_dict
###

imd = Image.open('noise_decode.png')

imageW = imd.size[0]
imageH = imd.size[1]

prev = None
for x in range(imageW):
	xy = (x,0)
	rgb = imd.getpixel(xy)
	if rgb != prev:
		print rgb,
		prev = rgb

###
###

decode_dict = {(0,0,0): '1', (255, 255, 255): '2', (127, 127, 127): '3',
	(136, 0, 21):'4', (237, 28, 36): '5', (255, 127, 39): '6', (255, 242, 0): '7',
	(34, 177, 76): '8', (0, 162, 232): '9', (63, 72, 204): '0', (163, 73, 164):'A',
	(200, 191, 231): 'B', (112, 146, 190): 'C', (153, 217, 234): 'D', (181, 230, 29): 'E', (255, 174, 201): 'F'} 
im = Image.open('noise.png')

imageW = im.size[0]
imageH = im.size[1]
print 'imageW', imageW
print 'imageH', imageH

decoded = ''
for y in range(imageH):
	print
	for x in range(imageW):
		offset = y*imageW + x
		xy = (x,y)
		rgb = im.getpixel(xy)
		sys.stdout.write(decode_dict[rgb])
		decoded += decode_dict[rgb]

print decoded.decode("hex")
