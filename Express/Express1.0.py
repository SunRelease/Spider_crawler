# -*- coding: utf-8 -*-
# author :HXM
import tkinter as tk
from requests import get
from time import strftime, localtime, sleep


class Express():

    def __init__(self, postid):
        '''
        1.定义请求头
        :param postid:
        '''
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
            'Cookie': 'BAIDUID=DAA787C560F69EBAFD63BF6F95568E73:FG=1; ZD_ENTRY=bing; BIDUPSID=DAA787C560F69EBAFD63BF6F95568E73; PSTM=1559650935; delPer=0; BD_HOME=0; H_PS_PSSID=26523_1421_21084_29135_29237_28518_29099_29138_28839_28585_26350; BD_UPN=12314753',
            'Host': 'sp0.baidu.com'
        }
        self.url = 'https://sp0.baidu.com/9_Q4sjW91Qh3otqbppnN2DJv/pae/channel/data/asyncqury?'
        self.params = {
            'appid': 4001,
            'com': '',
            'nu': postid
        }

    pass

    def get_response(self):
        '''
        1.获取response,并json格式化
        :return:
        '''
        try:
            response = get(url=self.url, headers=self.headers, params=self.params)
            if response.status_code == 200:
                sleep(1)
                return response.json()
            else:
                return None
            pass
        except Exception as e:
            print(f"error is {e}")
            pass

    pass

    def parse(self):
        '''
        1.解析时间戳
        2.提取信息
        :param response:
        :return:
        '''
        try:
            response = self.get_response()
            datas = response.get('data').get('info').get('context')  # 获取datas信息
            for data in datas:  # 循环提取信息
                times = int(data.get('time'))  # 传递时间
                timelocal = localtime(times)  # 本地化时间
                realtime = strftime("%Y-%m-%d %H:%M:%S", timelocal)  # 时间戳转换为标准时间
                # 返回结果
                yield {
                    'time': realtime,
                    'detail': data.get('desc')
                }
            pass
        except Exception as e:
            print(f"error is {e}")
            pass

    pass


class UI():

    def __init__(self):
        windows = tk.Tk()  # 初始化tk库
        windows.iconbitmap(r'.\\ico.ico')  # 图标
        windows.title('快递查询 By:HXM')  # 软件标题
        windows.geometry('430x390')  # 界面大小
        windows.resizable(1300,1300)  # 固定大小
        self.windows = windows

        label = tk.Label(windows, text='订单号:').place(x=0, y=20)
        self.lable = label  # 初始化lable

        search = tk.Entry(windows, width=35, bd=5, show=None)  # show显示成明文形式
        search.place(x=50, y=20)
        self.search = search

        text = tk.Text(windows, height=23, width=60)  # Text控件
        text.place(x=0, y=80)
        self.text = text
        # 事件的绑定
        windows.bind("<Return>", self.express_detail)  # 回车查询
        windows.bind("<Escape>", self.delete)  # Esc清空信息

    pass

    def express_detail(self, event=None):
        '''
        1.显示快递信息函数
        2.事件的绑定需要添加参数 event=None
        :return:
        '''
        try:
            postid = self.search.get()  # 获取订单号
            express = Express(postid=postid)
            datas = express.parse()
            for data in datas:
                result = data.get('time') + ' ' + data.get('detail') + '\n'  # 构造信息
                self.text.insert(tk.END, result)  # 显示信息
            pass
        except Exception as e:
            print(f"error is {e}")
            pass

    pass

    def delete(self, event=None):
        '''
        清空文本
        :return:
        '''
        self.text.delete('1.0', 'end')

        self.search.delete('0', 'end')

    pass

    def button(self):
        '''
        定义button控件
        :return:
        '''
        try:
            button1 = tk.Button(self.windows, text='查询', command=self.express_detail).place(x=320, y=15)
            button2 = tk.Button(self.windows, text='清空', command=self.delete).place(x=380, y=15)
            pass
        except Exception as e:
            print(f"error is {e}")
            pass

    pass

    def run(self):
        '''
        启动函数
        :return:
        '''
        try:
            self.button()
            self.windows.mainloop()
            pass
        except Exception as e:
            print(f"error is {e}")

    pass


if __name__ == '__main__':
    express = UI()
    express.run()
