# -*- coding: utf-8 -*-
# author :HXM

import time
import js2py
import requests

# 创建js执行对象
content = js2py.EvalJs()

class Baidu_Translate(object):

    def __init__(self, query, froms, to):
        '''
        1.定义初始化变量
        2.注意头请求要对应
        :param query:
        '''
        self.url = "https://fanyi.baidu.com/basetrans"
        self.query = query
        self.froms = froms
        self.to = to
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Mobile Safari/537.36",
            "Referer": "https://fanyi.baidu.com/",
            "Cookie": "locale=zh; BAIDUID=1A1E2309C9CAD413D3D8DCD3A184E526:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1555066435; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1555066444; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1555074113; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1555074113"
        }

    def creat_sign(self):
        '''
        1.执行js函数
        2.获取sign值
        :return:
        '''
        with open(r'.\translate_base.js', "r", encoding="utf-8") as f:
            content.execute(f.read())
            # 调用js中的函数生成sign
        sign = content.a(self.query)
        # 将sign加入到params中
        return sign

    pass

    def get_params(self, sign):
        '''
        1.构造字典
        2.默认是中文变英文
        :param sign:
        :return:
        '''
        params = {
            "query": self.query,
            "from": self.froms,
            "to": self.to,
            "token": "6fd9079d741adce0cc8cc1336220dc0b",
            "sign": sign
        }
        # 返回字典
        return params

    pass

    def get_translate(self, params):
        '''
        1.请求后台
        2.格式化数据AJAX模式
        :param params:
        :return:
        '''
        response = requests.post(url=self.url, headers=self.headers, params=params)
        # json格式化
        return response.json()

    pass

    def get_word(self, word):
        '''
        1.清洗数据
        2.获取翻译后结果
        3.注意这里是返回列表而不是字典
        :param word:
        :return:
        '''
        translate = word['trans'][0]['dst']
        return translate

    pass

    def run(self):
        '''
        1.启动函数
        2.显示翻译结果
        :return:
        '''
        sign = self.creat_sign()
        params = self.get_params(sign=sign)
        word = self.get_translate(params=params)
        translate_word = self.get_word(word=word)
        print(translate_word)
        time.sleep(1)

    pass


if __name__ == '__main__':
    # 输入翻译内容
    froms = input(
        "请输入您输入语言类型(英文简写):\n'jp': '日语'\n'fra': '法语'\n'ru': '俄语'\n'cht': '中文繁体'\n'zh': '中文'\n'en': '英语'\n'spa': '西班牙语'\n'kor': '韩语'\n'tr': '土耳其语'\n'vie': '越南语'\n")
    to = input(
        "请输入您要转换后语言类型(英文简写):\n'jp': '日语'\n'fra': '法语'\n'ru': '俄语'\n'cht': '中文繁体'\n'zh': '中文'\n'en': '英语'\n'spa': '西班牙语'\n'kor': '韩语'\n'tr': '土耳其语'\n'vie': '越南语'\n")
    query = input("请输入要翻译的内容:")

    translate_word = Baidu_Translate(query=query, froms=froms, to=to)

    translate_word.run()
