'''
George Skouroupathis
tags: pixels, pil, xor, qr code
'''

from PIL import Image, ImageDraw

BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

def draw_image(im1, im2, mode):
    # Assuming same image dimensions
    width = im1.size[0]
    height = im1.size[1]

    newImg = Image.new( 'RGBA', (width, height), 'white')
    newImgPixels = newImg.load()

    for x in range(width):
        for y in range(height):
            newImgPixels[x,y] = apply_filter_mode(mode, im1.getpixel((x,y)), im2.getpixel((x,y)))
    newImg.show()

def apply_filter_mode(mode, pixel1, pixel2):
    if mode == 'xor':
        if pixel1 != pixel2:
            return BLACK
        else:
            return WHITE
    if mode == 'and':
        if pixel1 == BLACK and pixel2 == BLACK:
            return BLACK
        else:
            return WHITE
    if mode == 'or':
        if pixel1 == BLACK or pixel2 == BLACK:
            return BLACK
        else:
            return WHITE

if __name__ == '__main__':
    im1 = Image.open('/Users/george/Downloads/QR1.png')
    im2 = Image.open('/Users/george/Downloads/QR2.png')

    draw_image(im1, im2, 'xor')

    dummyText = raw_input('Cool?')
