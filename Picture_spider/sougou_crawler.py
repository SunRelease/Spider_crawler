# -*- coding: utf-8 -*-
# author :HXM

import re,os,requests,json
from fake_useragent import UserAgent
import time
from hashlib import md5
from multiprocessing.pool import Pool

def image_parser(html):
    
    if html.get('items'):

        data=html.get('items')

        for item in data:         #字典的遍历

            image_url=item.get('ori_pic_url')#json值的获取

            r1=r'[\\/:*?"<>|.]'#去除非法文件命名
            image_titles=re.sub(r1,'-',item.get('title'))
            
            yield {
                'image_title' :image_titles,

                'image_url' :image_url
                }#运用generator生成字典
      
                   
def save_image(item):

    img_path = 'imgs' + os.path.sep + item.get('image_title')
    #于上面的函数不一样，只能调用yeild生成器的值，不要用作item.get（‘orinigl_url')

    print("文件路径获取成功!!")
    
    if  img_path[0:50]:#字符串的截取，解决文件名过长的导致无法建立文件夹
       
        if not os.path.exists(img_path): #谨记加not，否则找不到文件

            os.makedirs(img_path)

        try:
            
            resp =requests.get(item.get('image_url'))   

            if resp.status_code==200:

                file_path= img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                    file_name=md5(resp.content).hexdigest(),#运用哈希值生成文件名,防止重复
                    file_suffix='jpg')        

                if not os.path.exists(file_path):   #谨记加not，建立新文件

                    print('建立文件夹成功!!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                    
                    print("path is %s" % file_path)

                    with open (file_path,'wb')as f:

                        f.write(resp.content)#写入文件
                    
                    print('Downloaded image path is %s' % file_path)
                    
                    print('图片保存成功`!!')
                    
                    print("--------------------------------------------------------")
                else:

                    print("Download fail",file_path)

        except requests.ConnectionError:
#输出错误原因
            print("ConnectionError")

            return None
    
def image_get(url):

    try:

        headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
        'Host': 'pic.sogou.com'}
        
        response=requests.get(url,headers=headers)

        if response.status_code==200:

            return response.json()
    
    except requests.ConnectionError as e:

        print("Download fail:{}".format(e.args))
        
        return None

def main():

    word=str(input("请输入抓取关键字:"))

    page=int(input("请输入抓取的页数:"))
# 优化交互界面
    words=urllib.parse.quote(word,encoding='gbk')

    url=r'https://pic.sogou.com/pics?query='+words+r'&mode=1&start='+str(page*48)+r'&reqType=ajax&reqFrom=result&tn=0'
#     重新定义并规划了API接口
    html=image_get(url)

    for item in image_parser(html):

        print(item)

        save_image(item)

GROUP_START = 0
GROUP_END = 8
#线程池的建立
# 减少线程池的数目,降低机器负载,防止宕机
if __name__ == '__main__':
    pool = Pool()
    
    groups = ([x * 15 for x in range(GROUP_START, GROUP_END + 1)])
#     优化线程池
    pool.map(main(), groups)
    
    pool.close()
    
    pool.join()
    
    time.sleep(3)
#默认休息3秒,防止抓取过快导致ip被封
