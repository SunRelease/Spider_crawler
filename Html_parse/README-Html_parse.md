# 数据抓取以及简单清洗

--------------

## 网页抓取思路

>* ### **获取网页源代码**:
>>* #### 如果是静态界面,可以考虑用requestes库直接请求
>>* #### 如果是动态界面,要考虑JavaScript渲染和Ajax分离,这时候要运用其他方法解决 

----
## 案例

- [x] **[代理IP 1.0版](https://github.com/hfg123/Spider_crawler/blob/master/Html_parse/Get_proxies.py)**

>* ###  **对一个反爬能力不强的网站进行自定义网址抓取代理IP**:
>>* ### 该网站是以文本保留的静态页面.为p节点的文本,思路,直接用正则表达式,默认生成txt文本在本目录下



- [x] **[反爬代理 1](https://github.com/hfg123/Spider_crawler/blob/master/Html_parse/%E8%A5%BF%E5%88%BAip.py)**

>* ### **对某知名的免费代理进行抓取并构造格式**:
>>* ### 该网站抓取的ip与port是分离的,而且掺杂无用数据,要进行数据清洗和构造正常参数
>>* ### 运用正则表达式提取,并用generator返回字典,默认生成txt文本在本目录下

- [x] **[反爬代理 2](https://github.com/hfg123/Spider_crawler/blob/master/Html_parse/proxies.py)**

- ### 这次的网站是国外服务器的网站,需要科学上网才能获取到数据,直接上分析:

- ##### 从这里面看.可以轻易分析出请求构造:

|`key`|`value`|说明|
|:---:|:---:|:---:|
|`page`|1|页数|
|`limit`|10|页的数据多少限制|

![20191130235715](https://upload.cc/i1/2019/11/30/JDSP7z.jpg)

![20191130235625](https://upload.cc/i1/2019/11/30/auTmc9.jpg)


- ##### 当直接访问时,是会出现json数据,但是当直接放在python中请求时,会出现状态码500错误.

![20191201000300](https://upload.cc/i1/2019/12/01/prJGXb.jpg)

![20191201000439](https://upload.cc/i1/2019/12/01/imguNa.jpg)

- 分析一下原因,可能是请求头没有加,加入最常见的`User-Agent`和`referer`后,还是出现了如下错误

![20191201000439](https://upload.cc/i1/2019/12/01/imguNa.jpg)

- 后来推测可能原因在`Cookies`那里,毕竟他没有请求参数或者其他的请求意向,极大可能在`Cookies`已经存储了验证信息了,打开Cookies`存储单元,里面有很多数据,但是还不能判定哪个是验证信息.

![20191201001009](https://upload.cc/i1/2019/12/01/xhDEpa.jpg)

- 于是我在响应头里找到了一个可疑数据`session`,他是唯一一个在请求头和响应头里面同时存在的,所以我清空该值试试响应结果,果然是500状态码,确定了该请求数据的验证信息来自于`session`.

![20191201001400](https://upload.cc/i1/2019/12/01/r1B2Nu.jpg)

![20191201001549](https://upload.cc/i1/2019/12/01/t7WKdF.jpg)

- 解决方法:直接在请求头添加`Cookies`就可以解决问题

![20191201001808](https://upload.cc/i1/2019/12/01/UwigIa.jpg)

- 解决代码:
```Python
self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'cookie': 'session=eyJfcGVybWFuZW50Ijp0cnVlLCJwYXRoIjoiL2dhb25pIn0.EMK4Jw.SVpjwvOHNYGzsnNj72LceRTBVa4',
            'referer': 'https://www.attackmen.com/gaoni'
        }
```


-----



### 抓取成果实例

> ### [代理IP样品](https://github.com/hfg123/Spider_crawler/blob/master/Html_parse/ip_%E8%A5%BF%E5%88%BA.txt)
