# -*- coding: utf-8 -*-
# author :HXM


import os
import sys
import time
import random
import requests
from multiprocessing import Pool


class Image():

    def __init__(self, query, start_page):
        '''
        初始化变量
        :param query:
        '''
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
            'cookie': 'ABTEST=0|1554980405|v1; IPLOC=CN4401; SUV=006F02A478ECB1325CAF1E35AF346387; JSESSIONID=aaajNLx9bNXqrhK8FdmOw; tip_show_home_search=20190411; SNUID=6EEAB0235C5EDD644D819B135C19A8A3; ld=Bkllllllll2trecclllllVhs40klllllWnheGkllll9llllljZlll5@@@@@@@@@@; tip_show=20190411'
        }

        self.url = 'https://pic.sogou.com/pics'

        self.query = query
        self.start_page = start_page

    def get_page(self, page):
        '''
        1.默认创建images文件夹
        2.传入参数,将数据格式化
        :param page:
        :return:
        '''

        if not os.path.exists('images'):
            os.makedirs('images')

        params = {
            'query': self.query,
            'mode': 1,
            'start': page,
            'reqType': 'ajax',
            'reqFrom': 'result',
            'tn': 0
        }

        session = requests.Session()
        response = session.get(url=self.url, params=params, headers=self.headers)

        try:
            if response.status_code == 200:
                # print(response.content.decode('utf-8'))
                return response.json()
            else:
                return None
        #     排除异常
        except Exception as e:

            print("error is %s" % e)

    pass

    def page_parse(self, htmls):
        '''
        1.数据解析提取
        2.清洗返回字典
        :param htmls:
        :return:
        '''
        jsons = htmls.get('items')

        for json in jsons:
            url = json.get('ori_pic_url')

            yield {
                'url': url
            }

    pass

    def save(self, items):
        '''
        1.字典的遍历
        2.保存图片在images文件中
        :param items:
        :return:
        '''
        try:
            for item in items:
                responses = requests.get(url=(item.get('url')), headers=self.headers)
                if responses.status_code == 200:
                    # 随机命名图片
                    name = random.randint(1000, 99999)
                    # 设置开始时间
                    start_time = time.time()
                    # 保存图片
                    with open('images/{}.jpg'.format(name), 'wb')as f:

                        f.write(responses.content)
                        # 模拟进度条
                        for i in range(100):
                            k = i + 1

                            str = '>' * (i // 2) + '' * ((100 - k) // 2)

                            sys.stdout.write('\r' + str + '[%s%%]' % (i + 1))

                            sys.stdout.flush()

                            time.sleep(0.01)
                    #         结束时间
                    end_time = time.time()

                    print("Download %s.jpg success! It cost %.2f s" % (name, (end_time - start_time)))
                else:
                    print("Download fail!")

        except Exception as e:

            print("Download %s" % e)

    pass

    def total_size(self, path):
        '''
        递归计算文件夹大小
        增加文件计算代码优化
        :param path:
        :return:
        '''
        size_sum = 0
        file_list = os.listdir(path)
        for name_list in file_list:

            abs_path = os.path.join(path, name_list)
            if os.path.isdir(abs_path):

                size = self.total_size(abs_path)
                size_sum += size
            else:
                size_sum += os.path.getsize(abs_path)
        return size_sum

    def run(self):
        '''
        启动函数,并开始抓取
        :return:
        '''
        pages = int(self.start_page)*48
        for page in range(48, pages, 48):
            htmls = self.get_page(page=page)

            items = self.page_parse(htmls=htmls)

            self.save(items)

            time.sleep(1)

            sizes = float(self.total_size('images'))

            real_size = sizes / 1024 / 1024

            print("抓取第%s页成功,目前文件夹总大小 %.2f MB" % (page/48, real_size))
        pass


GROUP_START = 0
GROUP_END = 8

if __name__ == '__main__':
    '''
    交互界面
    开启多线程池
    '''
    query = input("请输入关键字:")
    page = input("请输入抓取的页数:")

    pool = Pool()

    groups = ([x * 15 for x in range(GROUP_START, GROUP_END + 1)])

    spider = Image(query=query, start_page=page)

    pool.map(spider.run(), groups)

    pool.join()

    pool.close()
