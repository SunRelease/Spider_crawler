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



- [x] **[反爬代理 1.0 版](https://github.com/hfg123/Spider_crawler/blob/master/Html_parse/%E8%A5%BF%E5%88%BAip.py)**

>* ### **对某知名的免费代理进行抓取并构造格式**:
>>* ### 该网站抓取的ip与port是分离的,而且掺杂无用数据,要进行数据清洗和构造正常参数
>>* ### 运用正则表达式提取,并用generator返回字典,默认生成txt文本在本目录下


-----

### 抓取成果实例

> ### [代理IP样品](https://github.com/hfg123/Spider_crawler/blob/master/Html_parse/ip_%E8%A5%BF%E5%88%BA.txt)
