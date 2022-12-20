# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'semiautowidget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QVBoxLayout, QWidget)

from mapclientplugins.heartsurfacesemiautosegmenterstep.view.semiautosceneviewerwidget import SemiAutoSceneviewerWidget

class Ui_SemiAutoWidget(object):
    def setupUi(self, SemiAutoWidget):
        if not SemiAutoWidget.objectName():
            SemiAutoWidget.setObjectName(u"SemiAutoWidget")
        SemiAutoWidget.resize(1021, 620)
        self.horizontalLayout = QHBoxLayout(SemiAutoWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(SemiAutoWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.groupBox_4 = QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButtonLoad = QPushButton(self.groupBox_4)
        self.pushButtonLoad.setObjectName(u"pushButtonLoad")

        self.horizontalLayout_8.addWidget(self.pushButtonLoad)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButtonSave = QPushButton(self.groupBox_4)
        self.pushButtonSave.setObjectName(u"pushButtonSave")

        self.horizontalLayout_9.addWidget(self.pushButtonSave)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.line = QFrame(self.groupBox_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButtonContinue = QPushButton(self.groupBox_4)
        self.pushButtonContinue.setObjectName(u"pushButtonContinue")

        self.horizontalLayout_7.addWidget(self.pushButtonContinue)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)


        self.verticalLayout_10.addWidget(self.groupBox_4)

        self.groupBox_6 = QGroupBox(self.groupBox_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout = QVBoxLayout(self.groupBox_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonViewAll = QPushButton(self.groupBox_6)
        self.pushButtonViewAll.setObjectName(u"pushButtonViewAll")

        self.horizontalLayout_2.addWidget(self.pushButtonViewAll)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox_6)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSlider = QSlider(self.groupBox_6)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.horizontalSlider)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_10.addWidget(self.groupBox_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.widgetZinc = SemiAutoSceneviewerWidget(SemiAutoWidget)
        self.widgetZinc.setObjectName(u"widgetZinc")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetZinc.sizePolicy().hasHeightForWidth())
        self.widgetZinc.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.widgetZinc)


        self.retranslateUi(SemiAutoWidget)

        QMetaObject.connectSlotsByName(SemiAutoWidget)
    # setupUi

    def retranslateUi(self, SemiAutoWidget):
        SemiAutoWidget.setWindowTitle(QCoreApplication.translate("SemiAutoWidget", u"Heart Surface", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("SemiAutoWidget", u"Heart Surface Segmenter", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("SemiAutoWidget", u"File", None))
        self.pushButtonLoad.setText(QCoreApplication.translate("SemiAutoWidget", u"Load", None))
        self.pushButtonSave.setText(QCoreApplication.translate("SemiAutoWidget", u"Save", None))
        self.pushButtonContinue.setText(QCoreApplication.translate("SemiAutoWidget", u"Continue", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("SemiAutoWidget", u"View", None))
        self.pushButtonViewAll.setText(QCoreApplication.translate("SemiAutoWidget", u"View All", None))
        self.label_3.setText(QCoreApplication.translate("SemiAutoWidget", u"Image Plane: ", None))
    # retranslateUi

