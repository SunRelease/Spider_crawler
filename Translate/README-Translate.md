# TRANSLATE_SPIDER

* ### 根据Github上的大神思路,仿写了一个翻译爬虫小程序,提高自己的实践能力
----

# [思路](https://fanyi.baidu.com/)

>* ### 对网站进行抓包,可以通过模拟手机版来进行提取有用参数

>* ### 经过分析可得出以下参数

 请求名 |  请求参数
---- | ----
 query| 翻译的内容 (你好)
from | 现在的类型 (zh)
to |转换后的类型 (en)
token | (6fd9079d741adce0cc8cc1336220dc0b) 经过对比参数可以固定
sign | sign

>* ### 这时候sign的值是通过js执行实时得到的结果

>>* ### 这时经过js逆向,得出生成sign值得js文件

>>* ### [chick here to read js](https://github.com/SunRelease/Spider_crawler/blob/master/Translate/translate_base.js)

>* ### 有了sign值,构造传参,解析就可以获取结果了

# 成品

## 1.0版本(4-12) [python 源码版](https://github.com/SunRelease/Spider_crawler/blob/master/Translate/translate.py)

### 实现功能:

* ### 1.可以对输入内容进行翻译您想要得结果 

* ### 2.目前可以支持大多数语言的翻译转换 :[语种简写参照表](http://www.afforange.com/556.html)
> * 日语 法语 俄语 中文繁体 中文 英语 西班牙语 韩语 土耳其语 越南语 ...

* ### 3.**输入转换参数是语种简写,不是汉字**

* ### 4.主要考虑对其实现GUI界面编写,开发中>>>>
----
## 2.0版(4-13)  [shell 版下载](https://www.lanzous.com/i3t37gd)

### 实现功能:

* ### 1.脱离python环境,打包为可执行shell可执行文件,解压即可使用

* ### 2.translate_base.js为必须文件,否则无法获取翻译API

----
## 3.0版(4-15)  [GUI 版下载](https://www.lanzous.com/i3t3ach)

### 实现功能:

* ### 1.优化界面,使用基于pyqt5的GUI图形界面.

* ### 2.优化了代码,精简逻辑.

* ### 3.并将GUI版打包为安装包,会在所选目录下生成Translate3.0文件夹,并默认在桌面生成快捷方式

----




