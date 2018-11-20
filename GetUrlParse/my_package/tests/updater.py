import requests
from collections import Iterable

class Updater(object):
    def __init__(self):
        self.old_proxy = []
    def new_update(self, base_ip_list):
        for proxy_list in base_ip_list:
            for base_ip in proxy_list:
                proxies = {"http": "http://{0}".format(base_ip)}
                try:
                    r = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=10, verify=False)
                    if r.status_code == 200:
                        yield base_ip
                except Exception as e:
                    pass
                '''
                try:
                    session = requests.session()
                    session.proxies = {base_ip}
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0'}
                    test_url = 'https://www.baidu.com/'
                    resp = session.get(test_url, timeout=5, headers=headers)
                    print(resp.status_code)
                    print('successful--->{}'.format(base_ip))
                    old_list = tuple(list(i.split(' ')))
                    print(old_list)
                    yield old_list
                except:
                    pass
                    #print('error-->{}'.format(base_ip))
                    '''


    def old_update(self):
        pass

    def main(self):
        pass
