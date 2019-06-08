# Express(快递查询)

## 目录

- [原理](#origin)

- [成品](#Express)


<h3 id ="origin"> 原理 </h3>

> * 抓包模拟`post`请求,`实现快速单的查询`

> * 运用`python` 实现`请求`以及`爬取`过程


<h3 id="Express"> 成品 </h3>

- [x] [Express(通用GUI版)](https://github.com/SunRelease/Spider_crawler/blob/master/Express/Express.py)

> * 直接请求爬取快递API参数

> * 支持市面上所有快递单号类型查询

> * 优化代码,提升运行速度

> * 使用原生`tkinter`库进行GUI界面编写,缩小文件体积

> * 待完善中...   [GUI下载](https://www.lanzous.com/i4htgta)

---

- [x] [Express100(官网版)](https://github.com/SunRelease/Spider_crawler/blob/master/Express/Express100.py)

> * 对快递100进行官网查询

> * 请求参数

| 参数类型 | 参数解析 | 参数实例|
|:---:|:---:|:---:|
|`type`|快递单号类型|`yunda`|
|`postid`|快递单号|4600284951052|
|`id`|固定参数|1|
|`temp`|随机数字|0.2083000676955935|

> * 对于`temp`开始不了解其生成原理,所以猜测尝试js逆向

>> * 全局搜索`temp`,果然在某个js文件找到参数temp

![Vaw2DO.png](https://s2.ax1x.com/2019/06/06/Vaw2DO.png)

>> * 还发现其URl的构造原理

>> * `temp`参数时由`JavaScript`的`Math.random()`生成的

>> * 于是只要执行`js`函数,并将结果返回给`data`参数就行

> * 关于查询结果

>> * 查询结果与订单号不符合,不知道原因,可能是后端加入`crsftoken`认证

>> * 只是提供爬取原理,具体查询请使用第一个成品
