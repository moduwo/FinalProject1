from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from remote import *


class Logic(QMainWindow, Ui_mute_button):
    """Class variables for functions"""
    power_count:int = 0
    volume_up_count:int = 0
    volume_down_count:int = 0
    channel_up_count:int = 0
    channel_down_count:int = 0
    mute_count:int = 0
    min_volume:int = 0
    max_volume:int = 3

    def __init__(self) -> None:
        """Function calls"""
        super().__init__()
        self.setupUi(self)
        self.horizontalSlider.setValue(0)
        self.value = self.horizontalSlider.value()
        self.power_button.clicked.connect(lambda: self.submit())
        self.volume_up.clicked.connect(lambda: self.volumeup())
        self.volume_down.clicked.connect(lambda: self.volumedown())
        self.mute_button_2.clicked.connect(lambda: self.mute())
        self.channel1_button.clicked.connect(lambda: self.show_image1())
        self.channel2_button.clicked.connect(lambda: self.show_image2())
        self.channel3_button.clicked.connect(lambda: self.show_image3())
        self.channel_up.clicked.connect(lambda: self.channelup())
        self.channel_down.clicked.connect(lambda: self.channeldown())


    def submit(self) -> None:
        """Turn TV on or off if power button is clicked"""
        self.horizontalSlider.setValue(0)
        self.power_count += 1
        if self.power_count % 2 != 0:
            print('power is on ')
            self.show_image1()
        if self.power_count % 2 == 0:
            print('Power is off')
            self.screen.setStyleSheet('Background-color: black')
            self.screen.clear()
            self.channel_up_count = 0


    def volumeup(self) -> None:
        """Turn TV volume up by adjusting horizontal slider when the volume up button is clicked"""
        if self.power_count % 2 != 0:
            self.volume_up_count += 1
            if self.horizontalSlider.value() < 50:
                self.horizontalSlider.setValue(50)
                self.value = self.horizontalSlider.value()
            elif self.volume_up_count > 1 :
                self.horizontalSlider.setValue(100)
                self.value = self.horizontalSlider.value()


    def volumedown(self) -> None:
        """Turn TV volume down by adjusting horizontal slier when the volume down button is clicked"""
        if self.power_count % 2 != 0:
            if self.horizontalSlider.value() <= 50:
                self.horizontalSlider.setValue(0)
                self.value = self.horizontalSlider.value()
            elif self.horizontalSlider.value() > 50:
                self.horizontalSlider.setValue(50)
                self.value = self.horizontalSlider.value()



    def mute(self) -> None:
        """TV should be muted or unMuted when the mute button is pressed. When the TV is muted then the volume should be set at 0"""
        if self.power_count % 2 != 0:
            self.mute_count += 1
            if self.mute_count % 2 != 0:
                self.mute_button_2.setText('UnMute')
                self.horizontalSlider.setValue(0)
                self.horizontalSlider.setEnabled(False)
                self.volume_up.setDisabled(True)
                self.volume_down.setDisabled(True)
            else:
                self.mute_button_2.setText('Mute')
                self.volume_up.setDisabled(False)
                self.volume_down.setDisabled(False)
                self.horizontalSlider.setEnabled(True)
                self.horizontalSlider.setValue(self.value)


    def show_image1(self) -> None:
        """Show ABCNEWS image when the TV is on and the channel is set at 1"""
        if self.power_count % 2 != 0:
            self.channel_up_count = 0
            self.channel_down_count = 2
            if self.channel1_button:
                pixmap = QPixmap('Images\\abcnews.png')
                if pixmap.isNull():
                    self.screen.setText('Image not found')
                else:
                    scaled = pixmap.scaled(291, 121, Qt.AspectRatioMode.IgnoreAspectRatio)
                    self.screen.setStyleSheet('Background-color: grey')
                    self.screen.setPixmap(scaled)

                self.screen.repaint()

    def show_image2(self) -> None:
        """SHow CNN image when the TV is on and the channel is set at 1"""
        if self.power_count % 2 != 0:
            self.channel_up_count = 1
            self.channel_down_count = 1
            if self.channel2_button:
                pixmap = QPixmap('Images\\cnnphoto.jpg')
                if pixmap.isNull():
                    self.screen.setText('Image not found')
                else:
                    scaled = pixmap.scaled(291, 121, Qt.AspectRatioMode.IgnoreAspectRatio)
                    self.screen.setStyleSheet('Background-color: black')
                    self.screen.setPixmap(scaled)

                self.screen.repaint()


    def show_image3(self) -> None:
        """Show NBCNEWS image when the TV is on and the channel is set at 3"""
        if self.power_count % 2 != 0:
            self.channel_up_count = 2
            self.channel_down_count = 0
            if self.channel3_button:
                pixmap = QPixmap('Images\\nbcnewschannel.png')
                if pixmap.isNull():
                    self.screen.setText('Image not found')
                else:
                    scaled = pixmap.scaled(291, 121, Qt.AspectRatioMode.KeepAspectRatioByExpanding)
                    self.screen.setStyleSheet('Background-color: white')
                    self.screen.setPixmap(scaled)

                self.screen.repaint()


    def channelup(self) -> None:
        """TV displays the next channel when the channel up button is clicked"""
        if self.power_count % 2 != 0:
            self.channel_up_count += 1
            if self.channel_up_count == 1:
                self.show_image2()
            elif self.channel_up_count == 2:
                self.show_image3()
            elif self.channel_up_count == 3:
                self.show_image1()
                self.channel_up_count = 0


    def channeldown(self) -> None:
        """TV displays the previous channel when the channel down button is clicked"""
        if self.power_count % 2 != 0:
            self.channel_down_count += 1
            if self.channel_down_count == 1:
                self.show_image2()
            elif self.channel_down_count > 1:
                self.show_image1()

















