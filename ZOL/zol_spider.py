# -*- coding: utf-8 -*-
# author :HXM
'''

1.对笔记本电脑排行和品牌进行抓取,为接下来收集整理提供数据支持
2.网站为:http://detail.zol.com.cn/
3.拓展版,支持图片保存并分类
'''

from tqdm import trange
from os import makedirs
from requests import get
from random import randint
from os.path import exists
from time import sleep, perf_counter
from re import compile, findall, S, sub


class Zol():
    def __init__(self, price):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        }
        self.price = price
        self.url = 'http://detail.zol.com.cn/notebook_index/subcate16_0_list_{}_{}.html'

    pass

    def get_response(self, url):
        try:
            response = get(url, headers=self.headers)
            sleep(2)
            return response
        except Exception as e:
            print("error is %s" % e)

    pass

    def page_next(self, offset):
        '''
        页数递归和价格修改
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

    def save_image(self, item):
        '''
        1.支持图片分类并保存
        2.默认在本地生成image总文件夹

        :param item:
        :return:
        '''
        try:
            if not exists('{}/{}'.format('images', item.get('dir_name'))):
                makedirs('{}/{}'.format('images', item.get('dir_name')))
            pic_name = randint(10000, 90000)
            file_path = '{}/{}/{}.{}'.format('images', item.get('dir_name'), pic_name, 'jpg')
            image_url = item.get('image_url')
            response = self.get_response(image_url)
            start_time = perf_counter()
            with open(file_path, 'wb')as f:
                f.write(response.content)
                print('Download success %s.jpg!' % pic_name)
            end_time = perf_counter()
            # 进度条显示
            for i in trange(100):
                sleep(end_time - start_time)
        # 抛出异常
        except Exception as  e:
            print("download fail is %s" % e)

    pass

    def run(self):
        '''
        1.函数入口点
        :return:
        '''
        for offset in range(1, 10, 1):
            url = self.page_next(offset)
            html = self.get_html(url)
            items = self.parse_text(html)
            for item in items:
                self.save_image(item)

    pass


if __name__ == '__main__':
    price = input("请输入您想要的价位的电脑信息:")
    spider = Zol(price=price)
    spider.run()
