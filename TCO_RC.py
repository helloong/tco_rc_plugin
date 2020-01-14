# -*- coding: utf-8 -*-

"""
################################################################################
    Title: TCO Remote Control Portable Plug-in
    Author: helloong@gmail.com
    DateTime: 2020.01.13 First created
    History:
        - 2020.01.13 First created
################################################################################
"""
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from tco_rc_ui import Ui_frm_main
from PyQt5 import uic
import subprocess
import socket
import os

# form_class = uic.loadUiType(os.path.abspath(os.path.dirname(__file__)) + '\\TCO_RC_PlugIn.ui')[0]


class WindowClass(QMainWindow, Ui_frm_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.btn_connect.clicked.connect(self.btn_connect_clicked)
        self.btn_help.clicked.connect(self.btn_help_clicked)
        self.btn_quit.clicked.connect(self.btn_quit_clicked)
        self.txt_ip.returnPressed.connect(self.btn_connect.click)

    def get_connect(self):
        ip_adrs = self.txt_ip.text()
        if not ip_adrs:
            print(f'IP: {ip_adrs}')
            QMessageBox.question(self, '확인', '접속대상 IP 주소가 입력되지 않았습니다.', QMessageBox.Ok)
            self.txt_ip.selectAll()
            self.txt_ip.setFocus()
            return -1
        try:
            socket.inet_aton(ip_adrs)
        except Exception as e:
            QMessageBox.question(self, '오류', f'올바른 IP 주소가 아닙니다.', QMessageBox.Ok)
            self.txt_ip.selectAll()
            self.txt_ip.setFocus()
            return -1

        ret_value = subprocess.call(["ZOOKPluginViewer.exe", f"{ip_adrs}:3560"])

    @pyqtSlot()
    def btn_connect_clicked(self):
        self.get_connect()

    @pyqtSlot()
    def btn_help_clicked(self):
        help_msg = """
        언덕저편 너머 미지의 세계에 도달 할 수 있도록 돠드림\n\n
        TCO 네트워크 리스트에 나타나지 않는 IP[172.16.30.11]를\n
        입력 후 연결버튼 클릭\n\n
        - hElLoOnG -
        """
        QMessageBox.question(self, 'TCO_RC_PlugIn for KB & KH', f"{help_msg}", QMessageBox.Ok)
        self.txt_ip.selectAll()
        self.txt_ip.setFocus()

    @pyqtSlot()
    def btn_quit_clicked(self):
        self.close()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()