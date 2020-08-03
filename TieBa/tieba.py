# -*- coding: utf-8 -*-
# author :HXM

# -*- coding: utf8 -*-
# 百度贴吧网上签到
from requests import Session
from time import sleep
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [line:%(lineno)d] - %(levelname)s: %(message)s')


class Tieba_Signture():

    def __init__(self):
        '''
        初始化相关网址以及填写自己账号的Cookies值
        '''
        self.data_url = 'https://tieba.baidu.com/mo/q/newmoindex?'
        self.sign_url = 'http://tieba.baidu.com/sign/add'
        self.tbs = '4fb45fea4498360d1547435295'
        self.headers = {
            'Accept': 'text/html, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': '',  # 这里找到BDUSS和STOKEN的值并按照格式'BDUSS=  ;STOKEN= '填写上去
            'Host': 'tieba.baidu.com',
            'Referer': 'http://tieba.baidu.com/i/i/forum',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'}
        self.data = []
        self.session = Session()

    def get_likes(self):
        '''
        获取账号贴吧关注目录
        :return:
        '''
        try:
            tieba_datas = self.session.get(url=self.data_url, headers=self.headers).json()['data']['like_forum']
            for tieba_data in tieba_datas:
                self.data.append(tieba_data['forum_name'])
        except Exception as  e:
            logging.error(e)
            pass

    def signed(self):
        '''
        定义请求状态码以及返回签到状态
        :return:
        '''
        bars = self.data
        already_signed_code = 1101
        success_code = 0
        need_verify_code = 2150040
        already_signed = 0
        succees = 0
        failed_bar = []
        n = 0
        while n < len(bars):
            sleep(1)
            bar = bars[n]
            data = {
                'ie': 'utf-8',
                'kw': bar,
                'tbs': self.tbs
            }
            try:
                r = self.session.post(self.sign_url, data=data, headers=self.headers)
            except Exception as e:
                logging.error(f'未能签到{bar}, 由于{e}。')
                failed_bar.append(bar)
                continue
            dic = r.json()
            msg = dic['no']
            if msg == already_signed_code:
                already_signed += 1;
                r = '已经签到过了!'
            elif msg == need_verify_code:
                n -= 1;
                r = '需要验证码，即将重试!'
            elif msg == success_code:
                r = f"签到成功!你是第{dic['data']['uinfo']['user_sign_rank']}个签到的吧友,共签到{dic['data']['uinfo']['total_sign_num']}天。"
            else:
                r = '未知错误!' + dic['error']
            logging.info(f"{bar}：{r}")
            succees += 1
            n += 1
        l = len(bars)
        failed = "\n失败列表：" + '\n'.join(failed_bar) if len(failed_bar) else ''
        logging.info(f'''共{l}个吧，其中: {succees}个吧签到成功，{len(failed_bar)}个吧签到失败，{already_signed}个吧已经签到。{failed}''')

    def run(self):
        '''
        启动函数
        :return:
        '''
        try:
            self.get_likes()
            self.signed()
        except Exception as  e:
            logging.error(e)
            pass


if __name__ == '__main__':
    tieba = Tieba_Signture()
    tieba.run()
