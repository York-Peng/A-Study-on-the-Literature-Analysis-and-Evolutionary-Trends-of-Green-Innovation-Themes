#-*- codeing = utf-8 -*-
#@Time: 2021/4/9 12:19
#@Author : Asus
#@File : WordCloud.py
#@Software : PyCharm

import pymysql.cursors
from wordcloud import WordCloud
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import jieba

connection = pymysql.connect(host="localhost", port=3306, user="root",passwd="123456", db="graduate_project")

try:
    cursor = connection.cursor()
    sql = "select Keyword from input"
    cursor.execute(sql)
    datalist = []
    result = cursor.fetchall()
    for data in result:
        mid = data.__str__().strip('(').strip(')').strip("'").strip(',').strip("'").strip('').replace(';;', ';')
        if mid[-1] == ';':
           res = mid.rstrip(';')
        split = res.split(';')
        datalist.append(split[0])
    print (datalist)
except Exception:
    print("发生错误")
cursor.close()
connection.close()

# file = open('word.txt','w')
# for i in range(len(datalist)):
#     s = str(datalist[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
#     s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
#     file.write(s)
# file.close()
# print("保存文件成功")


# cut = jieba.cut(''.join(datalist))
# string = ' '.join(cut)
# # print(string)
#
# img = Image.open(r'./img/tree.jpg')           #打开遮罩图片
# img_arry = np.array(img)                                    #将图片装换为数组进行相应计算
# wc = WordCloud(
#     background_color='white',
#     mask = img_arry,
#     font_path="msyh.ttc"
# )
# wc.generate_from_text(string)
#
#
# fig = plt.figure(1)
# plt.imshow(wc)
# plt.axis('off')                                             #是否显示坐标轴
# plt.savefig(r'./img/word.jpg',dpi = 500)
#





