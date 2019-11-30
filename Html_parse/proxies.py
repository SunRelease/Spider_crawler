import requests
import logging
import json
import telnetlib


class Get_Proxy():

    def __init__(self):
        '''
        该地址是国外的服务器,需要科学上网
        '''

        self.url = 'https://www.attackmen.com/freeproxy?page=1&limit=20'

        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36', 'cookie': 'session=eyJfcGVybWFuZW50Ijp0cnVlLCJwYXRoIjoiL2dhb25pIn0.EMK4Jw.SVpjwvOHNYGzsnNj72LceRTBVa4',
            'referer': 'https://www.attackmen.com/gaoni'
        }
        self.params = {
            'page': 1,
            'limit': 10
        }

    def get_proxies(self):

        try:
            response = requests.get(
                url=self.url, headers=self.headers, params=self.params)
            print(response.status_code)
            if response.status_code == 200:
                print(response.json())
                return response.json().get('data')
        except Exception as e:
            logging.error(e)

    def save_json(self):
        '''
        验证并保存有用的代理ip
        '''
        try:

            proxies = self.get_proxies()
            for proxy in proxies:
                ip = proxy.get('ipaddr')
                port = proxy.get('port')
                types = proxy.get('proxy_class')
                self.verify(types=types, ip=ip, port=port)

        except Exception as e:
            logging.error(e)

    def verify(self, types, ip, port):
        '''
        验证ip可用性
        :param types:
        :param ip:
        :param port:
        :return:
        '''
        proxies_pool = {}
        try:
            telnet = telnetlib.Telnet(ip, port=port, timeout=5)
        except:
            print('unconnected')
        else:
            proxies_pool['types'] = types
            proxies_pool['ip'] = f'{ip}:{port}'
            # proxies['port'] = port
            print(f'{types}://{ip}:{port}')
            with open('ip.json', 'a', encoding='utf-8')as f:
                f.write(json.dumps(proxies_pool, indent=2, ensure_ascii=False))

    def last_test(self):
        '''
        最后代理ip测试
        '''
        url = 'http://icanhazip.com'
        #实例
        proxies = {
            "https": "212.112.97.27:3128"
        }
        response = requests.get(url=url, proxies=proxies)
        print(response.text)


if __name__ == '__main__':
    get_proxy = Get_Proxy()
    get_proxy.last_test()
