# 豆瓣电影抓取  

-------

##  抓取思路:

>* 先用F12来抓取Ajax格式的请求原生的URL

>* 根据请求构造字典,从而返回json格式的字典

>* 负责简单的数据清洗,除去无用的信息,并将有用的信息保存到文件中

## 具体代码:

* 第一种方法  ![GitHub file size in bytes](https://img.shields.io/github/size/hfg123/Spider_crawler/Douban/douban_spider.py.svg?label=code%20size)

> * 1.运用yield(**generator**)方法, 重新构造并写入文件中. 
>> * ### [chick here to read source](https://github.com/hfg123/Spider_crawler/blob/master/Douban/douban_spider.py)  
>>* #### [抓取实例1](https://github.com/hfg123/Spider_crawler/blob/master/Douban/donban.csv)

----

* 第二种方法 ![GitHub file size in bytes](https://img.shields.io/github/size/hfg123/Spider_crawler/Douban/numpy_test.py.svg?label=code%20size)
> * 2.运用**pandas**库来对数据进行处理,比上述方法便捷.
>>* ### [chick here to read source](https://github.com/hfg123/Spider_crawler/blob/master/Douban/numpy_test.py)
>>* #### [抓取实例2](https://github.com/hfg123/Spider_crawler/blob/master/Douban/douba.csv)

