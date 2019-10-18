from PIL import Image, ImageDraw, ImageFont
import io
import re
import base64
import random
# base64化された画像データを用意
data = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=="
# 頭のいらない部分を取り除いた上で、バイト列にエンコード
image_data_bytes = re.sub('^data:image/.+;base64,','',data).encode('utf-8')
# バイト列をbase64としてデコード
image_data = base64.b64decode(image_data_bytes)#返り値もバイト列
# ファイルとして開き、pillowのImageインスタンスにする

ynum = random.randint(1,22)
mnum = random.randint(1,16)
color1 = random.randint(0,255)
color2 = random.randint(0,255)
color3 = random.randint(0,255)
color4 = random.randint(0,255)
color5 = random.randint(0,255)
color6 = random.randint(0,255)
color7 = random.randint(0,255)
haikei = random.randint(0,17)


yuka = './img/yukari/' + str(ynum) + '.png'
maki = './img/maki/' + str(mnum) + '.png'

haikei2 = './img/' + str(haikei) + '.jpg'



im2 = Image.open(io.BytesIO(image_data))
pic = Image.open(yuka).copy().resize(size=(1280, 2380), resample=Image.ANTIALIAS)
pic2 = Image.open(maki).copy().resize(size=(1680, 2380), resample=Image.ANTIALIAS)
im = Image.open(haikei2).copy().resize(size=(1280, 720), resample=Image.ANTIALIAS)


icon = im.resize(size=(1280, 720), resample=Image.ANTIALIAS)
im.paste(pic, (-400, -50), pic)
im.paste(pic2, (200, -50), pic2)






draw = ImageDraw.Draw(im)
fnt = ImageFont.truetype('./TanukiMagic.ttf',150)
draw.text((70,500),"test",fill=(color2, color3, color4),font=fnt)
fnt = ImageFont.truetype('./TanukiMagic.ttf',149)
draw.text((69,500),"test",fill=(color5, color6, color7),font=fnt)


im.save("../test.png")
