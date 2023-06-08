# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './interfaces/signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_signup(object):
    def setupUi(self, signup):
        signup.setObjectName("signup")
        signup.resize(625, 504)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(signup.sizePolicy().hasHeightForWidth())
        signup.setSizePolicy(sizePolicy)
        signup.setMinimumSize(QtCore.QSize(625, 504))
        signup.setMaximumSize(QtCore.QSize(625, 504))
        self.centralwidget = QtWidgets.QWidget(signup)
        self.centralwidget.setObjectName("centralwidget")
        self.signup_title = QtWidgets.QLabel(self.centralwidget)
        self.signup_title.setGeometry(QtCore.QRect(100, 90, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(30)
        self.signup_title.setFont(font)
        self.signup_title.setAlignment(QtCore.Qt.AlignCenter)
        self.signup_title.setObjectName("signup_title")
        self.email_label = QtWidgets.QLabel(self.centralwidget)
        self.email_label.setGeometry(QtCore.QRect(140, 180, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)
        self.email_label.setFont(font)
        self.email_label.setTextFormat(QtCore.Qt.RichText)
        self.email_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.email_label.setObjectName("email_label")
        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(140, 240, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)
        self.pass_label.setFont(font)
        self.pass_label.setTextFormat(QtCore.Qt.RichText)
        self.pass_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pass_label.setObjectName("pass_label")
        self.repass_label = QtWidgets.QLabel(self.centralwidget)
        self.repass_label.setGeometry(QtCore.QRect(110, 300, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)
        self.repass_label.setFont(font)
        self.repass_label.setTextFormat(QtCore.Qt.RichText)
        self.repass_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.repass_label.setObjectName("repass_label")
        self.email_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.email_input.setGeometry(QtCore.QRect(280, 180, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.email_input.setFont(font)
        self.email_input.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.email_input.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.email_input.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.email_input.setDocumentTitle("")
        self.email_input.setOverwriteMode(False)
        self.email_input.setObjectName("email_input")
        self.pass_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pass_input.setGeometry(QtCore.QRect(280, 240, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.pass_input.setFont(font)
        self.pass_input.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pass_input.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pass_input.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.pass_input.setDocumentTitle("")
        self.pass_input.setPlainText("")
        self.pass_input.setOverwriteMode(False)
        self.pass_input.setObjectName("pass_input")
        self.repass_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.repass_input.setGeometry(QtCore.QRect(280, 300, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.repass_input.setFont(font)
        self.repass_input.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.repass_input.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.repass_input.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.repass_input.setDocumentTitle("")
        self.repass_input.setOverwriteMode(False)
        self.repass_input.setObjectName("repass_input")
        self.signup_btn = QtWidgets.QPushButton(self.centralwidget)
        self.signup_btn.setGeometry(QtCore.QRect(280, 360, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.signup_btn.setFont(font)
        self.signup_btn.setObjectName("signup_btn")
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(400, 360, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.login_btn.setFont(font)
        self.login_btn.setDefault(False)
        self.login_btn.setFlat(True)
        self.login_btn.setObjectName("login_btn")
        signup.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(signup)
        self.statusbar.setObjectName("statusbar")
        signup.setStatusBar(self.statusbar)

        self.retranslateUi(signup)
        QtCore.QMetaObject.connectSlotsByName(signup)

    def retranslateUi(self, signup):
        _translate = QtCore.QCoreApplication.translate
        signup.setWindowTitle(_translate("signup", "Create new account"))
        self.signup_title.setText(_translate("signup", "Create a new account"))
        self.email_label.setText(_translate("signup", "Email Address"))
        self.pass_label.setText(_translate("signup", "Password"))
        self.repass_label.setText(_translate("signup", "Re-enter password"))
        self.email_input.setPlaceholderText(_translate("signup", "Enter your email address"))
        self.pass_input.setPlaceholderText(_translate("signup", "Enter your password"))
        self.repass_input.setPlaceholderText(_translate("signup", "Re-enter your password"))
        self.signup_btn.setText(_translate("signup", "Sign up account"))
        self.login_btn.setText(_translate("signup", "Already have an account?"))
