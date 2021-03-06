# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WindowsWellbeing(object):
    def setupUi(self, WindowsWellbeing):
        WindowsWellbeing.setObjectName("WindowsWellbeing")
        WindowsWellbeing.resize(811, 600)
        WindowsWellbeing.setMinimumSize(QtCore.QSize(800, 600))
        WindowsWellbeing.setMaximumSize(QtCore.QSize(16777215, 16777215))
        WindowsWellbeing.setAutoFillBackground(False)
        WindowsWellbeing.setStyleSheet("background-color: rgb(231, 231, 231);")
        self.centralwidget = QtWidgets.QWidget(WindowsWellbeing)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(100, 520, 631, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setSizeIncrement(QtCore.QSize(1, 1))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.todayBt = QtWidgets.QPushButton(self.frame)
        self.todayBt.setGeometry(QtCore.QRect(250, 0, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.todayBt.setFont(font)
        self.todayBt.setStyleSheet("QPushButton{\n"
"    border:2px solid white;\n"
"    background-color:white;\n"
"    outline:none;\n"
"}\n"
"QPushButton:focus{\n"
"    border:2px solid grey;\n"
"}")
        self.todayBt.setObjectName("todayBt")
        self.prevBt = QtWidgets.QPushButton(self.frame)
        self.prevBt.setGeometry(QtCore.QRect(40, 0, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.prevBt.setFont(font)
        self.prevBt.setStyleSheet("QPushButton{\n"
"    border:2px solid white;\n"
"    background-color:white;\n"
"    outline:none;\n"
"}\n"
"QPushButton:focus{\n"
"    border:2px solid grey;\n"
"}")
        self.prevBt.setObjectName("prevBt")
        self.aboutBt = QtWidgets.QPushButton(self.frame)
        self.aboutBt.setGeometry(QtCore.QRect(460, 0, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aboutBt.sizePolicy().hasHeightForWidth())
        self.aboutBt.setSizePolicy(sizePolicy)
        self.aboutBt.setSizeIncrement(QtCore.QSize(2, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.aboutBt.setFont(font)
        self.aboutBt.setStyleSheet("QPushButton{\n"
"    border:2px solid white;\n"
"    background-color:white;\n"
"    outline:none;\n"
"}\n"
"QPushButton:focus{\n"
"    border:2px solid grey;\n"
"}")
        self.aboutBt.setObjectName("aboutBt")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 9, 1191, 501))
        self.stackedWidget.setSizeIncrement(QtCore.QSize(1, 1))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page1 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page1.sizePolicy().hasHeightForWidth())
        self.page1.setSizePolicy(sizePolicy)
        self.page1.setObjectName("page1")
        self.todayOption = QtWidgets.QFrame(self.page1)
        self.todayOption.setGeometry(QtCore.QRect(0, 460, 801, 41))
        self.todayOption.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.todayOption.setFrameShadow(QtWidgets.QFrame.Raised)
        self.todayOption.setObjectName("todayOption")
        self.foregroundBt = QtWidgets.QPushButton(self.todayOption)
        self.foregroundBt.setGeometry(QtCore.QRect(270, 0, 121, 41))
        self.foregroundBt.setStyleSheet("QPushButton{\n"
"    border:2px solid white;\n"
"    background-color:white;\n"
"    outline:none;\n"
"}\n"
"QPushButton:focus{\n"
"    border:2px solid grey;\n"
"}")
        self.foregroundBt.setObjectName("foregroundBt")
        self.backgroundBt = QtWidgets.QPushButton(self.todayOption)
        self.backgroundBt.setGeometry(QtCore.QRect(440, 0, 121, 41))
        self.backgroundBt.setStyleSheet("QPushButton{\n"
"    border:2px solid white;\n"
"    background-color:white;\n"
"    outline:none;\n"
"}\n"
"QPushButton:focus{\n"
"    border:2px solid grey;\n"
"}")
        self.backgroundBt.setObjectName("backgroundBt")
        self.frame_2 = QtWidgets.QFrame(self.page1)
        self.frame_2.setGeometry(QtCore.QRect(10, 0, 1171, 461))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.foreAndBackStackedToday = QtWidgets.QStackedWidget(self.frame_2)
        self.foreAndBackStackedToday.setGeometry(QtCore.QRect(0, 0, 791, 451))
        self.foreAndBackStackedToday.setObjectName("foreAndBackStackedToday")
        self.foreground = QtWidgets.QWidget()
        self.foreground.setObjectName("foreground")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.foreground)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-10, 0, 801, 461))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.todayFrQhbox = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.todayFrQhbox.setContentsMargins(0, 0, 0, 0)
        self.todayFrQhbox.setObjectName("todayFrQhbox")
        self.foreAndBackStackedToday.addWidget(self.foreground)
        self.background = QtWidgets.QWidget()
        self.background.setObjectName("background")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.background)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(-10, 0, 801, 471))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.backgroundQhbox = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.backgroundQhbox.setContentsMargins(0, 0, 0, 0)
        self.backgroundQhbox.setObjectName("backgroundQhbox")
        self.foreAndBackStackedToday.addWidget(self.background)
        self.noTodayDataPage = QtWidgets.QWidget()
        self.noTodayDataPage.setObjectName("noTodayDataPage")
        self.noDataLabelToday = QtWidgets.QLabel(self.noTodayDataPage)
        self.noDataLabelToday.setGeometry(QtCore.QRect(220, 160, 351, 151))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.noDataLabelToday.setFont(font)
        self.noDataLabelToday.setAlignment(QtCore.Qt.AlignCenter)
        self.noDataLabelToday.setWordWrap(True)
        self.noDataLabelToday.setObjectName("noDataLabelToday")
        self.foreAndBackStackedToday.addWidget(self.noTodayDataPage)
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setStyleSheet("")
        self.page2.setObjectName("page2")
        self.label2 = QtWidgets.QLabel(self.page2)
        self.label2.setGeometry(QtCore.QRect(310, 150, 131, 161))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label2.setFont(font)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setWordWrap(True)
        self.label2.setObjectName("label2")
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.thanks = QtWidgets.QLabel(self.page3)
        self.thanks.setGeometry(QtCore.QRect(250, 100, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.thanks.setFont(font)
        self.thanks.setAlignment(QtCore.Qt.AlignCenter)
        self.thanks.setWordWrap(True)
        self.thanks.setObjectName("thanks")
        self.link = QtWidgets.QLabel(self.page3)
        self.link.setGeometry(QtCore.QRect(250, 250, 271, 41))
        self.link.setAlignment(QtCore.Qt.AlignCenter)
        self.link.setObjectName("link")
        self.stackedWidget.addWidget(self.page3)
        WindowsWellbeing.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WindowsWellbeing)
        self.statusbar.setObjectName("statusbar")
        WindowsWellbeing.setStatusBar(self.statusbar)

        self.retranslateUi(WindowsWellbeing)
        self.stackedWidget.setCurrentIndex(0)
        self.foreAndBackStackedToday.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(WindowsWellbeing)

    def retranslateUi(self, WindowsWellbeing):
        _translate = QtCore.QCoreApplication.translate
        WindowsWellbeing.setWindowTitle(_translate("WindowsWellbeing", "Window Wellbeing"))
        self.todayBt.setText(_translate("WindowsWellbeing", "Today\'s stats"))
        self.prevBt.setText(_translate("WindowsWellbeing", "Previous Stats"))
        self.aboutBt.setText(_translate("WindowsWellbeing", "About"))
        self.foregroundBt.setText(_translate("WindowsWellbeing", "Foreground apps"))
        self.backgroundBt.setText(_translate("WindowsWellbeing", "Background apps"))
        self.noDataLabelToday.setText(_translate("WindowsWellbeing", "No statistics found for today. Reboot your computer or try running script manually"))
        self.label2.setText(_translate("WindowsWellbeing", "previous graphs will go here"))
        self.thanks.setText(_translate("WindowsWellbeing", "Thanks for trying out this software "))
        self.link.setText(_translate("WindowsWellbeing", "<html><head/><body><p>Link to github source code <a href=\"https://github.com/pratik0903/Windows-Wellbeing\"><span style=\" text-decoration: underline; color:#0000ff;\">here</span></a></p></body></html>"))
#import qtImage_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowsWellbeing = QtWidgets.QMainWindow()
    ui = Ui_WindowsWellbeing()
    ui.setupUi(WindowsWellbeing)
    WindowsWellbeing.show()
    sys.exit(app.exec_())
