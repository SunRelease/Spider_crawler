# **简介**

 ![A38by4.jpg](https://s2.ax1x.com/2019/03/21/A38by4.jpg)






> 一些简单的爬虫案例,有助于对爬虫的入门和了解

# **编译环境**
 System | win10 1803 
---|---
 Python Version | python3.6.2 |
 Python IDE | VS Code |



# Sougou_spider(搜狗壁纸抓取)

## **安装所需库**
```
pip install requests
pip install Fake_Useragent
pip install urllib

```


### [chick here to read source](https://github.com/hfg123/Spider_crawler/blob/master/Sougou_spider/sougou_crawler.py)

      
>1.这是一个支持搜狗壁纸抓取的案例,运行后将在本文件路径创建文件夹以及图片

>2.**支持url地址抓取,但仅限于搜狗壁纸**

>3.关于程序无法创建文件夹的问题,已经寻找问题,并解决中....

>4.开启多线程池下载,加快下载速率(**3-25 update**)

>5.全新的交互界面,支持命令行自定义抓取相关壁纸(**3-25 update**)

>6.准备对该程序进行重构,优化BUG,使用类进行面向对象编程>>>....(**4-2 update**)

>7.正在准备GUI界面,>>主要基于pyqt5编写...
***



# Html_parse(网页抓取)

## **安装所需库**
```

pip install lxml
pip install beautifulsoup4
pip install pyquery

```


### [chick here to read source](https://github.com/hfg123/Spider_crawler/blob/master/Html_parse/Get_ip.py)

>1.这是运用基本原生的框架进行初步网页提取,**方法包括但不仅限于下面的方法**
>>1. beautifulsoup4,pyquery,正则表达式,xpath

>2.**主要是对简单的网页进行抓取,仅限于对反爬措施不强的网站**(update 4-2)


# Douban_crawler(豆瓣)

## **安装所需库**
```
pip install requests

```


### [chick here to read source](https://github.com/hfg123/Spider_crawler/blob/master/Douban/douban_spider.py)

>1.这是一个关于豆瓣抓取的简单爬虫

>2.默认以csv文件生成在文件夹中,顺序为ID, title ,rate ,url

>3.如果想修改抓取抓取页数,**请参照84行文档修改案例**








