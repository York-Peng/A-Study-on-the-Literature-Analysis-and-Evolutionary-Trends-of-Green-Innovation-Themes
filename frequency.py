#-*- codeing = utf-8 -*-
#@Time: 2021/4/18 23:37
#@Author : Asus
#@File : frequency.py
#@Software : PyCharm


import pymysql
import jieba
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


mpl.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']  # 汉字字体,优先使用楷体，如果找不到楷体，则使用黑体
mpl.rcParams['font.size'] = 12  # 字体大小
mpl.rcParams['axes.unicode_minus'] = False  # 正常显示负号


connection = pymysql.connect(host="localhost", port=3306, user="root",passwd="123456", db="graduate_project")

try:
    cursor = connection.cursor()
    sql = "select Keyword from input"
    cursor.execute(sql)
    datalist = []
    result = cursor.fetchall()
    for data in result:
    #     mid = data.__str__().strip('(').strip(')').strip("'").strip(',').strip("'").strip('').replace(';;', ';')
    #     if mid[-1] == ';':
    #        res = mid.rstrip(';')
    #     split = res.split(';')
        datalist.append(data)
    # print (datalist)
except Exception:
    print("发生错误")
cursor.close()
connection.close()

text = []
# file = open('word.txt','w')
for i in range(len(datalist)):
    s = str(datalist[i]).replace('(','').replace(')','')#去除[],这两行按数据不同，可以选择
    s = s.replace("'",'').replace(';','').replace(',','')   #去除单引号，逗号，每行末尾追加换行符(+'\n')
    text.append(s)
#     file.write(s)
# file.close()
# print(text)


#装在停用词
stoplist = open('../cn_stopwords.txt', 'r', encoding="utf-8").readlines()
stoplist = set(w.strip() for w in stoplist)


#分词，去停用词
texts = []
for d in text:
    for w in list(jieba.cut(d,cut_all=False)):
        if len(w)>1 and w not in stoplist:
            texts.append(w)
# print(texts)
df = pd.DataFrame(texts, columns=['word'])
fre = df.groupby(['word']).size()
frelist = fre.sort_values(ascending=False)
frelist = frelist[:10]
# print(frelist)
word = ['绿色','创新','发展','技术创新','环境','企业','管理','技术','生态','产业']
wordlist = []
for i in range(len(frelist)):
    wordlist.append([word[i],frelist[i]])
print(wordlist)
# frelist.plot.bar()
# plt.title("摘要词频TOP10")
# plt.xticks(rotation = 360)
# plt.savefig("word_frequence.jpg")
# plt.show()
# print(frelist)
