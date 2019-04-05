import re
import time
import requests


class Xici_ip():

    def __init__(self, offset):
        # 定义抓取免费代理的页数
        self.offset = offset
        '''
        1.构造请求头
        2.模拟请求头(由于设置反爬,请求头模拟尽量全
        '''
        self.url = 'https://www.xicidaili.com/nn/' + str(offset)
        self.headers = {

            'Host': 'www.xicidaili.com',
            'Referer': 'https://www.xicidaili.com/',
            'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTUwMGY4NDAxYzBjMWMwNTgxNWY4ZGU2MmRjZGNhODQ1BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMURQSTllVGt1TzRxOFdZYVYvTGVQVWNOYzFWRUtRSTlaQjV3K1pGUk5VNHc9BjsARg%3D%3D--ac0fdca7a7223a011ab000eeaca2c29741b84d3c; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1554464998; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1554465003',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
        }
        pass

    def html_get(self):
        '''
        保持会话,维护cookies
        :return:
        '''
        session = requests.Session()
        response = session.get(url=self.url, headers=self.headers)
        try:
            if response.status_code == 200:
                html = response.content.decode('utf-8')
                print(type(html))
                return html
        #     排除异常
        except Exception as e:
            print("connection error{}".format(e))
        pass

    def parser(self, htmls):
        '''
        1.用正则表达式来提取网页规则
        2.返回字典,清洗数据
        '''
        pattern = re.compile('<td class="country".*?src=' +
                             '.*?alt=.*?</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>', re.S)
        items = re.findall(pattern, htmls)
        for item in items:
            yield {
                'ip': item[0],
                'port': item[1]
            }
        pass

    def write_file(self, contents):
        '''
        1.根据字典保存数据
        2.默认在本文件目录下生成>>ip_西刺.txt
        :param contents:
        :return:
        '''
        for content in contents:
            with open('ip_西刺.txt', 'a', encoding='utf-8') as f:
                f.write('{}:{}\n'.format(content.get('ip'), content.get('port')))

    def run(self):
        '''
        1.定义启动函数
        2.设置休眠为5秒,反爬虫简单过法

        '''
        htmls = self.html_get()
        print(htmls)
        contents = self.parser(htmls=htmls)
        self.write_file(contents=contents)
        time.sleep(5)


if __name__ == "__main__":
    # 函数开头
    for offset in range(2, 4, 1):
        '''
        1.默认从第二页到第四页
        2.可以根据需求修改
        '''
        spider = Xici_ip(offset=offset)
        spider.run()
