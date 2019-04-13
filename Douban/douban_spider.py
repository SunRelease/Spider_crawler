#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author :HXM


import time
import requests
from faker import Faker
from random import randint


class Douban():
    # 初始化变量
    def __init__(self, tag, page):
        # 定义标签
        self.tag = tag
        # 定义页数
        self.page = page
        # Ajax接口API
        self.url = 'https://movie.douban.com/j/search_subjects'
#         添加随机请求头
        faker = Faker()
        # 请求头headers随机化
        self.headers = {
            'User_Agent': faker.user_agent(),
            'Host': 'movie.douban.com',
            'Referer': 'https://movie.douban.com'}
        pass

    def get_source(self, page_strat):
        # 获取相应网页源码
        # 构造参数
        params = {
            "type": "moive",
            "tag": self.tag,
            "sort": "recommend",
            "page_limit": "20",
            "page_start": page_strat
        }
        # 随机延时
        response = requests.get(url=self.url, params=params, headers=self.headers)
        sleep_time = randint(1, 3)
        time.sleep(sleep_time)
        if response.status_code == 200:
            # 返回有效请求 response==200
            # Ajax json格式化
            return response.json()
        else:
            # 非正常请求则返回空
            return None

    pass

    def parser(self, response):
        # 字典键值获取 .get('键')
        jsons = response.get('subjects')
        for json in jsons:
            # 分别获取名字,url,评分,以及ID
            title = json.get('title')
            rate = json.get('rate')
            url = json.get('url')
            id = json.get('id')
            '''
             用生成器返回一个字典
             title
             rate
             ID
             url
            '''
            # 将结果打印在控制台上
            print("{} {} {}".format(title,rate,url))
            yield {
                'title': title,
                'rate': rate,
                'url': url,
                'id': id
            }
        pass

    def save(self, items):
        # 对文件进行保存
        try:
            for item in items:
                # 保存为csv文件,逗号分隔值
                with open('donban.csv', 'a', encoding='utf-8-sig')as f:
                    f.write(
                        "{},{},{},{}\n".format(item.get('id'), item.get('title'), item.get('rate'), item.get('url')))
        except Exception as e:
            # 如有错误则输出错误
            print("error is %s" % e)

        pass

    def run(self):
        # 定义程序运行
        pages = int(self.page)* 20
        for page_start in range(0, pages, 20):
            '''
            大家可以根据需求进行修改抓取s
            思路:
            用input函数进行交互
            '''
            # 获取网页
            response = self.get_source(page_strat=page_start)
            # 解析网页
            items = self.parser(response)
            # 保存结果
            self.save(items)
            # 默认休眠2秒,以防止localhost IP访问被禁止
            time.sleep(2)
        pass


if __name__ == '__main__':
    page = input("请输入抓取页数:")
    tag = input("请输入抓取标签:")
    douban_spider = Douban(tag=tag, page=page)
    douban_spider.run()

