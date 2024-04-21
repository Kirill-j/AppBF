# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1000, 600)
        Widget.setStyleSheet(u"\n"
"*{\n"
"	boder: 5px #FF0000; \n"
"	font: 16pt Comic Sans MS;\n"
"	background-color: rgb(85, 85, 85);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#tab_1, #tab_2, #tab_3, #tab_4, #tab_5, #tab_6, #tab_7, #tab_8, #tab_9, #tab_10, #tab_11, #tab_12{\n"
"	border: 3px solid #31363B; \n"
"	padding: 2px;\n"
"	margin:  0px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"	font-size: 13pt;\n"
"	width: 66%;\n"
"	height: 22%;\n"
"	background: transparent;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"	color: rgb(48, 48, 48);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(48, 48, 48);\n"
"	border: 2px solid gray;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"\n"
"QTabBar {\n"
"	qproperty-sizePolicy: [Expanding, Expanding, 0, 0];\n"
"}\n"
"\n"
"#answer_4 {\n"
"	font-size: 30pt\n"
"}")
        Widget.setTabShape(QTabWidget.Triangular)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout = QVBoxLayout(self.tab_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.task_1 = QLabel(self.tab_1)
        self.task_1.setObjectName(u"task_1")
        self.task_1.setWordWrap(True)

        self.verticalLayout.addWidget(self.task_1)

        self.input_text_1 = QLineEdit(self.tab_1)
        self.input_text_1.setObjectName(u"input_text_1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_text_1.sizePolicy().hasHeightForWidth())
        self.input_text_1.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.input_text_1)

        self.button_enter_1 = QPushButton(self.tab_1)
        self.button_enter_1.setObjectName(u"button_enter_1")
        sizePolicy.setHeightForWidth(self.button_enter_1.sizePolicy().hasHeightForWidth())
        self.button_enter_1.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.button_enter_1)

        self.answer_1 = QLabel(self.tab_1)
        self.answer_1.setObjectName(u"answer_1")
        self.answer_1.setWordWrap(True)

        self.verticalLayout.addWidget(self.answer_1)

        Widget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.task_2 = QLabel(self.tab_2)
        self.task_2.setObjectName(u"task_2")
        self.task_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.task_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.input_text_2_1 = QLineEdit(self.tab_2)
        self.input_text_2_1.setObjectName(u"input_text_2_1")
        sizePolicy.setHeightForWidth(self.input_text_2_1.sizePolicy().hasHeightForWidth())
        self.input_text_2_1.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.input_text_2_1)

        self.input_text_2_2 = QLineEdit(self.tab_2)
        self.input_text_2_2.setObjectName(u"input_text_2_2")
        sizePolicy.setHeightForWidth(self.input_text_2_2.sizePolicy().hasHeightForWidth())
        self.input_text_2_2.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.input_text_2_2)

        self.input_text_2_3 = QLineEdit(self.tab_2)
        self.input_text_2_3.setObjectName(u"input_text_2_3")
        sizePolicy.setHeightForWidth(self.input_text_2_3.sizePolicy().hasHeightForWidth())
        self.input_text_2_3.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.input_text_2_3)

        self.verticalSpacer = QSpacerItem(200, 50, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.button_enter_2 = QPushButton(self.tab_2)
        self.button_enter_2.setObjectName(u"button_enter_2")
        sizePolicy.setHeightForWidth(self.button_enter_2.sizePolicy().hasHeightForWidth())
        self.button_enter_2.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.button_enter_2)

        self.answer_2 = QLabel(self.tab_2)
        self.answer_2.setObjectName(u"answer_2")

        self.verticalLayout_2.addWidget(self.answer_2)

        Widget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_3 = QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.task_3 = QLabel(self.tab_3)
        self.task_3.setObjectName(u"task_3")
        self.task_3.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.task_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.input_text_3_1 = QLineEdit(self.tab_3)
        self.input_text_3_1.setObjectName(u"input_text_3_1")
        sizePolicy.setHeightForWidth(self.input_text_3_1.sizePolicy().hasHeightForWidth())
        self.input_text_3_1.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.input_text_3_1)

        self.input_text_3_2 = QLineEdit(self.tab_3)
        self.input_text_3_2.setObjectName(u"input_text_3_2")
        sizePolicy.setHeightForWidth(self.input_text_3_2.sizePolicy().hasHeightForWidth())
        self.input_text_3_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.input_text_3_2)

        self.input_text_3_3 = QLineEdit(self.tab_3)
        self.input_text_3_3.setObjectName(u"input_text_3_3")
        sizePolicy.setHeightForWidth(self.input_text_3_3.sizePolicy().hasHeightForWidth())
        self.input_text_3_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.input_text_3_3)

        self.verticalSpacer_2 = QSpacerItem(150, 50, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.button_enter_3 = QPushButton(self.tab_3)
        self.button_enter_3.setObjectName(u"button_enter_3")
        sizePolicy.setHeightForWidth(self.button_enter_3.sizePolicy().hasHeightForWidth())
        self.button_enter_3.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.button_enter_3)

        self.answer_3 = QLabel(self.tab_3)
        self.answer_3.setObjectName(u"answer_3")

        self.verticalLayout_3.addWidget(self.answer_3)

        Widget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_4 = QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.task_4 = QLabel(self.tab_4)
        self.task_4.setObjectName(u"task_4")
        self.task_4.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.task_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.verticalSpacer_3)

        self.answer_4 = QLabel(self.tab_4)
        self.answer_4.setObjectName(u"answer_4")

        self.horizontalLayout_3.addWidget(self.answer_4)

        self.button_start_4 = QPushButton(self.tab_4)
        self.button_start_4.setObjectName(u"button_start_4")
        sizePolicy.setHeightForWidth(self.button_start_4.sizePolicy().hasHeightForWidth())
        self.button_start_4.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.button_start_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.label_function_4 = QLabel(self.tab_4)
        self.label_function_4.setObjectName(u"label_function_4")

        self.verticalLayout_4.addWidget(self.label_function_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_ans_4_1 = QPushButton(self.tab_4)
        self.btn_ans_4_1.setObjectName(u"btn_ans_4_1")

        self.horizontalLayout_6.addWidget(self.btn_ans_4_1)

        self.btn_ans_4_2 = QPushButton(self.tab_4)
        self.btn_ans_4_2.setObjectName(u"btn_ans_4_2")

        self.horizontalLayout_6.addWidget(self.btn_ans_4_2)

        self.btn_ans_4_3 = QPushButton(self.tab_4)
        self.btn_ans_4_3.setObjectName(u"btn_ans_4_3")

        self.horizontalLayout_6.addWidget(self.btn_ans_4_3)

        self.btn_ans_4_4 = QPushButton(self.tab_4)
        self.btn_ans_4_4.setObjectName(u"btn_ans_4_4")

        self.horizontalLayout_6.addWidget(self.btn_ans_4_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_ans_4_5 = QPushButton(self.tab_4)
        self.btn_ans_4_5.setObjectName(u"btn_ans_4_5")

        self.horizontalLayout_7.addWidget(self.btn_ans_4_5)

        self.btn_ans_4_6 = QPushButton(self.tab_4)
        self.btn_ans_4_6.setObjectName(u"btn_ans_4_6")

        self.horizontalLayout_7.addWidget(self.btn_ans_4_6)

        self.btn_ans_4_7 = QPushButton(self.tab_4)
        self.btn_ans_4_7.setObjectName(u"btn_ans_4_7")

        self.horizontalLayout_7.addWidget(self.btn_ans_4_7)

        self.btn_ans_4_8 = QPushButton(self.tab_4)
        self.btn_ans_4_8.setObjectName(u"btn_ans_4_8")

        self.horizontalLayout_7.addWidget(self.btn_ans_4_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_ans_4_9 = QPushButton(self.tab_4)
        self.btn_ans_4_9.setObjectName(u"btn_ans_4_9")

        self.horizontalLayout_8.addWidget(self.btn_ans_4_9)

        self.btn_ans_4_10 = QPushButton(self.tab_4)
        self.btn_ans_4_10.setObjectName(u"btn_ans_4_10")

        self.horizontalLayout_8.addWidget(self.btn_ans_4_10)

        self.btn_ans_4_11 = QPushButton(self.tab_4)
        self.btn_ans_4_11.setObjectName(u"btn_ans_4_11")

        self.horizontalLayout_8.addWidget(self.btn_ans_4_11)

        self.btn_ans_4_12 = QPushButton(self.tab_4)
        self.btn_ans_4_12.setObjectName(u"btn_ans_4_12")

        self.horizontalLayout_8.addWidget(self.btn_ans_4_12)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_ans_4_13 = QPushButton(self.tab_4)
        self.btn_ans_4_13.setObjectName(u"btn_ans_4_13")

        self.horizontalLayout_9.addWidget(self.btn_ans_4_13)

        self.btn_ans_4_14 = QPushButton(self.tab_4)
        self.btn_ans_4_14.setObjectName(u"btn_ans_4_14")

        self.horizontalLayout_9.addWidget(self.btn_ans_4_14)

        self.btn_ans_4_15 = QPushButton(self.tab_4)
        self.btn_ans_4_15.setObjectName(u"btn_ans_4_15")

        self.horizontalLayout_9.addWidget(self.btn_ans_4_15)

        self.btn_ans_4_16 = QPushButton(self.tab_4)
        self.btn_ans_4_16.setObjectName(u"btn_ans_4_16")

        self.horizontalLayout_9.addWidget(self.btn_ans_4_16)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        Widget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_5 = QVBoxLayout(self.tab_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.button_enter_5 = QPushButton(self.tab_5)
        self.button_enter_5.setObjectName(u"button_enter_5")

        self.verticalLayout_5.addWidget(self.button_enter_5)

        self.label_5 = QLabel(self.tab_5)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)

        Widget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_6 = QVBoxLayout(self.tab_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.task_6 = QLabel(self.tab_6)
        self.task_6.setObjectName(u"task_6")
        self.task_6.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.task_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_function_6 = QLabel(self.tab_6)
        self.label_function_6.setObjectName(u"label_function_6")

        self.horizontalLayout_10.addWidget(self.label_function_6)

        self.button_start_6 = QPushButton(self.tab_6)
        self.button_start_6.setObjectName(u"button_start_6")
        sizePolicy.setHeightForWidth(self.button_start_6.sizePolicy().hasHeightForWidth())
        self.button_start_6.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.button_start_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.input_text_6 = QLineEdit(self.tab_6)
        self.input_text_6.setObjectName(u"input_text_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.input_text_6.sizePolicy().hasHeightForWidth())
        self.input_text_6.setSizePolicy(sizePolicy1)

        self.verticalLayout_6.addWidget(self.input_text_6)

        self.button_enter_6 = QPushButton(self.tab_6)
        self.button_enter_6.setObjectName(u"button_enter_6")
        sizePolicy.setHeightForWidth(self.button_enter_6.sizePolicy().hasHeightForWidth())
        self.button_enter_6.setSizePolicy(sizePolicy)

        self.verticalLayout_6.addWidget(self.button_enter_6)

        self.answer_6 = QLabel(self.tab_6)
        self.answer_6.setObjectName(u"answer_6")

        self.verticalLayout_6.addWidget(self.answer_6)

        Widget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_8 = QVBoxLayout(self.tab_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.task_7 = QLabel(self.tab_7)
        self.task_7.setObjectName(u"task_7")
        self.task_7.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.task_7)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_function_7 = QLabel(self.tab_7)
        self.label_function_7.setObjectName(u"label_function_7")

        self.horizontalLayout_11.addWidget(self.label_function_7)

        self.button_start_7 = QPushButton(self.tab_7)
        self.button_start_7.setObjectName(u"button_start_7")
        sizePolicy.setHeightForWidth(self.button_start_7.sizePolicy().hasHeightForWidth())
        self.button_start_7.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.button_start_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.input_text_7 = QLineEdit(self.tab_7)
        self.input_text_7.setObjectName(u"input_text_7")
        sizePolicy1.setHeightForWidth(self.input_text_7.sizePolicy().hasHeightForWidth())
        self.input_text_7.setSizePolicy(sizePolicy1)

        self.verticalLayout_8.addWidget(self.input_text_7)

        self.button_enter_7 = QPushButton(self.tab_7)
        self.button_enter_7.setObjectName(u"button_enter_7")
        sizePolicy.setHeightForWidth(self.button_enter_7.sizePolicy().hasHeightForWidth())
        self.button_enter_7.setSizePolicy(sizePolicy)

        self.verticalLayout_8.addWidget(self.button_enter_7)

        self.answer_7 = QLabel(self.tab_7)
        self.answer_7.setObjectName(u"answer_7")

        self.verticalLayout_8.addWidget(self.answer_7)

        Widget.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_9 = QVBoxLayout(self.tab_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.task_8 = QLabel(self.tab_8)
        self.task_8.setObjectName(u"task_8")
        self.task_8.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.task_8)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")

        self.verticalLayout_9.addLayout(self.horizontalLayout_12)

        self.input_text_8 = QLineEdit(self.tab_8)
        self.input_text_8.setObjectName(u"input_text_8")
        sizePolicy1.setHeightForWidth(self.input_text_8.sizePolicy().hasHeightForWidth())
        self.input_text_8.setSizePolicy(sizePolicy1)

        self.verticalLayout_9.addWidget(self.input_text_8)

        self.button_enter_8 = QPushButton(self.tab_8)
        self.button_enter_8.setObjectName(u"button_enter_8")
        sizePolicy.setHeightForWidth(self.button_enter_8.sizePolicy().hasHeightForWidth())
        self.button_enter_8.setSizePolicy(sizePolicy)

        self.verticalLayout_9.addWidget(self.button_enter_8)

        self.answer_8 = QLabel(self.tab_8)
        self.answer_8.setObjectName(u"answer_8")

        self.verticalLayout_9.addWidget(self.answer_8)

        Widget.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.verticalLayout_10 = QVBoxLayout(self.tab_9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.task_9 = QLabel(self.tab_9)
        self.task_9.setObjectName(u"task_9")
        self.task_9.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.task_9)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")

        self.verticalLayout_10.addLayout(self.horizontalLayout_13)

        self.input_text_9 = QLineEdit(self.tab_9)
        self.input_text_9.setObjectName(u"input_text_9")
        sizePolicy1.setHeightForWidth(self.input_text_9.sizePolicy().hasHeightForWidth())
        self.input_text_9.setSizePolicy(sizePolicy1)

        self.verticalLayout_10.addWidget(self.input_text_9)

        self.button_enter_9 = QPushButton(self.tab_9)
        self.button_enter_9.setObjectName(u"button_enter_9")
        sizePolicy.setHeightForWidth(self.button_enter_9.sizePolicy().hasHeightForWidth())
        self.button_enter_9.setSizePolicy(sizePolicy)

        self.verticalLayout_10.addWidget(self.button_enter_9)

        self.answer_9 = QLabel(self.tab_9)
        self.answer_9.setObjectName(u"answer_9")

        self.verticalLayout_10.addWidget(self.answer_9)

        Widget.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        Widget.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        Widget.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        Widget.addTab(self.tab_12, "")

        self.retranslateUi(Widget)

        Widget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Boolean Functions", None))
        self.task_1.setText(QCoreApplication.translate("Widget", u"\u041d\u0430 \u0432\u0445\u043e\u0434 \u2014 \u0447\u0438\u0441\u043b\u043e n, \u043d\u0430 \u0432\u044b\u0445\u043e\u0434 \u2014 \u0431\u0443\u043b\u0435\u0432\u0430 \u0444\u0443\u043d\u043a\u0446\u0438\u044f \u043e\u0442 n \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.input_text_1.setPlaceholderText(QCoreApplication.translate("Widget", u"n", None))
        self.button_enter_1.setText(QCoreApplication.translate("Widget", u"Enter", None))
        self.answer_1.setText(QCoreApplication.translate("Widget", u"Answer: ", None))
        Widget.setTabText(Widget.indexOf(self.tab_1), QCoreApplication.translate("Widget", u"1", None))
        self.task_2.setText(QCoreApplication.translate("Widget", u"\u041d\u0430 \u0432\u0445\u043e\u0434 \u2014 \u0432\u0435\u043a\u0442\u043e\u0440 \u0444\u0443\u043d\u043a\u0446\u0438\u0438, 0 \u0438\u043b\u0438 1, \u043d\u043e\u043c\u0435\u0440 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442\u0430, \u043d\u0430 \u0432\u044b\u0445\u043e\u0434 \u2014 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0430\u044f \u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u0430\u044f", None))
        self.input_text_2_1.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0412\u0435\u043a\u0442\u043e\u0440 \u0444\u0443\u043d\u043a\u0446\u0438\u0438", None))
        self.input_text_2_2.setPlaceholderText(QCoreApplication.translate("Widget", u"0 \u0438\u043b\u0438 1", None))
        self.input_text_2_3.setPlaceholderText(QCoreApplication.translate("Widget", u"\u041d\u043e\u043c\u0435\u0440 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442\u0430", None))
        self.button_enter_2.setText(QCoreApplication.translate("Widget", u"Enter", None))
        self.answer_2.setText(QCoreApplication.translate("Widget", u"Answer: ", None))
        Widget.setTabText(Widget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"2", None))
        self.task_3.setText(QCoreApplication.translate("Widget", u"\u041d\u0430 \u0432\u0445\u043e\u0434 \u2014 \u0434\u0432\u0430 \u0432\u0435\u043a\u0442\u043e\u0440\u0430 (\u044d\u0442\u043e \u043d\u0443\u043b\u0435\u0432\u0430\u044f \u0438 \u0435\u0434\u0438\u043d\u0438\u0447\u043d\u0430\u044f \u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u044b\u0435 \u0444\u0443\u043d\u043a\u0446\u0438\u0438 \u043f\u043e \u043d\u0435\u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442\u0443), \u043d\u043e\u043c\u0435\u0440 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442\u0430, \u043d\u0430 \u0432\u044b\u0445\u043e\u0434 \u2014 \u0432\u0435\u043a\u0442\u043e\u0440 \u0444\u0443\u043d\u043a\u0446\u0438\u0438", None))
        self.input_text_3_1.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0412\u0435\u043a\u0442\u043e\u0440 \u0444\u0443\u043d\u043a\u0446\u0438\u0438(0)", None))
        self.input_text_3_2.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0412\u0435\u043a\u0442\u043e\u0440 \u0444\u0443\u043d\u043a\u0446\u0438\u0438(1)", None))
        self.input_text_3_3.setPlaceholderText(QCoreApplication.translate("Widget", u"\u041d\u043e\u043c\u0435\u0440 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442\u0430", None))
        self.button_enter_3.setText(QCoreApplication.translate("Widget", u"Enter", None))
        self.answer_3.setText(QCoreApplication.translate("Widget", u"Answer: ", None))
        Widget.setTabText(Widget.indexOf(self.tab_3), QCoreApplication.translate("Widget", u"3", None))
        self.task_4.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u00ab\u0438\u043c\u044f\u00bb \u0444\u0443\u043d\u043a\u0446\u0438\u0438 \u043e\u0442 \u0434\u0432\u0443\u0445 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.answer_4.setText("")
        self.button_start_4.setText(QCoreApplication.translate("Widget", u"Start", None))
        self.label_function_4.setText("")
        self.btn_ans_4_1.setText("")
        self.btn_ans_4_2.setText("")
        self.btn_ans_4_3.setText("")
        self.btn_ans_4_4.setText("")
        self.btn_ans_4_5.setText("")
        self.btn_ans_4_6.setText("")
        self.btn_ans_4_7.setText("")
        self.btn_ans_4_8.setText("")
        self.btn_ans_4_9.setText("")
        self.btn_ans_4_10.setText("")
        self.btn_ans_4_11.setText("")
        self.btn_ans_4_12.setText("")
        self.btn_ans_4_13.setText("")
        self.btn_ans_4_14.setText("")
        self.btn_ans_4_15.setText("")
        self.btn_ans_4_16.setText("")
        Widget.setTabText(Widget.indexOf(self.tab_4), QCoreApplication.translate("Widget", u"4", None))
        self.button_enter_5.setText(QCoreApplication.translate("Widget", u"\u041d\u0430\u0436\u043c\u0438 \u043c\u0435\u043d\u044f", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        Widget.setTabText(Widget.indexOf(self.tab_5), QCoreApplication.translate("Widget", u"5", None))
        self.task_6.setText(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0414\u041d\u0424 \u0444\u0443\u043d\u043a\u0446\u0438\u0438", None))
        self.label_function_6.setText("")
        self.button_start_6.setText(QCoreApplication.translate("Widget", u"Start", None))
        self.input_text_6.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0414\u041d\u0424 \u0444\u0443\u043d\u043a\u0446\u0438\u0438", None))
        self.button_enter_6.setText(QCoreApplication.translate("Widget", u"Enter", None))
        self.answer_6.setText("")
        Widget.setTabText(Widget.indexOf(self.tab_6), QCoreApplication.translate("Widget", u"6", None))
        self.task_7.setText(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u041a\u041d\u0424 \u0444\u0443\u043d\u043a\u0446\u0438\u0438", None))
        self.label_function_7.setText("")
        self.button_start_7.setText(QCoreApplication.translate("Widget", u"Start", None))
        self.input_text_7.setPlaceholderText(QCoreApplication.translate("Widget", u"\u041a\u041d\u0424 \u0444\u0443\u043d\u043a\u0446\u0438\u0438", None))
        self.button_enter_7.setText(QCoreApplication.translate("Widget", u"Enter", None))
        self.answer_7.setText("")
        Widget.setTabText(Widget.indexOf(self.tab_7), QCoreApplication.translate("Widget", u"7", None))
        self.task_8.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0421\u0414\u041d\u0424. \u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0435\u043a\u0442\u043e\u0440 \u0444\u0443\u043d\u043a\u0446\u0438\u0438:", None))
        self.input_text_8.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0412\u0435\u043a\u0442\u043e\u0440 \u0444\u0443\u043d\u043a\u0446\u0438\u0438", None))
        self.button_enter_8.setText(QCoreApplication.translate("Widget", u"Enter", None))
        self.answer_8.setText(QCoreApplication.translate("Widget", u"PDNF: ", None))
        Widget.setTabText(Widget.indexOf(self.tab_8), QCoreApplication.translate("Widget", u"8", None))
        self.task_9.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0421\u041a\u041d\u0424. \u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0435\u043a\u0442\u043e\u0440 \u0444\u0443\u043d\u043a\u0446\u0438\u0438:", None))
        self.input_text_9.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0412\u0435\u043a\u0442\u043e\u0440 \u0444\u0443\u043d\u043a\u0446\u0438\u0438", None))
        self.button_enter_9.setText(QCoreApplication.translate("Widget", u"Enter", None))
        self.answer_9.setText(QCoreApplication.translate("Widget", u"PCNF: ", None))
        Widget.setTabText(Widget.indexOf(self.tab_9), QCoreApplication.translate("Widget", u"9", None))
        Widget.setTabText(Widget.indexOf(self.tab_10), QCoreApplication.translate("Widget", u"10", None))
        Widget.setTabText(Widget.indexOf(self.tab_11), QCoreApplication.translate("Widget", u"11", None))
        Widget.setTabText(Widget.indexOf(self.tab_12), QCoreApplication.translate("Widget", u"12", None))
    # retranslateUi

