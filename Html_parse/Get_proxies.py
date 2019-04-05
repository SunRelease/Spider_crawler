# -*- coding: utf-8 -*-
# author :HXM
from lxml import etree
import requests
import re
from fake_useragent import UserAgent
def page_get():
        
        ua=UserAgent()

        url=input("请输入代理网页:")
        #https://proxy.horocn.com/day-free-proxy/e8ZG.html

        headers={'User-Agent' : ua.random}
#设置请求头
        response=requests.get(url,headers=headers)
#用requests.get
        if response.status_code==200:
        #服务器返回状态码为200时正常,继续进行下一步,否则结束
                datas=response.text
                
                return datas
                #返回HTMl
         return None
def parse():

        pattern=re.compile('.*?<br />(.*?)#.*?<br />',re.S)
        #re.S表示换行匹配,不受行数限制,python常用pattern来封装表达式规则,极大方便了调用

        result=re.findall(pattern,datas)
        #表示寻找Html里面的所有匹配规则的字符串

        print(type(result))
        #打印值返回型
        for results in result:
        #列表的遍历
                with open ("ip.txt","a",encoding="utf-8") as f:
        #将结果保存到列表中.以text的格式
                        f.write("{}\n".format(results))
        print("Download successfully!")
        
        return None
if __name__ == '__main__':
  
  page_get()
  
  parse()
