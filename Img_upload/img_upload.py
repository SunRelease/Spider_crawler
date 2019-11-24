
import logging
from requests import post

class Sm_Ms():

    def __init__(self):
        '''
        自定义初始化数据,请求头
        '''
        self.url='https://sm.ms/api/v2/upload?inajax=1'

        self.headers={
            'referer': 'https://sm.ms/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
        }

        self.data = {
            'smfile': ("图片名称", open('这里是图片路径', 'rb'), 'image/jpeg'),   #修改这里的参数
            'file_id': ('0')
        }

    def upload(self):
        '''
        上传图片
        '''
        try:

            response=post(url=self.url,headers=self.headers,files=self.data)

            if response.status_code ==200:
                # print(response.json())
                print(response.json().get('data').get('url'))
            else:
                pass
        except Exception as e:
            logging.error(e)
            pass

if __name__ == "__main__":

    pic_upload=Sm_Ms()

    pic_upload.upload()