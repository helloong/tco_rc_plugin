# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TCO_RC_PlugIn.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frm_main(object):
    def setupUi(self, frm_main):
        frm_main.setObjectName("frm_main")
        frm_main.resize(282, 111)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("TConsole_1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frm_main.setWindowIcon(icon)
        self.verticalLayoutWidget = QtWidgets.QWidget(frm_main)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 261, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_ip = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_ip.setObjectName("lbl_ip")
        self.horizontalLayout_2.addWidget(self.lbl_ip)
        self.txt_ip = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_ip.setMaxLength(15)
        self.txt_ip.setObjectName("txt_ip")
        self.horizontalLayout_2.addWidget(self.txt_ip)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_connect = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_connect.setObjectName("btn_connect")
        self.horizontalLayout.addWidget(self.btn_connect)
        self.btn_help = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_help.setObjectName("btn_help")
        self.horizontalLayout.addWidget(self.btn_help)
        self.btn_quit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_quit.setObjectName("btn_quit")
        self.horizontalLayout.addWidget(self.btn_quit)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(frm_main)
        QtCore.QMetaObject.connectSlotsByName(frm_main)

    def retranslateUi(self, frm_main):
        _translate = QtCore.QCoreApplication.translate
        frm_main.setWindowTitle(_translate("frm_main", "TCO Remote Plug-In ver 0.9 beta"))
        self.lbl_ip.setText(_translate("frm_main", "IP주소"))
        self.btn_connect.setText(_translate("frm_main", "연결"))
        self.btn_help.setText(_translate("frm_main", "도움말"))
        self.btn_quit.setText(_translate("frm_main", "닫기"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frm_main = QtWidgets.QDialog()
    ui = Ui_frm_main()
    ui.setupUi(frm_main)
    frm_main.show()
    sys.exit(app.exec_())

