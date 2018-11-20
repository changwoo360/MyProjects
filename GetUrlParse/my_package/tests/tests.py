



class TestProxy():
	def __init__(self):
		self.old_proxy = ['1','2']
	def proxypool_num(self):
		a = 20
		if a > 100:
			return True
		else:
			return False

	def run(self):
		if self.proxypool_num():
			for proxy in self.old_proxy:
				print(proxy)