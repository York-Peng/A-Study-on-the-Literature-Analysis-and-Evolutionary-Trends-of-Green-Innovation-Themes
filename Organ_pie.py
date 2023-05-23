#-*- codeing = utf-8 -*-
#@Time: 2021/4/28 16:08
#@Author : Asus
#@File : Organ_pie.py
#@Software : PyCharm
import pymysql
import matplotlib.pyplot as plt
import matplotlib as mpl

connection = pymysql.connect(host="localhost", port=3306, user="root", passwd="123456", db="graduate_project")
cursor = connection.cursor()
sql = "select Source,count(*) as count from input GROUP BY Source ORDER BY count DESC LIMIT 15"
cursor.execute(sql)
result = cursor.fetchall()
Source = []
count = []
for data in result:
    mid = data.__str__().replace(',', '').replace(';', '').replace("'", '').replace('(', '').replace(')', '').split(
        ' ')
    Source.append(mid[0])
    count.append(mid[1])
print(Source)

mpl.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']  # 汉字字体,优先使用楷体，如果找不到楷体，则使用黑体
mpl.rcParams['font.size'] = 11  # 字体大小
mpl.rcParams['axes.unicode_minus'] = False  # 正常显示负号

fig = plt.figure()
wedges, texts, autotexts = plt.pie(count,
                                   labels=Source,
                                   autopct='%1.2f%%')
plt.title("文献来源统计TOP15")
# plt.legend(wedges,Source,
#           fontsize = 7,
#           title = '机构列表',
#           loc="center left",
#           bbox_to_anchor=(1.0, 0.2, 0.5, 0.8))

plt.setp(autotexts,weight="bold",size=10)
plt.setp(texts, size=10)
plt.savefig("PieChart.jpg")
plt.show()


