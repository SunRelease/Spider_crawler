# 图床上传

- 这是一个关于图片图床源获取的一个示例,尽量去除掉网站上图片上传的限制.


### 分析过程

#### 寻找网址

- 这是一个比较稳定的网址,有用户亲测16年的图片还有效,图床源确实比较稳定,下面是该图床的首页

![20191124005430](https://upload.cc/i1/2019/11/24/MjABoC.jpg)

- 可以看到这里官网提供了API上传服务,而且有用户身份`token`认证,以及其他相关信息
![20191124005537](https://upload.cc/i1/2019/11/24/CI1DvS.jpg)

####  分析请求

- 直接打开chrome调试控制台,点击`perverse log`防止丢包

![20191124005603](https://upload.cc/i1/2019/11/24/4bKohJ.jpg)

- 随便上传一个图片,先观察抓包情况.

![20191124002122](https://upload.cc/i1/2019/11/24/vc6O1Y.jpg)

- 首先可以直接使用过滤器,先进入xhr,大部分数据都是属于xhr类的,果然找到了仅有的一个网址,在看看`response`,的确是数据图床请求.

![20191124002502](https://upload.cc/i1/2019/11/24/nY6vFi.jpg)

![20191124002528](https://upload.cc/i1/2019/11/24/xujZRA.jpg)


- 这里我们可以尝试看看`post`的是什么数据,直接滑下来查看`Form Data`,可以看到这么一个结果.

![20191124002733](https://upload.cc/i1/2019/11/24/L9m5ek.jpg)

- 这个`WebKitFormBoundary`是什么呢?直接搜索,按照网上这样子理解.

> *首先生成了一个 `boundary` 用于分割不同的字段，为了避免与正文内容重复，`boundary` 很长很复杂。然后 `Content-Type` 里指明了数据是以 `mutipart/form-data` 来编码，本次请求的 `boundary` 是什么内容。消息主体里按照字段个数又分为多个结构类似的部分，每部分都是以 `--boundary` 开始，紧接着内容描述信息，然后是回车，最后是字段具体内容（文本或二进制）。如果传输的是文件，还要包含文件名和文件类型信息。消息主体最后以 `--boundary--` 标示结束。*

- 实际上就是直接分割数据段存储,这是`post`方法中比较常用的,而且支持原生浏览器的请求表单的一种方式.那么该如何书写请求呢?我从`requests`官网中得到了[解释](http://cn.python-requests.org/zh_CN/latest/user/quickstart.html#post-multipart-encoded).

![20191124003802](https://upload.cc/i1/2019/11/24/XZ1rgO.jpg)

- 根据官方文档说给的解释结合该网页的数据分段,我直接创建了如下的格式表单.

![20191124004019](https://upload.cc/i1/2019/11/24/utCgqm.jpg)

```Python
self.data = {
            'smfile': (f"{image_name}.jpg", open(f'pic_history/{image_name}.jpg', 'rb'), 'image/jpeg'),
            'file_id': ('0')
        }
```

- 直接上请求,果然请求成功,返回了图片源地址,经测试没有问题.

![20191124004639](https://upload.cc/i1/2019/11/24/JknLph.jpg)

![20191124004803](https://upload.cc/i1/2019/11/24/tiYreK.jpg)

### [源代码](https://github.com/SunRelease/Spider_crawler/blob/master/Img_upload/img_upload.py)
