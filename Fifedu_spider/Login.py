# -*- coding: utf-8 -*-
# author :HXM

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Login():

    def __init__(self, username, password):
        '''
        1.初始化用户名密码
        :param username:
        :param password:
        '''
        self.username = username
        self.password = password
        # 定义无头浏览器,由于想可视化,暂时不使用
        self.chrome_option = Options()
        self.chrome_option.add_argument('--headless')
        #参数可使取消可视化
        self.browser = webdriver.Chrome()

    def login(self):
        '''
        请求登陆界面
        :return:
        '''
        self.browser.get('https://www.fifedu.com')

        button1 = self.browser.find_element_by_class_name('login')
        button1.click()
        # 用户名输入
        inputs = self.browser.find_element_by_id('username')
        inputs.send_keys(self.username)
        # 密码输入
        passwd = self.browser.find_element_by_id('password')
        passwd.send_keys(self.password)
        #确认登陆
        button2 = self.browser.find_element_by_id('loginBtn')
        button2.click()

if __name__ == '__main__':

    username=input("请输入您的用户名:")
    password=input("请输入您的密码:")
    logins=Login(username=username,password=password)
    logins.login()
