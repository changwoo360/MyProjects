from settings import *
import pymysql
class Storer(object):
    def save_data(self, data, HOST=HOST, USER=USER, PASSWORD=PASSWORD, DATABASE=DATABASE):
        conn = pymysql.connect(HOST, USER, PASSWORD, DATABASE)
        cursor = conn.cursor()
        sql = "insert proxypool(ip) values(%s)"
        cursor.executemany(sql, data)
        print('数据保存成功')
        conn.commit()
        cursor.close()
        conn.close()

    def main(self):
        pass