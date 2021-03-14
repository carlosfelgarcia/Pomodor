# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Repo\Pomodor\ui\pomodor_config_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pomodor_config(object):
    def setupUi(self, pomodor_config):
        pomodor_config.setObjectName("pomodor_config")
        pomodor_config.resize(720, 364)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        pomodor_config.setFont(font)
        self.gridLayout_3 = QtWidgets.QGridLayout(pomodor_config)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(pomodor_config)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(pomodor_config)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.break_time_sb = QtWidgets.QSpinBox(pomodor_config)
        self.break_time_sb.setObjectName("break_time_sb")
        self.gridLayout.addWidget(self.break_time_sb, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(pomodor_config)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.focus_time_sb = QtWidgets.QSpinBox(pomodor_config)
        self.focus_time_sb.setObjectName("focus_time_sb")
        self.gridLayout.addWidget(self.focus_time_sb, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line = QtWidgets.QFrame(pomodor_config)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.quotes_file_txt = QtWidgets.QTextEdit(pomodor_config)
        self.quotes_file_txt.setMaximumSize(QtCore.QSize(16777215, 25))
        self.quotes_file_txt.setObjectName("quotes_file_txt")
        self.gridLayout_2.addWidget(self.quotes_file_txt, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(pomodor_config)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.quotes_search_btn = QtWidgets.QPushButton(pomodor_config)
        self.quotes_search_btn.setObjectName("quotes_search_btn")
        self.gridLayout_2.addWidget(self.quotes_search_btn, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.label_4 = QtWidgets.QLabel(pomodor_config)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.save_btn = QtWidgets.QPushButton(pomodor_config)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout.addWidget(self.save_btn)
        self.cancel_btn = QtWidgets.QPushButton(pomodor_config)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(pomodor_config)
        QtCore.QMetaObject.connectSlotsByName(pomodor_config)

    def retranslateUi(self, pomodor_config):
        _translate = QtCore.QCoreApplication.translate
        pomodor_config.setWindowTitle(_translate("pomodor_config", "Dialog"))
        self.label.setText(_translate("pomodor_config", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Pomodor Configuration</span></p></body></html>"))
        self.label_2.setText(_translate("pomodor_config", "Set focus time (minutes)"))
        self.label_3.setText(_translate("pomodor_config", "Set break time (minutes)"))
        self.label_5.setText(_translate("pomodor_config", "Quotes File"))
        self.quotes_search_btn.setText(_translate("pomodor_config", "Search"))
        self.label_4.setText(_translate("pomodor_config", "<html><head/><body><p><span style=\" font-size:11pt; font-style:italic;\">Note: Time settings will get override if smart function is on</span></p></body></html>"))
        self.save_btn.setText(_translate("pomodor_config", "Save"))
        self.cancel_btn.setText(_translate("pomodor_config", "Cancel"))