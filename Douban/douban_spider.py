import requests
import time


class Douban():
    # 初始化变量
    def __init__(self, tag):
        # 定义标签
        self.tag = tag
        # Ajax接口API
        self.url = 'https://movie.douban.com/j/search_subjects'
        # 请求头headers
        self.headers = {
            'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
            'Host': 'movie.douban.com',
            'Referer': 'https://movie.douban.com'}
        pass

    def get_source(self, page_start):
        # 获取相应网页源码
        # 构造参数
        params = {
            "type": "moive",
            "tag": self.tag,
            "sort": "recommend",
            "page_limit": "20",
            "page_start": page_start
        }
        # 为了方便,保持会话
        session = requests.Session()
        response = session.get(url=self.url, params=params, headers=self.headers)
        if response.status_code == 200:
            # 返回有效请求 response==200
            # 将结果打印在控制台上
            print(response.content.decode('utf-8'))
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
                with open('donban.csv', 'a', encoding='utf-8')as f:
                    f.write(
                        "{},{},{},{}\n".format(item.get('id'), item.get('title'), item.get('rate'), item.get('url')))
        except Exception as e:
            # 如有错误则输出错误
            print("error is %s" % e)

        pass

    def run(self):
        # 定义程序运行
        for page_start in range(0, 100, 20):
            '''
            这里是默认从0到100,步长为20抓取
            大家可以根据需求进行修改抓取
            思路:
            用input函数进行交互
            '''
            # 获取网页
            response = self.get_source(page_start=page_start)
            # 解析网页
            items = self.parser(response)
            # 保存结果
            self.save(items)
            # 默认休眠2秒,以防止localhost IP访问被禁止
            time.sleep(2)
        pass


if __name__ == '__main__':
    douban_spider = Douban("热门")
    douban_spider.run()



