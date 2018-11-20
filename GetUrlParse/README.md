# Model-GetUrlParse
Extend model: requests.
Installation
------------


    pip install setup
    
    from geturlparse import GetUrlParse

  ~~~
  class ResponseParse(GetUrlParse):
    def __init__(self):
        super(ResponseParse, self).__init__()

   def test(self):
        response = self.get('https://www.baidu.com/')
        print(response)

    

   ResponseParse().test()
~~~
## 配置相关：
- 代理池默认关闭
- 使用时要先继承，可以修改配置参数
- 暂时没有写urllib 和 urllib2
- get方法可以传入一个列表或一个字符串
- 可以设置ip，cookies，headers..
- 对错误进行了捕获
~~~
try:
    try:
        import urllib2  # python2
        USED_PARSER = 'urllib2'
        # urllib.request = urllib2
    except ImportError:
        import requests
        USED_PARSER = 'requests(urllib3)'
except ImportError:
    import urllib.request  # python3 urllib2 = urllib.request
    USED_PARSER = 'urllib'
    urllib2 = urllib.request
~~~
