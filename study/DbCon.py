import pymysql# pymysql 임포트
print(pymysql.version_info)

# 전역변수 선언부

config = {
     'host' : '127.0.0.1',
     'user' : 'root',
     'password' : '1234',
     'database' : 'work',
     'port' : 3306,
     'charset':'utf8',
     'use_unicode' : True}

conn = None
cur = None
# db 환경변수 -> db 연동 객체
conn = pymysql.connect(**config)

# **config : config에 들어있는 7개의 환경변수를 이용해서 DB를 연동한다는 의미
# sql 실행 객체
cursor = conn.cursor();

# 메인 코드
# conn = pymysql.connect(host='http://127.0.0.1', user='root', password='root', db='tes', charset='utf8') # 접속정보
# cur = conn.cursor() # 커서생성
sql = "SELECT * FROM user"  # 실행할 sql문
cur.execute(sql)  # 커서로 sql문 실행
while (True):
    row = cur.fetchone()
    if row == None:
        break
        data1 = row[0]
        print(data1)

        # conn.commit() # 저장
        conn.close()  # 종료


