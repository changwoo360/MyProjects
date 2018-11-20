from gets.crawler import Crawler
from dbs.storer import Storer

class GetProxy(object):
	def __init__(self):
		pass
		'''
		self.proxy_list = Crawler().main()
		'''
	def proxypool_num(self):
		a = 20
		if a < 100:
			return True
		else:
			return False

	def run(self):
		if self.proxypool_num():
			ip_list = Crawler().main()
			print('数据筛选成功')
			Storer().save_data(ip_list)

			





