# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """
        메인 윈도우의 사용자 인터페이스를 설정하는 메서드입니다.
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 100)
        MainWindow.setWindowTitle("간단한 덧셈 계산기")

        # 중앙 위젯 및 레이아웃 설정
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 첫 번째 숫자 입력창
        self.input1 = QtWidgets.QLineEdit(self.centralwidget)
        self.input1.setObjectName("input1")
        self.input1.setPlaceholderText("숫자 1")
        self.horizontalLayout.addWidget(self.input1)

        # '+' 라벨
        self.plus_label = QtWidgets.QLabel(self.centralwidget)
        self.plus_label.setText("+")
        self.plus_label.setObjectName("plus_label")
        self.horizontalLayout.addWidget(self.plus_label)

        # 두 번째 숫자 입력창
        self.input2 = QtWidgets.QLineEdit(self.centralwidget)
        self.input2.setObjectName("input2")
        self.input2.setPlaceholderText("숫자 2")
        self.horizontalLayout.addWidget(self.input2)

        # '=' 라벨
        self.equal_label = QtWidgets.QLabel(self.centralwidget)
        self.equal_label.setText("=")
        self.equal_label.setObjectName("equal_label")
        self.horizontalLayout.addWidget(self.equal_label)

        # 결과 표시 라벨
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setText("결과")
        self.result_label.setObjectName("result_label")
        self.horizontalLayout.addWidget(self.result_label)

        # 계산 버튼
        self.calculate_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_button.setText("add")
        self.calculate_button.setObjectName("calculate_button")
        self.horizontalLayout.addWidget(self.calculate_button)

        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
