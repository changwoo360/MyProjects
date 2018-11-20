
# import nature models
import random
import time


# import extend models

# import personal models
from settings import *


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

class GetUrlParse(object):
    
    """docstring for GetParseUrl"""
    def __init__(self):
        self.sleep_time = SLEEP_TIME
        self.check_ip_url = CHECK_IP_URL
        self.request_url = []
        self.cookies = []
        self.ua_list = UA_LIST


    def user_agent(self):
        user_agent_choice = {'user-agent': random.choice(self.ua_list)}
        return user_agent_choice


    def request_frequency(self):
        time_sleep_choice = random.sample(self.sleep_time, 1)[0]
        request_frequency_choice = random.randint(time_sleep_choice[0], time_sleep_choice[1])

        print('The program is sleeping:need {}s'.format(request_frequency_choice))
        time.sleep(request_frequency_choice)

    def url_parse(self, url):
        
        try:
            response = requests.get(url, headers=self.user_agent())
            if response.status_code is 200:
                print('Parse url:({}) successful!'.format(url))
                return response.text    
                self.request_frequency()
            else:
                print("The url's status_code isn't 200! Please check!")
                return None
        except (ConnectionError):
            print('Error occurred')
            return None
        except Exception as result:
            print('捕获到其他异常:{}'.format(result))
            return None


    def get(self, urls):
        
        if isinstance(urls, list):
            return [self.url_parse(i) for i in urls]

        elif isinstance(urls, str):
            return self.url_parse(urls)

        else:
            print('Please input a valid value in function "get", for excaple: ["www.abc.com", "www.abc.com", "www.abc.com"] or "www.abc.com".')










