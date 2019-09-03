# -*- coding: utf-8 -*-
# author :HXM

from requests import get
from time import strftime, localtime, sleep
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.Qt import QApplication, QMainWindow


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
                result = realtime + ' ' + data.get('desc') + '\n'  # 构造信息
                with open('express.txt', 'a', encoding='utf-8')as f:  # 写入文件
                    f.write(result)
            pass
        except Exception as e:
            print(f"error is {e}")
            pass

    pass


class Ui_Form(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 650)
        icon = QtGui.QIcon("ico.ico")
        MainWindow.setWindowIcon(icon)
        self.textEdit = QtWidgets.QTextEdit(MainWindow)
        self.textEdit.setGeometry(QtCore.QRect(4, 110, 992, 536))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit.setGeometry(QtCore.QRect(80, 50, 600, 40))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(780, 50, 60, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(900, 50, 60, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(10, 50, 60, 40))
        self.label.setObjectName("label")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("Form", "快递查询"))
        self.lineEdit.setStyleSheet('''QLineEdit{
        border:1px solid gray;
        width:300px;
        border-radius:10px;
        padding:2px 4px;
        bd:4
        }''')
        self.textEdit.setStyleSheet("font: 12pt \"KaiTi_GB2312\";")
        self.lineEdit.setPlaceholderText(" 示例:4600284951052 ")
        self.pushButton.setText(_translate("MainWindow", "查询"))
        self.pushButton.setShortcut(_translate("MainWindow", "Ctrl+Return"))
        self.pushButton_2.setText(_translate("MainWindow", "清空"))
        self.pushButton_2.setShortcut(_translate("MainWindow", "Ctrl+Del"))
        self.label.setText(_translate("MainWindow", "订单号"))


class ExpressWindows(QMainWindow, Ui_Form):

    def __init__(self, parent=None):

        super(ExpressWindows, self).__init__(parent)
        self.setupUi(self)
        self.setWindowOpacity(0.9)
        self.pushButton.clicked.connect(self.express)
        self.pushButton_2.clicked.connect(self.deldetail)

    def express(self):
        try:
            postid = self.lineEdit.text()  # 订单号获取
            query = Express(postid=postid)  # 传递订单号
            query.parse()  # 执行解析

            with open('express.txt', 'r+', encoding='utf-8')as f:
                detail = f.read()  # 读取内容
                self.textEdit.setText(detail)  # 显示文本
                f.seek(0)  # 定位到开头
                f.truncate()  # 删除内容
        except Exception:
            pass

    pass

    def deldetail(self):
        '''
        清空文本信息
        :return:
        '''
        self.textEdit.clear()
        self.lineEdit.clear()
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ExpressWindows()
    win.show()  # 4600284951052
    sys.exit(app.exec())
