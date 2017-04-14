# -*- coding: utf-8 -*-

import numpy
from fake_useragent import UserAgent 
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class RotateUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self,user_agent=''):
        self.user_agent = user_agent
        
    def process_request(self,request,spider):
        ua = UserAgent()
        user_agent = ua.random
        print "********Current UserAgent:%s************" % user_agent
        #log.msg('Current UserAgent: '+ua, level='INFO') 
        request.headers.setdefault('User-Agent', user_agent)

class ProxyMiddleware(object):
    
    #从数据库中读取代理url
    proxyList = ['218.92.220.58:8080', '43.226.162.23:80', '27.148.151.27:80', '124.88.67.7:843']
    
    def process_request(self, request, spider):
        pass
        # Set the location of the proxy
        pro_adr = random.choice(self.proxyList)
        print "*******-----------*Current Proxy IP:%s*-----------***********" %pro_adr
        #request.meta['proxy'] = "http://{}:{}@{}:{}".format(user,pass,'127.0.0.1','8118')
        request.meta['proxy'] = "http://"+ pro_adr

class ErrorHandleMiddleware(object):
    def process_response(self, request, response, spider):
        if response.status != 200:
            with open('failed_urls', 'a') as f:
                f.write(response.url + '\n')
        return response