# PICTURE SPIDER

---

## 本目录下介绍几个关于图片抓取以及批量下载的实例

---

### 实例一  

* ### [搜狗壁纸](https://pic.sogou.com/)

* ## [source](https://github.com/SunRelease/Spider_crawler/blob/master/Picture_spider/sougou_crawler.py)

----

>* 1.关于程序无法创建文件夹的问题,已经寻找问题,并解决中....

>* 2.开启多线程池下载,加快下载速率(**3-25 update**)

>* 3.全新的交互界面,支持命令行自定义抓取相关壁纸(**3-25 update**)

>* #### 4.准备对该程序进行重构,优化BUG,使用类进行面向对象编程>>>....(**4-2 update**)

>* 5.正在准备GUI界面,>>主要基于pyqt5编写...

---

### 实例二

* ### [高清壁纸抓取](https://unsplash.com/)

* ## [source](https://github.com/SunRelease/Spider_crawler/blob/master/Picture_spider/Image_spider.py)
----

>* 1.交互命令行界面,支持用户输入页数以及抓取内容(**由于是国外网站,目前仅支持英文输入**)

>* 2.多线程池开启,加快下载速度,默认休眠2秒

>* 3.设置了一定的反爬,所以下载较慢

>* 4.默认在本执行文件位置下设置子文件夹images,并以suffix为JPg格式保存图片

>* 5.更多详情请看源文件注释文档
----

