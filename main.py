from PIL import Image, ImageDraw, ImageFont
import codecs
with codecs.open("test.txt",'r',encoding='utf8') as f:
    text = f.read()
    image = Image.open('image.png')
    font_type = ImageFont.truetype("Kinnari.ttf",18)
    draw = ImageDraw.Draw(image)
    draw.text(xy=(1,4),text=text,fill=(255,0,255),font=font_type)
    image.show()
# import cv2
# import numpy as np
# img = np.zeros((36, 192, 3), dtype=np.uint8)
# cv2.imwrite('image.png', img)
# image = Image.open('image.png')
# font_type = ImageFont.truetype("OpenSans-Bold.ttf",18)
# draw = ImageDraw.Draw(image)
# draw.text(xy=(1,4),text="HELLO",fill=(255,69,0),font=font_type)
# image.show()

# print .read() 