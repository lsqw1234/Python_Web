import pymysql # pymysql 임포트

# 전역변수 선언부
conn = None
cur = None

conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='TEST', charset='utf8')
cur = conn.cursor()
