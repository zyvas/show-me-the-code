from PIL import Image, ImageDraw,ImageFont

url = 'img.jpg'
txt = '1'
fontcolor = (255,0,0)

font = ImageFont.truetype('arial.ttf',30)
img = Image.open(url)
x,y = img.size

draw = ImageDraw.Draw(img)

draw.text((x-40,20),"1",font=font,fill=fontcolor)
del draw

img.save('img_save.jpg')

