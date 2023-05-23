#-*- codeing = utf-8 -*-
#@Time: 2021/4/26 20:45
#@Author : Asus
#@File : app.py
#@Software : PyCharm
import pymysql.cursors
from flask import Flask,render_template

#创建应用程序
app = Flask(__name__)


#处理发送过来的请求
# @app.route("/")     #访问时默认执行函数
# def index():
#     return render_template("demo1.html")

#主页
@app.route("/")     #访问时默认执行函数
def index():
    return render_template("index.html")

@app.route("/index")
def home():
    return index()


#图表页面
@app.route("/data_view")
def data_view():
    connection = pymysql.connect(host="localhost", port=3306, user="root", passwd="123456", db="graduate_project")
    cursor = connection.cursor()
    sql = "select date_format(PubTime, '%Y') as mont, count(*) as coun from input " \
          "where date_format(PubTime, '%Y') > '2012' " \
          "group by date_format(PubTime, '%Y') " \
          "order by mont;"
    cursor.execute(sql)
    result = cursor.fetchall()
    # print (result)
    cursor.close()
    connection.close()
    year = []
    count = []
    for data in result:
        Year = data[0]
        Count = data[1]
        year.append(Year)
        count.append(Count)
    # print(year)

    return render_template("data_view.html",year = year,count = count)

#地图页面
@app.route("/map_view")
def map_view():
    return render_template("map_view.html")


#数据挖掘页面
@app.route("/dig_view")
def dig_view():
    return render_template("dig_view.html")

#地图页面
@app.route("/citespace_view")
def citespace_view():
    return render_template("citespace_view.html")


#运行
if __name__ == '__main__':
    app.run()