# Form implementation generated from reading ui file 'remote.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mute_button(object):
    def setupUi(self, mute_button):
        mute_button.setObjectName("mute_button")
        mute_button.resize(662, 559)
        mute_button.setStyleSheet("background-color: #RRGGBB")
        self.centralwidget = QtWidgets.QWidget(parent=mute_button)
        self.centralwidget.setObjectName("centralwidget")
        self.channel_up = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel_up.setGeometry(QtCore.QRect(170, 220, 75, 23))
        self.channel_up.setObjectName("channel_up")
        self.channel_down = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel_down.setGeometry(QtCore.QRect(170, 290, 75, 23))
        self.channel_down.setObjectName("channel_down")
        self.volume_up = QtWidgets.QPushButton(parent=self.centralwidget)
        self.volume_up.setGeometry(QtCore.QRect(280, 220, 75, 23))
        self.volume_up.setObjectName("volume_up")
        self.volume_down = QtWidgets.QPushButton(parent=self.centralwidget)
        self.volume_down.setGeometry(QtCore.QRect(280, 290, 75, 23))
        self.volume_down.setObjectName("volume_down")
        self.channel_label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.channel_label_2.setGeometry(QtCore.QRect(290, 260, 61, 21))
        self.channel_label_2.setObjectName("channel_label_2")
        self.channel_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.channel_label.setGeometry(QtCore.QRect(180, 260, 47, 13))
        self.channel_label.setObjectName("channel_label")
        self.mute_button_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.mute_button_2.setGeometry(QtCore.QRect(390, 260, 75, 23))
        self.mute_button_2.setObjectName("mute_button_2")
        self.power_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.power_button.setGeometry(QtCore.QRect(160, 20, 75, 23))
        self.power_button.setObjectName("power_button")
        self.horizontalSlider = QtWidgets.QSlider(parent=self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(250, 410, 131, 21))
        self.horizontalSlider.setProperty("value", 50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.channel1_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel1_button.setGeometry(QtCore.QRect(170, 320, 75, 71))
        self.channel1_button.setObjectName("channel1_button")
        self.channel2_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel2_button.setGeometry(QtCore.QRect(280, 320, 75, 71))
        self.channel2_button.setObjectName("channel2_button")
        self.channel3_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel3_button.setGeometry(QtCore.QRect(390, 320, 75, 71))
        self.channel3_button.setObjectName("channel3_button")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 440, 16, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 440, 16, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 440, 16, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.screen = QtWidgets.QLabel(parent=self.centralwidget)
        self.screen.setGeometry(QtCore.QRect(170, 70, 291, 121))
        self.screen.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.screen.setText("")
        self.screen.setObjectName("screen")
        mute_button.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=mute_button)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 21))
        self.menubar.setObjectName("menubar")
        mute_button.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=mute_button)
        self.statusbar.setObjectName("statusbar")
        mute_button.setStatusBar(self.statusbar)

        self.retranslateUi(mute_button)
        QtCore.QMetaObject.connectSlotsByName(mute_button)

    def retranslateUi(self, mute_button):
        _translate = QtCore.QCoreApplication.translate
        mute_button.setWindowTitle(_translate("mute_button", "MainWindow"))
        self.channel_up.setText(_translate("mute_button", "+"))
        self.channel_down.setText(_translate("mute_button", "-"))
        self.volume_up.setText(_translate("mute_button", "+"))
        self.volume_down.setText(_translate("mute_button", "-"))
        self.channel_label_2.setText(_translate("mute_button", "Volume"))
        self.channel_label.setText(_translate("mute_button", "Channel"))
        self.mute_button_2.setText(_translate("mute_button", "Mute"))
        self.power_button.setText(_translate("mute_button", "Power"))
        self.channel1_button.setText(_translate("mute_button", "1"))
        self.channel2_button.setText(_translate("mute_button", "2"))
        self.channel3_button.setText(_translate("mute_button", "3"))
        self.label.setText(_translate("mute_button", "1"))
        self.label_2.setText(_translate("mute_button", "2"))
        self.label_3.setText(_translate("mute_button", "3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mute_button = QtWidgets.QMainWindow()
    ui = Ui_mute_button()
    ui.setupUi(mute_button)
    mute_button.show()
    sys.exit(app.exec())