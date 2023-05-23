# -*- codeing = utf-8 -*-
# @Time: 2021/4/13 9:28
# @Author : Asus
# @File : TF-IDF.py
# @Software : PyCharm

import pymysql.cursors
import jieba.analyse
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from gensim.corpora.dictionary import Dictionary
import numpy as np

connection = pymysql.connect(host="localhost", port=3306, user="root", passwd="123456", db="graduate_project")

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

# 装在停用词表
stoplist = open("../cn_stopwords.txt", 'r', encoding="utf-8").readlines()
stoplist = set(w.strip() for w in stoplist)

# f分词，去停用词
texts = []
for d in datalist:
    doc = []
    for w in list(jieba.cut(d, cut_all=False)):
        if len(w) > 1 and w not in stoplist:
            doc.append(w)
    texts.append(doc)
# 特征选择：至少在texts中出现10次，而且所在文档数/总文档数<=1，前10个作文代表关键词
dictionary = Dictionary(texts)
dictionary.filter_extremes(no_below=10, no_above=1.0, keep_n=10)
d = dict(dictionary.items())
docwords = set(d.values())
# print("维度词汇是：",docwords)


connection = pymysql.connect(host="localhost", port=3306, user="root", passwd="123456", db="graduate_project")
cursor = connection.cursor()
a = '创新 求实 打造绿色医院文化'
cursor.execute("select Summary from input where Title = %s", (a))
summary = []
result = cursor.fetchall()
for data in result:
    mid = data.__str__().strip('(').strip(')').strip("'").strip(',').strip("'").strip('')
    summary.append(mid)
cursor.close()
connection.close()
summary = jieba.cut(
    summary.__str__().replace('[', '').replace(']', '').replace(',', '').replace('。', '').replace("'", ''))

list = []
for i in summary:
    if len(w) > 1 and w not in stoplist:
        list.append(i)

docword = []
for a in d.values():
    docword.append(a)
# print(docword)



corpus = []
for text in list:
    d = ""
    for w in text:
        if w in docwords:
            d = d + w + " "
    corpus.append(d)
# print(corpus)

result = []
# 计算文档中每个维度词汇的TF-IDF值
vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(corpus)
words = vectorizer.get_feature_names()
for i in range(len(corpus)):
    for j in range(len(words)):
        print(words[j])
        print(tfidf[i,j])


    # word_list = []
    # for i in range(len(b)):
    #     word_list.append()








# for i in range(len(corpus)):
#     for j in range(len(words)):
#         if np.any(tfidf[i,j] == 1):
#             result.append([words[j],tfidf[i,j]])
# print(result)


# cut = jieba.cut(''.join(datalist))
# seed = ' '.join(cut)
# # print(seed)

# IDF = jieba.analyse.extract_tags(seed, topK=15, withWeight=True, allowPOS=())
# print(IDF)
