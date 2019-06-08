# -*- coding: utf-8 -*-
# author :HXM
from requests import get
from time import strftime, localtime, sleep


class Express():

    def __init__(self, postid):
        '''
        1.定义请求头
        :param postid:
        '''
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
            'Cookie': 'BAIDUID=DAA787C560F69EBAFD63BF6F95568E73:FG=1; ZD_ENTRY=bing; BIDUPSID=DAA787C560F69EBAFD63BF6F95568E73; PSTM=1559650935; delPer=0; BD_HOME=0; H_PS_PSSID=26523_1421_21084_29135_29237_28518_29099_29138_28839_28585_26350; BD_UPN=12314753',
            'Host': 'sp0.baidu.com'
        }
        self.url = 'https://sp0.baidu.com/9_Q4sjW91Qh3otqbppnN2DJv/pae/channel/data/asyncqury?'
        self.params = {
            'appid': 4001,
            'com': '',
            'nu': postid
        }

    pass

    def get_response(self):
        '''
        1.获取response,并json格式化
        :return:
        '''
        try:
            response = get(url=self.url, headers=self.headers, params=self.params)
            sleep(1)
            if response.status_code == 200:
                return response.json()
            else:
                return None
            pass

        except Exception as e:
            print(f"error is {e}")
            pass

    pass

    def parse(self, response):
        '''
        1.解析时间戳
        2.提取信息
        :param response:
        :return:
        '''
        try:
            datas = response.get('data').get('info').get('context')  # 获取datas信息
            for data in datas:  # 循环提取信息
                times = int(data.get('time'))
                timelocal = localtime(times)
                realtime = strftime("%Y-%m-%d %H:%M:%S", timelocal)  # 时间戳转换为标准时间
                print('{} {}\n'.format(realtime, data.get('desc')))  # 打印信息
            pass

        except Exception as e:
            print(f"error is {e}")
            pass

    pass

    def run(self):
        '''
        1.函数起点
        :return:
        '''
        try:
            response = self.get_response()
            self.parse(response=response)

        except Exception as e:
            print(f"error is {e}")

    pass


if __name__ == '__main__':
    '''
    启动函数
    '''

    postid = int(input("请输入订单号:"))  # 测试单号:4600284951052
    express = Express(postid=postid)
    express.run()
