import time

from multiprocessing import Process

from settings import *
from gets.gets import GetProxy
from tests.tests import TestProxy
from dbs.dbs import Dbs


class Scheduler(object):
	def get_proxy(self, get_proxy_time=GET_PROXY_TIME, get_proxy_num=GET_PROXY_NUM):
		n = 1
		while n < get_proxy_num:
			print("第{}次获取代理循环已启动".format(n))
			GetProxy().run()
			# time.sleep(get_proxy_time)
			n += 1
	def test_proxy(self, test_proxy_time=TEST_PROXY_TIME, post_proxy_num=POST_PROXY_NUM):
		n = 1
		while n < post_proxy_num:
			print("第{}次获取代理循环已启动".format(n))
			TestProxy().run()
			# time.sleep(get_proxy_time)
			n += 1

	def dbs_proxy(self):
		Dbs().run(HOST, USER, PASSWORD, DATABASE)

	def run(self):
		if GETS_:
			Process(target=self.get_proxy).start()
		if TESTS_:
			Process(target=self.test_proxy).start()
		if DBS_:
			Process(target=self.db_proxy).start()

