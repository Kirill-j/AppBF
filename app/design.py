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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1000, 500)
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
"#answer_4, #label_function_4 {\n"
"	font-size: 30pt\n"
"}")
        Widget.setTabShape(QTabWidget.TabShape.Triangular)
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
        self.input_text_1.setMaximumSize(QSize(50, 16777215))

        self.verticalLayout.addWidget(self.input_text_1, 0, Qt.AlignmentFlag.AlignLeft)

        self.button_enter_1 = QPushButton(self.tab_1)
        self.button_enter_1.setObjectName(u"button_enter_1")

        self.verticalLayout.addWidget(self.button_enter_1, 0, Qt.AlignmentFlag.AlignLeft)

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

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.input_text_2_1 = QLineEdit(self.tab_2)
        self.input_text_2_1.setObjectName(u"input_text_2_1")

        self.verticalLayout_5.addWidget(self.input_text_2_1, 0, Qt.AlignmentFlag.AlignLeft)

        self.input_text_2_3 = QLineEdit(self.tab_2)
        self.input_text_2_3.setObjectName(u"input_text_2_3")

        self.verticalLayout_5.addWidget(self.input_text_2_3, 0, Qt.AlignmentFlag.AlignLeft)

        self.input_text_2_2 = QLineEdit(self.tab_2)
        self.input_text_2_2.setObjectName(u"input_text_2_2")

        self.verticalLayout_5.addWidget(self.input_text_2_2, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_2.addLayout(self.verticalLayout_5)

        self.button_enter_2 = QPushButton(self.tab_2)
        self.button_enter_2.setObjectName(u"button_enter_2")

        self.verticalLayout_2.addWidget(self.button_enter_2, 0, Qt.AlignmentFlag.AlignLeft)

        self.answer_2 = QLabel(self.tab_2)
        self.answer_2.setObjectName(u"answer_2")
        self.answer_2.setWordWrap(True)

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

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.input_text_3_3 = QLineEdit(self.tab_3)
        self.input_text_3_3.setObjectName(u"input_text_3_3")

        self.verticalLayout_4.addWidget(self.input_text_3_3, 0, Qt.AlignmentFlag.AlignLeft)

        self.input_text_3_1 = QLineEdit(self.tab_3)
        self.input_text_3_1.setObjectName(u"input_text_3_1")

        self.verticalLayout_4.addWidget(self.input_text_3_1, 0, Qt.AlignmentFlag.AlignLeft)

        self.input_text_3_2 = QLineEdit(self.tab_3)
        self.input_text_3_2.setObjectName(u"input_text_3_2")

        self.verticalLayout_4.addWidget(self.input_text_3_2, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.button_enter_3 = QPushButton(self.tab_3)
        self.button_enter_3.setObjectName(u"button_enter_3")

        self.verticalLayout_3.addWidget(self.button_enter_3, 0, Qt.AlignmentFlag.AlignLeft)

        self.answer_3 = QLabel(self.tab_3)
        self.answer_3.setObjectName(u"answer_3")
        self.answer_3.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.answer_3)

        Widget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_6 = QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.task_4 = QLabel(self.tab_4)
        self.task_4.setObjectName(u"task_4")
        self.task_4.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.task_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 50)
        self.label_function_4 = QLabel(self.tab_4)
        self.label_function_4.setObjectName(u"label_function_4")
        self.label_function_4.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.label_function_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.answer_4 = QLabel(self.tab_4)
        self.answer_4.setObjectName(u"answer_4")
        self.answer_4.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.answer_4)

        self.button_start_4 = QPushButton(self.tab_4)
        self.button_start_4.setObjectName(u"button_start_4")

        self.horizontalLayout_5.addWidget(self.button_start_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_ans_4_1 = QPushButton(self.tab_4)
        self.btn_ans_4_1.setObjectName(u"btn_ans_4_1")

        self.horizontalLayout.addWidget(self.btn_ans_4_1)

        self.btn_ans_4_2 = QPushButton(self.tab_4)
        self.btn_ans_4_2.setObjectName(u"btn_ans_4_2")

        self.horizontalLayout.addWidget(self.btn_ans_4_2)

        self.btn_ans_4_3 = QPushButton(self.tab_4)
        self.btn_ans_4_3.setObjectName(u"btn_ans_4_3")

        self.horizontalLayout.addWidget(self.btn_ans_4_3)

        self.btn_ans_4_4 = QPushButton(self.tab_4)
        self.btn_ans_4_4.setObjectName(u"btn_ans_4_4")

        self.horizontalLayout.addWidget(self.btn_ans_4_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_ans_4_5 = QPushButton(self.tab_4)
        self.btn_ans_4_5.setObjectName(u"btn_ans_4_5")

        self.horizontalLayout_2.addWidget(self.btn_ans_4_5)

        self.btn_ans_4_6 = QPushButton(self.tab_4)
        self.btn_ans_4_6.setObjectName(u"btn_ans_4_6")

        self.horizontalLayout_2.addWidget(self.btn_ans_4_6)

        self.btn_ans_4_7 = QPushButton(self.tab_4)
        self.btn_ans_4_7.setObjectName(u"btn_ans_4_7")

        self.horizontalLayout_2.addWidget(self.btn_ans_4_7)

        self.btn_ans_4_8 = QPushButton(self.tab_4)
        self.btn_ans_4_8.setObjectName(u"btn_ans_4_8")

        self.horizontalLayout_2.addWidget(self.btn_ans_4_8)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_ans_4_9 = QPushButton(self.tab_4)
        self.btn_ans_4_9.setObjectName(u"btn_ans_4_9")

        self.horizontalLayout_3.addWidget(self.btn_ans_4_9)

        self.btn_ans_4_10 = QPushButton(self.tab_4)
        self.btn_ans_4_10.setObjectName(u"btn_ans_4_10")

        self.horizontalLayout_3.addWidget(self.btn_ans_4_10)

        self.btn_ans_4_11 = QPushButton(self.tab_4)
        self.btn_ans_4_11.setObjectName(u"btn_ans_4_11")

        self.horizontalLayout_3.addWidget(self.btn_ans_4_11)

        self.btn_ans_4_12 = QPushButton(self.tab_4)
        self.btn_ans_4_12.setObjectName(u"btn_ans_4_12")

        self.horizontalLayout_3.addWidget(self.btn_ans_4_12)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_ans_4_13 = QPushButton(self.tab_4)
        self.btn_ans_4_13.setObjectName(u"btn_ans_4_13")

        self.horizontalLayout_4.addWidget(self.btn_ans_4_13)

        self.btn_ans_4_14 = QPushButton(self.tab_4)
        self.btn_ans_4_14.setObjectName(u"btn_ans_4_14")

        self.horizontalLayout_4.addWidget(self.btn_ans_4_14)

        self.btn_ans_4_15 = QPushButton(self.tab_4)
        self.btn_ans_4_15.setObjectName(u"btn_ans_4_15")

        self.horizontalLayout_4.addWidget(self.btn_ans_4_15)

        self.btn_ans_4_16 = QPushButton(self.tab_4)
        self.btn_ans_4_16.setObjectName(u"btn_ans_4_16")

        self.horizontalLayout_4.addWidget(self.btn_ans_4_16)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        Widget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_15 = QVBoxLayout(self.tab_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.task_5 = QLabel(self.tab_5)
        self.task_5.setObjectName(u"task_5")
        self.task_5.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.task_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.button_start_5 = QPushButton(self.tab_5)
        self.button_start_5.setObjectName(u"button_start_5")

        self.verticalLayout_14.addWidget(self.button_start_5, 0, Qt.AlignmentFlag.AlignLeft)

        self.button_enter_5 = QPushButton(self.tab_5)
        self.button_enter_5.setObjectName(u"button_enter_5")

        self.verticalLayout_14.addWidget(self.button_enter_5, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_9.addLayout(self.verticalLayout_14)

        self.label_5_func = QLabel(self.tab_5)
        self.label_5_func.setObjectName(u"label_5_func")

        self.horizontalLayout_9.addWidget(self.label_5_func, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_9.setStretch(1, 1)

        self.verticalLayout_15.addLayout(self.horizontalLayout_9)

        self.answer_5 = QLabel(self.tab_5)
        self.answer_5.setObjectName(u"answer_5")
        self.answer_5.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.answer_5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.group_box_x = QGroupBox(self.tab_5)
        self.group_box_x.setObjectName(u"group_box_x")
        self.verticalLayout_11 = QVBoxLayout(self.group_box_x)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.radio_button_5_x_fict = QRadioButton(self.group_box_x)
        self.radio_button_5_x_fict.setObjectName(u"radio_button_5_x_fict")

        self.verticalLayout_11.addWidget(self.radio_button_5_x_fict)

        self.radio_button_5_x_su = QRadioButton(self.group_box_x)
        self.radio_button_5_x_su.setObjectName(u"radio_button_5_x_su")

        self.verticalLayout_11.addWidget(self.radio_button_5_x_su)


        self.horizontalLayout_8.addWidget(self.group_box_x)

        self.group_box_y = QGroupBox(self.tab_5)
        self.group_box_y.setObjectName(u"group_box_y")
        self.verticalLayout_12 = QVBoxLayout(self.group_box_y)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.radio_button_5_y_fict = QRadioButton(self.group_box_y)
        self.radio_button_5_y_fict.setObjectName(u"radio_button_5_y_fict")

        self.verticalLayout_12.addWidget(self.radio_button_5_y_fict)

        self.radio_button_5_y_su = QRadioButton(self.group_box_y)
        self.radio_button_5_y_su.setObjectName(u"radio_button_5_y_su")

        self.verticalLayout_12.addWidget(self.radio_button_5_y_su)


        self.horizontalLayout_8.addWidget(self.group_box_y)

        self.group_box_z = QGroupBox(self.tab_5)
        self.group_box_z.setObjectName(u"group_box_z")
        self.verticalLayout_13 = QVBoxLayout(self.group_box_z)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.radio_button_5_z_fict = QRadioButton(self.group_box_z)
        self.radio_button_5_z_fict.setObjectName(u"radio_button_5_z_fict")

        self.verticalLayout_13.addWidget(self.radio_button_5_z_fict)

        self.radio_button_5_z_su = QRadioButton(self.group_box_z)
        self.radio_button_5_z_su.setObjectName(u"radio_button_5_z_su")

        self.verticalLayout_13.addWidget(self.radio_button_5_z_su)


        self.horizontalLayout_8.addWidget(self.group_box_z)


        self.verticalLayout_15.addLayout(self.horizontalLayout_8)

        Widget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_7 = QVBoxLayout(self.tab_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.task_6 = QLabel(self.tab_6)
        self.task_6.setObjectName(u"task_6")
        self.task_6.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.task_6)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_function_6 = QLabel(self.tab_6)
        self.label_function_6.setObjectName(u"label_function_6")
        self.label_function_6.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.label_function_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_start_6 = QPushButton(self.tab_6)
        self.button_start_6.setObjectName(u"button_start_6")

        self.horizontalLayout_6.addWidget(self.button_start_6, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.input_text_6 = QLineEdit(self.tab_6)
        self.input_text_6.setObjectName(u"input_text_6")
        self.input_text_6.setMinimumSize(QSize(400, 0))

        self.verticalLayout_7.addWidget(self.input_text_6, 0, Qt.AlignmentFlag.AlignLeft)

        self.button_enter_6 = QPushButton(self.tab_6)
        self.button_enter_6.setObjectName(u"button_enter_6")

        self.verticalLayout_7.addWidget(self.button_enter_6, 0, Qt.AlignmentFlag.AlignLeft)

        self.answer_6 = QLabel(self.tab_6)
        self.answer_6.setObjectName(u"answer_6")
        self.answer_6.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.answer_6)

        Widget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_8 = QVBoxLayout(self.tab_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.task_7 = QLabel(self.tab_7)
        self.task_7.setObjectName(u"task_7")
        self.task_7.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.task_7)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_function_7 = QLabel(self.tab_7)
        self.label_function_7.setObjectName(u"label_function_7")
        self.label_function_7.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.label_function_7, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_start_7 = QPushButton(self.tab_7)
        self.button_start_7.setObjectName(u"button_start_7")

        self.horizontalLayout_7.addWidget(self.button_start_7, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.input_text_7 = QLineEdit(self.tab_7)
        self.input_text_7.setObjectName(u"input_text_7")
        self.input_text_7.setMinimumSize(QSize(400, 0))

        self.verticalLayout_8.addWidget(self.input_text_7, 0, Qt.AlignmentFlag.AlignLeft)

        self.button_enter_7 = QPushButton(self.tab_7)
        self.button_enter_7.setObjectName(u"button_enter_7")

        self.verticalLayout_8.addWidget(self.button_enter_7, 0, Qt.AlignmentFlag.AlignLeft)

        self.answer_7 = QLabel(self.tab_7)
        self.answer_7.setObjectName(u"answer_7")
        self.answer_7.setWordWrap(True)

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

        self.input_text_8 = QLineEdit(self.tab_8)
        self.input_text_8.setObjectName(u"input_text_8")

        self.verticalLayout_9.addWidget(self.input_text_8, 0, Qt.AlignmentFlag.AlignLeft)

        self.button_enter_8 = QPushButton(self.tab_8)
        self.button_enter_8.setObjectName(u"button_enter_8")

        self.verticalLayout_9.addWidget(self.button_enter_8, 0, Qt.AlignmentFlag.AlignLeft)

        self.answer_8 = QLabel(self.tab_8)
        self.answer_8.setObjectName(u"answer_8")
        self.answer_8.setWordWrap(True)

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

        self.input_text_9 = QLineEdit(self.tab_9)
        self.input_text_9.setObjectName(u"input_text_9")

        self.verticalLayout_10.addWidget(self.input_text_9, 0, Qt.AlignmentFlag.AlignLeft)

        self.button_enter_9 = QPushButton(self.tab_9)
        self.button_enter_9.setObjectName(u"button_enter_9")

        self.verticalLayout_10.addWidget(self.button_enter_9, 0, Qt.AlignmentFlag.AlignLeft)

        self.answer_9 = QLabel(self.tab_9)
        self.answer_9.setObjectName(u"answer_9")
        self.answer_9.setWordWrap(True)

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
        self.input_text_2_3.setPlaceholderText(QCoreApplication.translate("Widget", u"\u041d\u043e\u043c\u0435\u0440 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442\u0430", None))
        self.input_text_2_2.setPlaceholderText(QCoreApplication.translate("Widget", u"0 \u0438\u043b\u0438 1", None))
        self.button_enter_2.setText(QCoreApplication.translate("Widget", u"Enter", None))
        self.answer_2.setText(QCoreApplication.translate("Widget", u"Answer: ", None))
        Widget.setTabText(Widget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"2", None))
        self.task_3.setText(QCoreApplication.translate("Widget", u"\u041d\u0430 \u0432\u0445\u043e\u0434 \u2014 \u0434\u0432\u0430 \u0432\u0435\u043a\u0442\u043e\u0440\u0430 (\u044d\u0442\u043e \u043d\u0443\u043b\u0435\u0432\u0430\u044f \u0438 \u0435\u0434\u0438\u043d\u0438\u0447\u043d\u0430\u044f \u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u044b\u0435 \u0444\u0443\u043d\u043a\u0446\u0438\u0438 \u043f\u043e \u043d\u0435\u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442\u0443), \u043d\u043e\u043c\u0435\u0440 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442\u0430, \u043d\u0430 \u0432\u044b\u0445\u043e\u0434 \u2014 \u0432\u0435\u043a\u0442\u043e\u0440 \u0444\u0443\u043d\u043a\u0446\u0438\u0438", None))
        self.input_text_3_3.setPlaceholderText(QCoreApplication.translate("Widget", u"\u041d\u043e\u043c\u0435\u0440 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442\u0430", None))
        self.input_text_3_1.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0412\u0435\u043a\u0442\u043e\u0440 \u0444\u0443\u043d\u043a\u0446\u0438\u0438(0)", None))
        self.input_text_3_2.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0412\u0435\u043a\u0442\u043e\u0440 \u0444\u0443\u043d\u043a\u0446\u0438\u0438(1)", None))
        self.button_enter_3.setText(QCoreApplication.translate("Widget", u"Enter", None))
        self.answer_3.setText(QCoreApplication.translate("Widget", u"Answer: ", None))
        Widget.setTabText(Widget.indexOf(self.tab_3), QCoreApplication.translate("Widget", u"3", None))
        self.task_4.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u00ab\u0438\u043c\u044f\u00bb \u0444\u0443\u043d\u043a\u0446\u0438\u0438 \u043e\u0442 \u0434\u0432\u0443\u0445 \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.label_function_4.setText("")
        self.answer_4.setText("")
        self.button_start_4.setText(QCoreApplication.translate("Widget", u"Start", None))
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
        self.task_5.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0435 \u0438 \u0444\u0438\u043a\u0442\u0438\u0432\u043d\u044b\u0435 \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0435", None))
        self.button_start_5.setText(QCoreApplication.translate("Widget", u"Start", None))
        self.button_enter_5.setText(QCoreApplication.translate("Widget", u"Enter", None))
        self.label_5_func.setText(QCoreApplication.translate("Widget", u"\u0412\u0435\u043a\u0442\u043e\u0440", None))
        self.answer_5.setText(QCoreApplication.translate("Widget", u"answer", None))
        self.group_box_x.setTitle(QCoreApplication.translate("Widget", u"X", None))
        self.radio_button_5_x_fict.setText(QCoreApplication.translate("Widget", u"\u0424\u0438\u043a\u0442\u0438\u0432\u043d\u0430\u044f", None))
        self.radio_button_5_x_su.setText(QCoreApplication.translate("Widget", u"\u0421\u0443\u0449\u0435\u0442\u0432\u0435\u043d\u043d\u0430\u044f", None))
        self.group_box_y.setTitle(QCoreApplication.translate("Widget", u"Y", None))
        self.radio_button_5_y_fict.setText(QCoreApplication.translate("Widget", u"\u0424\u0438\u043a\u0442\u0438\u0432\u043d\u0430\u044f", None))
        self.radio_button_5_y_su.setText(QCoreApplication.translate("Widget", u"\u0421\u0443\u0449\u0435\u0442\u0432\u0435\u043d\u043d\u0430\u044f", None))
        self.group_box_z.setTitle(QCoreApplication.translate("Widget", u"Z", None))
        self.radio_button_5_z_fict.setText(QCoreApplication.translate("Widget", u"\u0424\u0438\u043a\u0442\u0438\u0432\u043d\u0430\u044f", None))
        self.radio_button_5_z_su.setText(QCoreApplication.translate("Widget", u"\u0421\u0443\u0449\u0435\u0442\u0432\u0435\u043d\u043d\u0430\u044f", None))
        Widget.setTabText(Widget.indexOf(self.tab_5), QCoreApplication.translate("Widget", u"5", None))
        self.task_6.setText(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0414\u041d\u0424 \u0444\u0443\u043d\u043a\u0446\u0438\u0438", None))
        self.label_function_6.setText(QCoreApplication.translate("Widget", u"\u0424\u0443\u043d\u043a\u0446\u0438\u044f", None))
        self.button_start_6.setText(QCoreApplication.translate("Widget", u"Start", None))
        self.input_text_6.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0414\u041d\u0424 \u0444\u0443\u043d\u043a\u0446\u0438\u0438", None))
        self.button_enter_6.setText(QCoreApplication.translate("Widget", u"Enter", None))
        self.answer_6.setText(QCoreApplication.translate("Widget", u"Answer: ", None))
        Widget.setTabText(Widget.indexOf(self.tab_6), QCoreApplication.translate("Widget", u"6", None))
        self.task_7.setText(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u041a\u041d\u0424 \u0444\u0443\u043d\u043a\u0446\u0438\u0438", None))
        self.label_function_7.setText(QCoreApplication.translate("Widget", u"\u0424\u0443\u043d\u043a\u0446\u0438\u044f", None))
        self.button_start_7.setText(QCoreApplication.translate("Widget", u"Start", None))
        self.input_text_7.setPlaceholderText(QCoreApplication.translate("Widget", u"\u041a\u041d\u0424 \u0444\u0443\u043d\u043a\u0446\u0438\u0438", None))
        self.button_enter_7.setText(QCoreApplication.translate("Widget", u"Enter", None))
        self.answer_7.setText(QCoreApplication.translate("Widget", u"Answer: ", None))
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

