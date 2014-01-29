# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Wed Jan 29 16:13:02 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName(_fromUtf8("TabWidget"))
        TabWidget.resize(590, 436)
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.layoutWidget = QtGui.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(190, 10, 198, 76))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit.setInputMask(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox.setWrapping(False)
        self.doubleSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.doubleSpinBox.setSingleStep(1.0)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.verticalLayout_2.addWidget(self.doubleSpinBox)
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.verticalLayout_2.addWidget(self.doubleSpinBox_2)
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_3.setObjectName(_fromUtf8("doubleSpinBox_3"))
        self.verticalLayout_2.addWidget(self.doubleSpinBox_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 10, 161, 21))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        TabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.layoutWidget_2 = QtGui.QWidget(self.tab1)
        self.layoutWidget_2.setGeometry(QtCore.QRect(200, 20, 198, 76))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.lineEdit_5 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_5.setInputMask(_fromUtf8(""))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.verticalLayout_3.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.verticalLayout_3.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.verticalLayout_3.addWidget(self.lineEdit_7)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.doubleSpinBox_4 = QtGui.QDoubleSpinBox(self.layoutWidget_2)
        self.doubleSpinBox_4.setWrapping(False)
        self.doubleSpinBox_4.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.doubleSpinBox_4.setSingleStep(1.0)
        self.doubleSpinBox_4.setObjectName(_fromUtf8("doubleSpinBox_4"))
        self.verticalLayout_4.addWidget(self.doubleSpinBox_4)
        self.doubleSpinBox_5 = QtGui.QDoubleSpinBox(self.layoutWidget_2)
        self.doubleSpinBox_5.setObjectName(_fromUtf8("doubleSpinBox_5"))
        self.verticalLayout_4.addWidget(self.doubleSpinBox_5)
        self.doubleSpinBox_6 = QtGui.QDoubleSpinBox(self.layoutWidget_2)
        self.doubleSpinBox_6.setObjectName(_fromUtf8("doubleSpinBox_6"))
        self.verticalLayout_4.addWidget(self.doubleSpinBox_6)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        self.lineEdit_8 = QtGui.QLineEdit(self.tab1)
        self.lineEdit_8.setGeometry(QtCore.QRect(20, 20, 161, 21))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        TabWidget.addTab(self.tab1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.graphicsView = QtGui.QGraphicsView(self.tab_2)
        self.graphicsView.setGeometry(QtCore.QRect(30, 60, 521, 321))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        TabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget", None))
        self.lineEdit.setPlaceholderText(_translate("TabWidget", "Sláðu inn lánaupphæð.", None))
        self.lineEdit_2.setPlaceholderText(_translate("TabWidget", "Sláðu inn lánaupphæð.", None))
        self.lineEdit_3.setPlaceholderText(_translate("TabWidget", "Sláðu inn lánaupphæð.", None))
        self.lineEdit_4.setPlaceholderText(_translate("TabWidget", "Sláðu inn upphæð.", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Lán", None))
        self.lineEdit_5.setPlaceholderText(_translate("TabWidget", "Sláðu inn innistæðu.", None))
        self.lineEdit_6.setPlaceholderText(_translate("TabWidget", "Sláðu inn innistæðu.", None))
        self.lineEdit_7.setPlaceholderText(_translate("TabWidget", "Sláðu inn innistæðu.", None))
        self.lineEdit_8.setPlaceholderText(_translate("TabWidget", "Sláðu inn upphæð.", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "Reikningar", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "Plot", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TabWidget = QtGui.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec_())

