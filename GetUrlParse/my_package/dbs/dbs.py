import pymysql
from dbs.storer import Storer

class Dbs(object):
	def run(self, HOST, USER, PASSWORD, DATABASE):
		try:
			db = pymysql.connect(HOST, USER, PASSWORD, DATABASE)

		except:
			print('error')

