# -*- coding: utf-8 -*-
# author :HXM
'''
1.对笔记本电脑排行和品牌进行抓取,为接下来收集整理提供数据支持
2.网站为:http://detail.zol.com.cn/
3.精简版,只保留数据
'''
from requests import get
from time import sleep
from re import compile, findall, S
from os import makedirs
from os.path import exists

class Zol():
    def __init__(self, price):
        '''
        1.根据网址对self.url进行修改
        '''
        self.price = price
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        }
        self.url = 'http://detail.zol.com.cn/notebook_index/subcate16_list_{}_{}.html'

    pass

    def get_response(self, url):
        '''
        1.requests 请求复用
        :param url:
        :return:
        '''
        try:
            response = get(url, headers=self.headers)
            sleep(2)
            return response
        except Exception as e:
            print("error is %s" % e)

    pass

    def page_next(self, offset):
        '''
        1.页数递归
        :param offset:
        :return:
        '''
        url = self.url.format(self.price, offset)
        return url

    pass

    def get_html(self, url):
        '''
        1.获取网页源码
        :param url:
        :return:
        '''
        response = self.get_response(url)
        return response.text

    pass

    def parse_text(self, html):
        '''
        1.解析网页,清洗数据
        :param html:
        :return:
        '''
        if not exists("zol_detail"):
            makedirs("zol_detail")
        #     csv文件位置
        save_csv_path = "zol_detail/zol_{}.csv".format(self.price)
        pattern = compile(
            'height=.*?.src="(.*?)" alt=.*?<h3><a href.*? title="(.*?)".*?class="price-tip">(.*?)</span>.*?class="price-type">(.*?)</b>.*?class="score">(.*?)</span>',
            S)
        results = findall(pattern, html)
        results.pop(0)
        for result in results:
            print('详情:{},评分:{} 参考价:{}'.format(result[1], result[4], result[2], result[3]))
            # 生成文件csv格式,可以自动匹配价格
            with open(save_csv_path, 'a', encoding='utf-8-sig')as f:
                f.write('{},{},{}\n'.format(result[4], result[1], result[3]))
            dir_name = result[1][0:15]
            yield {
                'image_url': result[0],
                'dir_name': dir_name
            }

    pass

    def run(self):
        '''
        1.函数的入口点
        :return:
        '''
        for offset in range(1, 6, 1):
            url = self.page_next(offset)
            html = self.get_html(url)
            self.parse_text(html)

    pass


if __name__ == '__main__':
    price = input("请输入您想要的价位的电脑信息:")
    spider = Zol(price=price)
    spider.run()
