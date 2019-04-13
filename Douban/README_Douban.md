# 豆瓣电影抓取  

-------

##  抓取思路:

>* 先用F12来抓取Ajax格式的请求原生的URL

>* 根据请求构造字典,从而返回json格式的字典

>* 负责简单的数据清洗,除去无用的信息,并将有用的信息保存到文件中

## 具体代码:

* 第一种方法  

* ![GitHub file size in bytes](https://img.shields.io/github/size/hfg123/Spider_crawler/Douban/douban_spider.py.svg?label=code%20size)

> * 1.运用yield(**generator**)方法, 重新构造并写入文件中. 
>> * ### [chick here to read source](https://github.com/hfg123/Spider_crawler/blob/master/Douban/douban_spider.py)  
>>* #### [抓取实例1](https://github.com/hfg123/Spider_crawler/blob/master/Douban/donban.csv)


----

* 第二种方法 

* ![GitHub file size in bytes](https://img.shields.io/github/size/hfg123/Spider_crawler/Douban/numpy_test.py.svg?label=code%20size)
> * 2.运用**pandas**库来对数据进行处理,比上述方法便捷.
>>* ### [chick here to read source](https://github.com/hfg123/Spider_crawler/blob/master/Douban/numpy_test.py)
>>* #### [抓取实例2](https://github.com/hfg123/Spider_crawler/blob/master/Douban/douba.csv)

----
## 功能与介绍

- [x] **豆瓣 1.0版** (2019-4-5)

* #### 1.对豆瓣电影网站进行数据抓取,包括评分,名字等

* #### 2.对数据进行简单清洗

- [x] **豆瓣 1.1版** (2019-4-13)

* #### 3.支持自定义标签以及抓取页数,建议标签的页数不要超过10

* #### 4.优化代码,添加随机请求头和延时等待,防止被封IP

