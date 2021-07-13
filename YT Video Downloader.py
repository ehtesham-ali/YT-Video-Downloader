from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import *
import webbrowser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 284)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.video_type = None

        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(0, 0, 531, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(24)
        self.label_title.setFont(font)
        self.label_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")

        self.entry_link = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_link.setGeometry(QtCore.QRect(40, 60, 451, 21))
        self.entry_link.setObjectName("entry_link")
        self.entry_link.setText("Please Enter a Youtube Link")

        self.button_selectVideo = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: func_selectVideo())
        self.button_selectVideo.setGeometry(QtCore.QRect(40, 100, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.button_selectVideo.setFont(font)
        self.button_selectVideo.setObjectName("button_selectVideo")
        def func_selectVideo():
            self.video_type = 'Video'
            self.label.setText(f'{self.video_type} Link Selected')

        self.button_selectPlaylist = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: func_selectPlaylist())
        self.button_selectPlaylist.setGeometry(QtCore.QRect(220, 100, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.button_selectPlaylist.setFont(font)
        self.button_selectPlaylist.setObjectName("button_selectPlaylist")
        def func_selectPlaylist():
            self.video_type = 'Playlist'
            self.label.setText(f'{self.video_type} Link Selected')

        self.button_selectChannel = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: func_selectChannel())
        self.button_selectChannel.setGeometry(QtCore.QRect(390, 100, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.button_selectChannel.setFont(font)
        self.button_selectChannel.setObjectName("button_selectChannel")
        def func_selectChannel():
            self.video_type = 'Channel'
            self.label.setText(f'{self.video_type} Link Selected')

        self.button_start = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: func_start())
        self.button_start.setGeometry(QtCore.QRect(170, 180, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.button_start.setFont(font)
        self.button_start.setObjectName("button_start")
        def func_start():
            if self.entry_link.text() != "Please Enter a Youtube Link":
                self.button_selectVideo.setEnabled(False)
                self.button_selectPlaylist.setEnabled(False)
                self.button_selectChannel.setEnabled(False)

                if self.video_type == 'Video':
                    self.label.setText('Downloading')
                    try:
                        self.video = YouTube(self.entry_link.text())
                        self.label.setText(f'Downloading {self.video.title}')
                        self.video.streams.first().download()
                        self.button_selectVideo.setEnabled(True)
                        self.button_selectPlaylist.setEnabled(True)
                        self.button_selectChannel.setEnabled(True)
                        self.label.setText('Video Successfully Downloaded!')
                    except:
                        self.label.setText('ERROR: FAILED TO DOWNLOAD VIDEO')
                        self.entry_link.setText('Please Enter a Youtube Link')
                        self.button_selectVideo.setEnabled(True)
                        self.button_selectPlaylist.setEnabled(True)
                        self.button_selectChannel.setEnabled(True)
                
                if self.video_type == 'Playlist':
                    self.label.setText('Downloading')
                    try:
                        self.playlist = Playlist(self.entry_link.text())
                        self.label.setText('Downloading Playlist')
                        
                        for video in self.playlist.videos:
                            self.label.setText(f'Downloading {video.title}')
                            video.streams.first().download()
                        
                        self.button_selectVideo.setEnabled(True)
                        self.button_selectPlaylist.setEnabled(True)
                        self.button_selectChannel.setEnabled(True)
                        self.label.setText('Video Successfully Downloaded!')

                    except:
                        self.label.setText('ERROR: FAILED TO DOWNLOAD VIDEO')
                        self.entry_link.setText('Please Enter a Youtube Link')
                        self.button_selectVideo.setEnabled(True)
                        self.button_selectPlaylist.setEnabled(True)
                        self.button_selectChannel.setEnabled(True)
                
                if self.video_type == 'Channel':
                    self.label.setText('Downloading')
                    try:
                        self.channel = Channel(self.entry_link.text())
                        self.label.setText('Downloading Channel')
                        
                        for video in self.channel.videos:
                            self.label.setText(f'Downloading {video.title}')
                            video.streams.first().download()

                        self.button_selectVideo.setEnabled(True)
                        self.button_selectPlaylist.setEnabled(True)
                        self.button_selectChannel.setEnabled(True)
                        self.label.setText('Video Successfully Downloaded!')

                    except:
                        self.label.setText('ERROR: FAILED TO DOWNLOAD VIDEO')
                        self.entry_link.setText('Please Enter a Youtube Link')
                        self.button_selectVideo.setEnabled(True)
                        self.button_selectPlaylist.setEnabled(True)
                        self.button_selectChannel.setEnabled(True)
            
            else:
                self.label.setText('Enter a Youtube Link Above')
                
        self.button_info = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: func_info())
        self.button_info.setGeometry(QtCore.QRect(500, 250, 21, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.button_info.setFont(font)
        self.button_info.setObjectName("button_info")
        def func_info():
            webbrowser.open('https://www.notion.so/Intro-Briefing-df63b6fc23b94cb7a79079d8a0ddf35b')
            self.label.setText('More Information Page Opened')

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 150, 451, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText('N/A')

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YT Video Downloader"))
        self.label_title.setText(_translate("MainWindow", "YouTube Video Downloader"))
        self.button_selectVideo.setText(_translate("MainWindow", "Video"))
        self.button_selectPlaylist.setText(_translate("MainWindow", "Playlist"))
        self.button_selectChannel.setText(_translate("MainWindow", "Channel"))
        self.button_start.setText(_translate("MainWindow", "Start"))
        self.button_info.setText(_translate("MainWindow", "?"))
        self.label.setText(_translate("MainWindow", "Status: N/A"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
