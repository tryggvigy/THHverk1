# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Wed Jan 29 19:25:04 2014
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
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(470, 110, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.checkBox = QtGui.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(350, 20, 74, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.tab)
        self.checkBox_2.setGeometry(QtCore.QRect(350, 50, 70, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.tab)
        self.checkBox_3.setGeometry(QtCore.QRect(350, 70, 70, 31))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.widget = QtGui.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(10, 100, 280, 22))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.widget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.comboBox_2 = QtGui.QComboBox(self.widget)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.comboBox_2, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.widget)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.comboBox, 0, 1, 1, 1)
        self.widget1 = QtGui.QWidget(self.tab)
        self.widget1.setGeometry(QtCore.QRect(10, 0, 335, 95))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.gridLayout_4 = QtGui.QGridLayout(self.widget1)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit = QtGui.QLineEdit(self.widget1)
        self.lineEdit.setInputMask(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.widget1)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.widget1)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 3, 1, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.widget1)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 2, 0, 1, 1)
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(self.widget1)
        self.doubleSpinBox_3.setObjectName(_fromUtf8("doubleSpinBox_3"))
        self.gridLayout.addWidget(self.doubleSpinBox_3, 3, 2, 1, 1)
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.widget1)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.gridLayout.addWidget(self.doubleSpinBox_2, 2, 2, 1, 1)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.widget1)
        self.doubleSpinBox.setWrapping(False)
        self.doubleSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.doubleSpinBox.setSingleStep(1.0)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.gridLayout.addWidget(self.doubleSpinBox, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 0, 1, 1)
        TabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.pushButton_2 = QtGui.QPushButton(self.tab1)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 140, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.widget2 = QtGui.QWidget(self.tab1)
        self.widget2.setGeometry(QtCore.QRect(12, 1, 385, 93))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(self.widget2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.widget2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 0, 3, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.widget2)
        self.lineEdit_5.setInputMask(_fromUtf8(""))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout_2.addWidget(self.lineEdit_5, 1, 1, 1, 1)
        self.doubleSpinBox_4 = QtGui.QDoubleSpinBox(self.widget2)
        self.doubleSpinBox_4.setWrapping(False)
        self.doubleSpinBox_4.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.doubleSpinBox_4.setSingleStep(1.0)
        self.doubleSpinBox_4.setObjectName(_fromUtf8("doubleSpinBox_4"))
        self.gridLayout_2.addWidget(self.doubleSpinBox_4, 1, 2, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.widget2)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout_2.addWidget(self.spinBox, 1, 3, 1, 1)
        self.lineEdit_8 = QtGui.QLineEdit(self.widget2)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.gridLayout_2.addWidget(self.lineEdit_8, 2, 0, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.widget2)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout_2.addWidget(self.lineEdit_6, 2, 1, 1, 1)
        self.doubleSpinBox_5 = QtGui.QDoubleSpinBox(self.widget2)
        self.doubleSpinBox_5.setObjectName(_fromUtf8("doubleSpinBox_5"))
        self.gridLayout_2.addWidget(self.doubleSpinBox_5, 2, 2, 1, 1)
        self.spinBox_2 = QtGui.QSpinBox(self.widget2)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.gridLayout_2.addWidget(self.spinBox_2, 2, 3, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.widget2)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout_2.addWidget(self.lineEdit_7, 3, 1, 1, 1)
        self.doubleSpinBox_6 = QtGui.QDoubleSpinBox(self.widget2)
        self.doubleSpinBox_6.setObjectName(_fromUtf8("doubleSpinBox_6"))
        self.gridLayout_2.addWidget(self.doubleSpinBox_6, 3, 2, 1, 1)
        self.spinBox_3 = QtGui.QSpinBox(self.widget2)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.gridLayout_2.addWidget(self.spinBox_3, 3, 3, 1, 1)
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
        self.pushButton.setText(_translate("TabWidget", "Reikna", None))
        self.checkBox.setText(_translate("TabWidget", "Verðtryggt", None))
        self.checkBox_2.setText(_translate("TabWidget", "Verðtryggt", None))
        self.checkBox_3.setText(_translate("TabWidget", "Verðtryggt", None))
        self.comboBox_2.setItemText(0, _translate("TabWidget", "2014", None))
        self.comboBox_2.setItemText(1, _translate("TabWidget", "2013", None))
        self.comboBox_2.setItemText(2, _translate("TabWidget", "2012", None))
        self.comboBox_2.setItemText(3, _translate("TabWidget", "2011", None))
        self.comboBox_2.setItemText(4, _translate("TabWidget", "2010", None))
        self.comboBox_2.setItemText(5, _translate("TabWidget", "2009", None))
        self.comboBox_2.setItemText(6, _translate("TabWidget", "2008", None))
        self.comboBox_2.setItemText(7, _translate("TabWidget", "2007", None))
        self.comboBox_2.setItemText(8, _translate("TabWidget", "2006", None))
        self.comboBox_2.setItemText(9, _translate("TabWidget", "2005", None))
        self.comboBox_2.setItemText(10, _translate("TabWidget", "2004", None))
        self.comboBox_2.setItemText(11, _translate("TabWidget", "2003", None))
        self.comboBox_2.setItemText(12, _translate("TabWidget", "2002", None))
        self.comboBox_2.setItemText(13, _translate("TabWidget", "2001", None))
        self.comboBox_2.setItemText(14, _translate("TabWidget", "2000", None))
        self.comboBox_2.setItemText(15, _translate("TabWidget", "1999", None))
        self.comboBox_2.setItemText(16, _translate("TabWidget", "1998", None))
        self.comboBox_2.setItemText(17, _translate("TabWidget", "1997", None))
        self.comboBox_2.setItemText(18, _translate("TabWidget", "1996", None))
        self.comboBox_2.setItemText(19, _translate("TabWidget", "1995", None))
        self.comboBox_2.setItemText(20, _translate("TabWidget", "1994", None))
        self.comboBox_2.setItemText(21, _translate("TabWidget", "1993", None))
        self.comboBox_2.setItemText(22, _translate("TabWidget", "1992", None))
        self.comboBox_2.setItemText(23, _translate("TabWidget", "1991", None))
        self.comboBox_2.setItemText(24, _translate("TabWidget", "1990", None))
        self.label.setText(_translate("TabWidget", "Tímabil meðalverðbólgu: ", None))
        #self.comboBox.setCurrentText(_translate("TabWidget", "1990", None))
        self.comboBox.setItemText(0, _translate("TabWidget", "2014", None))
        self.comboBox.setItemText(1, _translate("TabWidget", "2013", None))
        self.comboBox.setItemText(2, _translate("TabWidget", "2012", None))
        self.comboBox.setItemText(3, _translate("TabWidget", "2011", None))
        self.comboBox.setItemText(4, _translate("TabWidget", "2010", None))
        self.comboBox.setItemText(5, _translate("TabWidget", "2009", None))
        self.comboBox.setItemText(6, _translate("TabWidget", "2008", None))
        self.comboBox.setItemText(7, _translate("TabWidget", "2007", None))
        self.comboBox.setItemText(8, _translate("TabWidget", "2006", None))
        self.comboBox.setItemText(9, _translate("TabWidget", "2005", None))
        self.comboBox.setItemText(10, _translate("TabWidget", "2004", None))
        self.comboBox.setItemText(11, _translate("TabWidget", "2003", None))
        self.comboBox.setItemText(12, _translate("TabWidget", "2002", None))
        self.comboBox.setItemText(13, _translate("TabWidget", "2001", None))
        self.comboBox.setItemText(14, _translate("TabWidget", "2000", None))
        self.comboBox.setItemText(15, _translate("TabWidget", "1999", None))
        self.comboBox.setItemText(16, _translate("TabWidget", "1998", None))
        self.comboBox.setItemText(17, _translate("TabWidget", "1997", None))
        self.comboBox.setItemText(18, _translate("TabWidget", "1996", None))
        self.comboBox.setItemText(19, _translate("TabWidget", "1995", None))
        self.comboBox.setItemText(20, _translate("TabWidget", "1994", None))
        self.comboBox.setItemText(21, _translate("TabWidget", "1993", None))
        self.comboBox.setItemText(22, _translate("TabWidget", "1992", None))
        self.comboBox.setItemText(23, _translate("TabWidget", "1991", None))
        self.comboBox.setItemText(24, _translate("TabWidget", "1990", None))
        self.lineEdit.setPlaceholderText(_translate("TabWidget", "Sláðu inn lánaupphæð.", None))
        self.lineEdit_2.setPlaceholderText(_translate("TabWidget", "Sláðu inn lánaupphæð.", None))
        self.lineEdit_3.setPlaceholderText(_translate("TabWidget", "Sláðu inn lánaupphæð.", None))
        self.lineEdit_4.setPlaceholderText(_translate("TabWidget", "Sláðu inn greiðslu.", None))
        self.label_2.setText(_translate("TabWidget", "Vextir", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Lán", None))
        self.pushButton_2.setText(_translate("TabWidget", "Reikna", None))
        self.label_3.setText(_translate("TabWidget", "Vextir", None))
        self.label_6.setText(_translate("TabWidget", "Bindis tími", None))
        self.lineEdit_5.setPlaceholderText(_translate("TabWidget", "Sláðu inn innistæðu.", None))
        self.lineEdit_8.setPlaceholderText(_translate("TabWidget", "Sláðu inn upphæð.", None))
        self.lineEdit_6.setPlaceholderText(_translate("TabWidget", "Sláðu inn innistæðu.", None))
        self.lineEdit_7.setPlaceholderText(_translate("TabWidget", "Sláðu inn innistæðu.", None))
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

