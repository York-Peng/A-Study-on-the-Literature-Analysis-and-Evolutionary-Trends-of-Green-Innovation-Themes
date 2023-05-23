#-*- codeing = utf-8 -*-
#@Time: 2021/4/27 22:37
#@Author : Asus
#@File : textRank.py
#@Software : PyCharm
import random

import jieba
import seaborn as sns
from textrank4zh import TextRank4Keyword
from matplotlib import pyplot as plt
import pandas as pd
import pymysql.cursors

connection = pymysql.connect(host="localhost", port=3306, user="root",passwd="123456", db="graduate_project")

try:
    cursor = connection.cursor()
    sql = "select Keyword from input"
    cursor.execute(sql)
    datalist = []
    result = cursor.fetchall()
    for data in result:
        mid = data.__str__().strip('(').strip(')').strip("'").strip(',').strip("'").strip('').replace(';;', ' ')
        if mid[-1] == ';':
           res = mid.rstrip(';')
           split = res.split(';')
           datalist.append(split[0])
    # print (datalist)
except Exception:
    print("发生错误")
cursor.close()
connection.close()


cut = jieba.cut(''.join(datalist))
seed = ' '.join(cut)
# print(seed)

#匹配率最高的前10关键词
tr4w = TextRank4Keyword()
tr4w.analyze(text=seed, lower=True, window=2, pagerank_config={'alpha':0.85})
for item in  tr4w.get_keywords(10, word_min_len=2):
  print(item.word, item.weight)



