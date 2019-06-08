# -*- coding: utf-8 -*-
# author :HXM

from requests import get, post
from time import sleep
import json
from js2py import eval_js
import random


class Express100():

    def __init__(self, postid):
        '''
        1.初始化变量
        :param postid:
        '''
        self.headers = {
            'User-Agent': self.useragent_choice(),
        }
        self.postid = postid
        self.id_url = 'https://www.kuaidi100.com/query?'  # 快递查询API
        self.type_url = 'https://m.kuaidi100.com/apicenter/kdquerytools.do?'  # 类型API
        self.id_params = {  # 查询data
            'type': self.type_return(),
            'postid': postid,
            'id': 1,
            'valicode': '',
            'temp': self.temp(),
            'phone': '',
            'token': '',
            'platform': 'MWWW'
        }

    pass

    def useragent_choice(self):
        '''
        请求头的随机更换
        :return:
        '''
        useragent = [
            'Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; u18 Build/JRO03H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30',
            'Mozilla/5.0 (Linux; U; Android 4.0.3; en-us; M9 Build/IML74K)',
            'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; Redmi 3 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.8 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; U; Android 4.3; zh-CN; SCH-N719 Build/JSS15J) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.9.5.489 U3/0.8.0 Mobile Safari/533.1',
            'Mozilla/5.0 (Linux; U; Android 5.0.2; zh-cn; Redmi Note 3 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.85 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.1.6',
            'Mozilla/5.0 (Linux; Android 4.4.4; Lenovo S90-t Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 baiduboxapp/5.0 (Baidu; P1 4.4.4)',
            'Mozilla/5.0 (Linux; Android 4.4.4; Che1-CL10 Build/Che1-CL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3 rabbit/1.0 baiduboxapp/7.2 (Baidu; P1 4.4.4)',
            'Mozilla/5.0 (Linux; Android 4.4.4; Che1-CL10 Build/Che1-CL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3',
            'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-N9200 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 5.0.2; Redmi Note 3 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.2 TBS/036555 Safari/537.36 V1_AND_SQ_6.5.0_390_YYB_D QQ/6.5.0.2835 NetType/WIFI WebP/0.3.0 Pixel/1080',
        ]
        ua = random.choice(useragent)
        return ua

    pass

    def get_type_response(self):
        '''
        1.获取快递类型
        :return:
        '''
        type_params = {
            'method': 'autoComNum',
            'text': self.postid
        }
        response = get(url=self.type_url, headers=self.headers, params=type_params)

        sleep(0.5)

        return response.json()

    pass

    def type_return(self):
        '''
        1.传递类型参数
        :return:
        '''
        jsons = self.get_type_response()

        datas = jsons.get('auto')

        return datas[0].get('comCode')  # 碰到多个信息匹配时.默认首个类型

    pass

    def temp(self):
        '''
        1.temp参数的随机生成,构造查询参数
        :return:
        '''
        temp = eval_js('''
        
        function creatTemp() {
            return Math.random()
        }
        creatTemp()

        ''')

        return temp

    pass

    def post_query(self):
        '''
        1.发送参数请求快递信息
        :return:
        '''
        response = post(url=self.id_url, headers=self.headers, params=self.id_params)

        sleep(0.5)

        return response.json()

    pass

    def parse_express(self, response):
        '''
        1.解析response,打印信息
        :param response:
        :return:
        '''
        express = response.get('data')
        for data in express:
            context = data.get("context")
            time = data.get('ftime')
            print('{} {}\n'.format(time, context))

    pass

    def run(self):
        '''
        1.函数启动点
        :return:
        '''
        response = self.post_query()
        self.parse_express(response=response)


if __name__ == '__main__':
    '''
    1.函数入口点
    '''
    postid = int(input("请输入订单号:"))  # 测试:4600284951052
    express = Express100(postid=postid)
    express.run()
