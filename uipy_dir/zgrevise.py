# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zgrevise.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1115, 751)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_147 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_147.setFont(font)
        self.label_147.setObjectName("label_147")
        self.verticalLayout_3.addWidget(self.label_147)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_145 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_145.setFont(font)
        self.label_145.setObjectName("label_145")
        self.horizontalLayout_14.addWidget(self.label_145)
        self.lineEdit_113 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_113.setFont(font)
        self.lineEdit_113.setObjectName("lineEdit_113")
        self.horizontalLayout_14.addWidget(self.lineEdit_113)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_148 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_148.setFont(font)
        self.label_148.setObjectName("label_148")
        self.horizontalLayout.addWidget(self.label_148)
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout.addWidget(self.dateEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_143 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_143.setFont(font)
        self.label_143.setObjectName("label_143")
        self.horizontalLayout_13.addWidget(self.label_143)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.widget)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout_13.addWidget(self.dateEdit_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_154 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_154.setFont(font)
        self.label_154.setObjectName("label_154")
        self.horizontalLayout_7.addWidget(self.label_154)
        self.lineEdit_119 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_119.setFont(font)
        self.lineEdit_119.setObjectName("lineEdit_119")
        self.horizontalLayout_7.addWidget(self.lineEdit_119)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_150 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_150.setFont(font)
        self.label_150.setObjectName("label_150")
        self.horizontalLayout_3.addWidget(self.label_150)
        self.lineEdit_115 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_115.setFont(font)
        self.lineEdit_115.setObjectName("lineEdit_115")
        self.horizontalLayout_3.addWidget(self.lineEdit_115)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_144 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_144.setFont(font)
        self.label_144.setObjectName("label_144")
        self.horizontalLayout_12.addWidget(self.label_144)
        self.lineEdit_111 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_111.setFont(font)
        self.lineEdit_111.setObjectName("lineEdit_111")
        self.horizontalLayout_12.addWidget(self.lineEdit_111)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 1)
        self.horizontalLayout_12.setStretch(2, 5)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_142 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_142.setFont(font)
        self.label_142.setObjectName("label_142")
        self.horizontalLayout_10.addWidget(self.label_142)
        self.lineEdit_109 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_109.setFont(font)
        self.lineEdit_109.setObjectName("lineEdit_109")
        self.horizontalLayout_10.addWidget(self.lineEdit_109)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 1)
        self.horizontalLayout_10.setStretch(2, 5)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_146 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_146.setFont(font)
        self.label_146.setObjectName("label_146")
        self.horizontalLayout_11.addWidget(self.label_146)
        self.lineEdit_112 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_112.setFont(font)
        self.lineEdit_112.setObjectName("lineEdit_112")
        self.horizontalLayout_11.addWidget(self.lineEdit_112)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_151 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_151.setFont(font)
        self.label_151.setObjectName("label_151")
        self.horizontalLayout_4.addWidget(self.label_151)
        self.lineEdit_116 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_116.setFont(font)
        self.lineEdit_116.setObjectName("lineEdit_116")
        self.horizontalLayout_4.addWidget(self.lineEdit_116)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_152 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_152.setFont(font)
        self.label_152.setObjectName("label_152")
        self.horizontalLayout_5.addWidget(self.label_152)
        self.lineEdit_117 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_117.setFont(font)
        self.lineEdit_117.setObjectName("lineEdit_117")
        self.horizontalLayout_5.addWidget(self.lineEdit_117)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_153 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_153.setFont(font)
        self.label_153.setObjectName("label_153")
        self.horizontalLayout_6.addWidget(self.label_153)
        self.lineEdit_118 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_118.setFont(font)
        self.lineEdit_118.setObjectName("lineEdit_118")
        self.horizontalLayout_6.addWidget(self.lineEdit_118)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_157 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_157.setFont(font)
        self.label_157.setObjectName("label_157")
        self.horizontalLayout_9.addWidget(self.label_157)
        self.lineEdit_121 = QtWidgets.QLineEdit(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_121.setFont(font)
        self.lineEdit_121.setObjectName("lineEdit_121")
        self.horizontalLayout_9.addWidget(self.lineEdit_121)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 1)
        self.horizontalLayout_9.setStretch(2, 5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_156 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_156.setFont(font)
        self.label_156.setObjectName("label_156")
        self.horizontalLayout_8.addWidget(self.label_156)
        self.lineEdit_120 = QtWidgets.QLineEdit(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_120.setFont(font)
        self.lineEdit_120.setObjectName("lineEdit_120")
        self.horizontalLayout_8.addWidget(self.lineEdit_120)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_155 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_155.setFont(font)
        self.label_155.setObjectName("label_155")
        self.horizontalLayout_16.addWidget(self.label_155)
        self.lineEdit_122 = QtWidgets.QLineEdit(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_122.setFont(font)
        self.lineEdit_122.setObjectName("lineEdit_122")
        self.horizontalLayout_16.addWidget(self.lineEdit_122)
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
        self.verticalLayout_3.addWidget(self.widget_2, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButton_23 = QtWidgets.QPushButton(Form)
        self.pushButton_23.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_23.setObjectName("pushButton_23")
        self.horizontalLayout_15.addWidget(self.pushButton_23)
        self.pushButton_24 = QtWidgets.QPushButton(Form)
        self.pushButton_24.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_24.setObjectName("pushButton_24")
        self.horizontalLayout_15.addWidget(self.pushButton_24)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_147.setText(_translate("Form", "上报及认定："))
        self.label.setText(_translate("Form", "被审计对象上报整改情况："))
        self.label_145.setText(_translate("Form", "整改责任部门："))
        self.label_148.setText(_translate("Form", "应上报整改报告时间（根据审计报告要求测算）："))
        self.label_143.setText(_translate("Form", "实际上报整改报告时间："))
        self.label_154.setText(_translate("Form", "整改情况："))
        self.label_150.setText(_translate("Form", "已整改金额（万元）："))
        self.label_144.setText(_translate("Form", "追责问责（人）："))
        self.label_142.setText(_translate("Form", "推动制度建设（个）："))
        self.label_146.setText(_translate("Form", "推动制度建设（文件名称及文号）："))
        self.label_151.setText(_translate("Form", "部分整改情况具体描述："))
        self.label_152.setText(_translate("Form", "未整改原因说明："))
        self.label_153.setText(_translate("Form", "下一步整改措施及时限："))
        self.label_2.setText(_translate("Form", "专报起草处室对上报整改情况的认定："))
        self.label_157.setText(_translate("Form", "认定整改率："))
        self.label_156.setText(_translate("Form", "认定整改金额（万元）："))
        self.label_155.setText(_translate("Form", "认定整改情况："))
        self.pushButton_23.setText(_translate("Form", "确认修改"))
        self.pushButton_24.setText(_translate("Form", "退出"))
