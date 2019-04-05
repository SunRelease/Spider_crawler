from pandas import Series, DataFrame
import requests
import time


def get_source(page_start):
    # 获取相应网页源码
    # 构造参数
    headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'Host': 'movie.douban.com',
        'Referer': 'https://movie.douban.com'}
    url = 'https://movie.douban.com/j/search_subjects'
    params = {
        "type": "moive",
        "tag": "热门",
        "sort": "recommend",
        "page_limit": "20",
        "page_start": page_start
    }
    # 为了方便,保持会话
    session = requests.Session()
    response = session.get(url=url, params=params, headers=headers)
    if response.status_code == 200:
        # 返回有效请求 response==200
        # 将结果打印在控制台上
        print(response.content.decode('utf-8'))
        # Ajax json格式化
    return response.json()


def parse(json):
    # 运用pandas库DataFrame进行数据清洗
    jsons = DataFrame(json)
    print(type(jsons))
    # 将数据导出csv文件
    jsons.to_csv('.\douba.csv', index=False, header=False, encoding='utf-8-sig', mode='a')


if __name__ == '__main__':
    for page_start in range(0, 200, 20):
        json = get_source(page_start=page_start)
        parse(json=json)
        time.sleep(3)
