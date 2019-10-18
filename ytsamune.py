#-*- coding: utf8 -*-
import sys
import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
import io
import re
import base64
import random
import tkinter.messagebox as tkm

root = tk.Tk()

# ウインドウのタイトルを定義する
root.title(u'samune.auto.maker')

# ここでウインドウサイズを定義する
root.geometry('400x300')



# ボタンが押されたら呼び出される関数
def Entry(event):
    Entry1_value = Entry1.get()
    Entry1_value2 = Entry1.get()


    # base64化された画像データを用意
    # 頭のいらない部分を取り除いた上で、バイト列にエンコード
    # バイト列をbase64としてデコード
    # ファイルとして開き、pillowのImageインスタンスにする
    # Entryの中身をすべて削除します
    ynum = random.randint(1,22)
    mnum = random.randint(1,16)
    color2 = random.randint(0,255)
    color3 = random.randint(0,255)
    color4 = random.randint(0,255)
    color5 = random.randint(0,255)
    color6 = random.randint(0,255)
    haikei = random.randint(0,17)


    yuka = './img/yukari/' + str(ynum) + '.png'
    maki = './img/maki/' + str(mnum) + '.png'

    haikei2 = './img/' + str(haikei) + '.jpg'

    pic = Image.open(yuka).copy().resize(size=(1280, 2380), resample=Image.ANTIALIAS)
    pic2 = Image.open(maki).copy().resize(size=(1680, 2380), resample=Image.ANTIALIAS)
    im = Image.open(haikei2).copy().resize(size=(1280, 720), resample=Image.ANTIALIAS)


    fntsize = ftnhenkankansu(mozisuu)
    fntsize2 = fntsize - 5


    im.paste(pic, (-400, -50), pic)
    im.paste(pic2, (200, -50), pic2)

    draw = ImageDraw.Draw(im)
    fnt = ImageFont.truetype('./CP and U-Fo.ttf',fntsize)
    draw.text((50,500),Entry1_value,fill=(color2, color3, color4),font=fnt)
    fnt = ImageFont.truetype('./CP and U-Fo.ttf',fntsize2)
    draw.text((49,500),Entry1_value2,fill=(color5, color6, 0),font=fnt)
    im.save("../test.png")

# ラベルを使って文字を画面上に出す
Static1 = tk.Label(text=u'▼　Entryだぞ！　▼')
Static1.pack()

# Entryを出現させる
Entry1 = tk.Entry(width=50)                   # widthプロパティで大きさを変える
Entry1.insert(tk.END, u'挿入する文字')        # 最初から文字を入れておく
Entry1.pack()

# Buttonを設置してみる
Button1 = tk.Button(text=u'実行ボタン', width=50)
Button1.bind("<Button-1>", Entry)        # ボタンが押されたときに実行される関数をバインドします
Button1.pack()


mozisuu = len(Entry1.get())


# ラベルを使って文字を画面上に出す
Static2 = tk.Label(root, text = mozisuu)
Static2.pack()



def ftnhenkankansu(mozisuu):
    if mozisuu <= 6:
        amari = mozisuu - 6
        fsaize = amari * 33
        fskai = 200 - fsaize
        return(fskai)
    else:
        amari = mozisuu - 6
        fskai = 200 + (amari * 33)
        return(fskai)






root.mainloop()

