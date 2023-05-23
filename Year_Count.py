#-*- codeing = utf-8 -*-
#@Time: 2021/4/26 18:09
#@Author : Asus
#@File : Year_Count.py
#@Software : PyCharm
import pymysql.cursors
from matplotlib import pyplot as plt

connection = pymysql.connect(host="localhost", port=3306, user="root",passwd="123456", db="graduate_project")

try:
    cursor = connection.cursor()
    sql = "select date_format(PubTime, '%Y') as mont, count(*) as coun from input " \
          "where date_format(PubTime, '%Y') > '2012' " \
          "group by date_format(PubTime, '%Y') " \
          "order by mont;"
    cursor.execute(sql)
    result = cursor.fetchall()
    # print (result)
except Exception:
    print("发生错误")
cursor.close()
connection.close()

count = []
for data in result:
    Year = data[0]
    Count = data[1]
    count.append([Year,Count])
print(count)

# squares=count
# x=year
# plt.plot(x, squares)
# plt.savefig("Year_count.jpg")
# plt.show()



