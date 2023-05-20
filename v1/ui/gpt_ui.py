# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gpt.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QToolBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(602, 750)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setLayoutDirection(Qt.RightToLeft)
        self.actionpin = QAction(MainWindow)
        self.actionpin.setObjectName(u"actionpin")
        self.actionpin.setCheckable(True)
        icon = QIcon()
        icon.addFile(u"../../../../../../design_resource/icon/unpin.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"../../../../../../design_resource/icon/pin.png", QSize(), QIcon.Normal, QIcon.On)
        self.actionpin.setIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.graphicsView = QWebEngineView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setStyleSheet(u"border:px")

        self.verticalLayout.addWidget(self.graphicsView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMaximumSize(QSize(16777215, 18))
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setStyleSheet(u"border: 0px;background:white;")
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QSize(20, 20))
        self.toolBar.setFloatable(True)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionpin)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionpin.setText(QCoreApplication.translate("MainWindow", u"pin", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

