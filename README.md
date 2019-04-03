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

      
>1.This is a support wallpaper capture web page, support sogou image capture, and folder classification

>2.**Url capture is supported, but only for sogou wallpapers**

>3.There may be a folder suggestion problem, and I will try to solve the situation first

>4.Optimize the creation of thread pools to prevent downtime(**3-25 update**)

>5.New interactive interface, customizable keywords and pages(**3-25 update**)

>6.GUI interface writing in progress...
***



# Html_parse(网页抓取)

## **安装所需库**
```

pip install lxml
pip install beautifulsoup4
pip install pyquery

```


### [chick here to read source](https://github.com/hfg123/Spider_crawler/blob/master/Html_parse/Get_ip.py)

>1.This is a web page parsing folder. It contains xpath,bs4, regular expressions,pyquery use method



# Douban_crawler(豆瓣)

## **安装所需库**
```
pip install requests

```


### [chick here to read source](https://github.com/hfg123/Spider_crawler/blob/master/Douban/douban_spider.py)

>1.这是一个关于豆瓣抓取的简单爬虫

>2.默认以csv文件生成在文件夹中,顺序为ID, title ,rate ,url

>3.如果想修改抓取抓取页数,**请参照84行文档修改案例**








