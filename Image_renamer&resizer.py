"""
@author: Ak
"""
#ディレクトリ内の画像のリネーム、リサイズを一括で行う　(ディレクトリ内に同じ名前あるとエラーが起こります)


import os
import re
from PIL import Image
a = 1


#os.getcwd()  #現在のカレントディレクトリ取得
#os.path.exists("anaconda3\\sakura\\")
#os.chdir("C:\\Users\\Aki\\Anaconda3\\sakura")  #ディレクトリの移動



#image_1,image_2 等にディレクトリ内の画像の名前を一括変換する
files = os.listdir()
for file in files:
    jpg = re.compile("jpg")
    if jpg.search(file):
        os.rename(file, "image_%d.jpg" %(a))
        a+=1

    else:
        pass

サイズを75×75に一括リサイズ
files = os.listdir()
for file in files:

    if  file.find('.jpg') > 0 :

        img = Image.open(file)
        img = img.resize((75,75))
        img.save(file)

    else:
        pass

#os.chdir("C:\\Users\\Ak\\Anaconda3\\")
