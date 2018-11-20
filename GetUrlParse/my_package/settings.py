


_version = '0.0.1'


# 爬取频率
# TIME_SLEEP = [[0, 10], [0, 10], [0, 10], [0, 10], [0, 10], [20, 30]]
SLEEP_TIME = [[0, 3], ]


# ip代理池开关
OPEN_IP_POOL = False

# 检测ip可用性
CHECK_IP_URL = [[], ]

# ip代理
IP_PROXY = [[], ]

# user-agent
UA_LIST = [
            'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
            'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
            # others..
            ]


# 使用的解析器
USED_PARSER = ''


# cookies
COOKIES = [[], ]


# ip代理池设置
GETS_ = True
TESTS_ = False
DBS_ = False

GET_PROXY_NUM = 2
GET_PROXY_TIME = 300

POST_PROXY_NUM = 2
TEST_PROXY_TIME = 300

START_PAGE = 1
STOP_PAGE = 3

USER = 'root'
PASSWORD = 'ren666666'
HOST = '127.0.0.1'
DATABASE = 'proxypool'










