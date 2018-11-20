from pyquery import PyQuery as pq
import io
import sys
import pymysql
import requests
import time
import re
import random
import requests
import os
from requests.exceptions import ConnectionError
import sys 
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, dir)
from tests.updater import Updater 



sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


class Crawler():

    def get_response(self, url):
        USER_AGENTS = [
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
            "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
        ]
        headers = {
            'User-Agent': random.choice(USER_AGENTS),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Accept-Encoding': 'gzip, deflate',
        }
        try:
            response = requests.get(url, headers=headers)
            if response.status_code is 200:
                return response.text
        except Exception as result:
            print("The <get_response> program got an exception：\"{}\"".format(result))
            return

    def get_data_66ip(self, start_page=1, stop_page=10):
        base_url = "http://www.66ip.cn/{}.html"
        url_list = [base_url.format(i) for i in range(start_page, stop_page+1)]
        for url in url_list:
            content = self.get_response(url)
            if content:
                pattern = re.compile("<td>([0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4})</td><td>([0-9]{4})</td")
                items = re.findall(pattern, content)
                for host, port in items:
                    yield "{}:{}".format(host, port)

    def get_data_xici(self, start_page=11, stop_page=15):
        base_url = "http://www.66ip.cn/{}.html"
        url_list = [base_url.format(i) for i in range(start_page, stop_page+1)]
        for url in url_list:
            content = self.get_response(url)
            if content:
                pattern = re.compile("<td>([0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4})</td><td>([0-9]{4})</td")
                items = re.findall(pattern, content)
                for host, port in items:
                    yield "{}:{}".format(host, port)

    def get_data_kuai(self, start_page=1, stop_page=10):
        base_url = "http://www.kuaidaili.com/free/inha/{}/"
        url_list = [base_url.format(i) for i in range(start_page, stop_page+1)]
        for url in url_list:
            content = self.get_response(url)
            if content:
                pattern = re.compile('<td data-title="IP">(.*?)</td>') 
                host = re.findall(pattern,content)
                pattern = re.compile('<td data-title="PORT">(.*?)</td>')
                port = re.findall(pattern, content)
                for host,port in zip(host,port):
                    new_proxy = host + ":" + port
                    yield new_proxy

    def get_data_daxiang(self):
        pass
    
    def main(self):
        base_ip_list = []
        base_ip_list.append(self.get_data_66ip())
        base_ip_list.append(self.get_data_xici())
        base_ip_list.append(self.get_data_kuai())
        # base_ip_list.append(self.get_data_daxiang())
        
        print('数据抓取成功')
        return Updater().new_update(base_ip_list)
        
        '''
        for old_proxy in Updater().new_update(base_ip_list):
            print(old_proxy)
            yield old_proxy
'''



    def save_data(self, data):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='ren666666', database='proxypool')
        cursor = conn.cursor()
        sql = "insert proxypool(ip) values(%s)"
        cursor.executemany(sql, data)
        conn.commit()
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        print(result)
    def get_data(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='ren666666', database='proxypool')
        print('----1----')
        cursor = conn.cursor()
        sql = "select ip from proxypool"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result


