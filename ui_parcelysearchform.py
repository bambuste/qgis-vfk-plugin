# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_parcelysearchform.ui'
#
# Created: Fri Nov 20 17:50:47 2015
#      by: PyQt4 UI code generator 4.10.4
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


class Ui_ParcelySearchForm(object):

    def setupUi(self, ParcelySearchForm):
        ParcelySearchForm.setObjectName(_fromUtf8("ParcelySearchForm"))
        ParcelySearchForm.resize(269, 168)
        self.gridLayout = QtGui.QGridLayout(ParcelySearchForm)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(ParcelySearchForm)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.parCisloLineEdit = QtGui.QLineEdit(ParcelySearchForm)
        self.parCisloLineEdit.setInputMask(_fromUtf8(""))
        self.parCisloLineEdit.setObjectName(_fromUtf8("parCisloLineEdit"))
        self.gridLayout.addWidget(self.parCisloLineEdit, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(ParcelySearchForm)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.typParcelyCombo = QtGui.QComboBox(ParcelySearchForm)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.typParcelyCombo.sizePolicy().hasHeightForWidth())
        self.typParcelyCombo.setSizePolicy(sizePolicy)
        self.typParcelyCombo.setObjectName(_fromUtf8("typParcelyCombo"))
        self.typParcelyCombo.addItem(_fromUtf8(""))
        self.typParcelyCombo.addItem(_fromUtf8(""))
        self.typParcelyCombo.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.typParcelyCombo, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(ParcelySearchForm)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.druhPozemkuCombo = QtGui.QComboBox(ParcelySearchForm)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.druhPozemkuCombo.sizePolicy().hasHeightForWidth())
        self.druhPozemkuCombo.setSizePolicy(sizePolicy)
        self.druhPozemkuCombo.setObjectName(_fromUtf8("druhPozemkuCombo"))
        self.gridLayout.addWidget(self.druhPozemkuCombo, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.lvParcelyLineEdit = QtGui.QLineEdit(ParcelySearchForm)
        self.lvParcelyLineEdit.setObjectName(_fromUtf8("lvParcelyLineEdit"))
        self.gridLayout.addWidget(self.lvParcelyLineEdit, 3, 1, 1, 1)
        self.label = QtGui.QLabel(ParcelySearchForm)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.retranslateUi(ParcelySearchForm)
        QtCore.QMetaObject.connectSlotsByName(ParcelySearchForm)

    def retranslateUi(self, ParcelySearchForm):
        ParcelySearchForm.setWindowTitle(
            _translate("ParcelySearchForm", "Form", None))
        self.label_3.setText(
            _translate("ParcelySearchForm", "Parcelní číslo :", None))
        self.label_5.setText(
            _translate("ParcelySearchForm", "Typ parcely:", None))
        self.typParcelyCombo.setItemText(
            0, _translate("ParcelySearchForm", "libovolný", None))
        self.typParcelyCombo.setItemText(
            1, _translate("ParcelySearchForm", "pozemková", None))
        self.typParcelyCombo.setItemText(
            2, _translate("ParcelySearchForm", "stavební", None))
        self.label_6.setText(
            _translate("ParcelySearchForm", "Druh pozemku:", None))
        self.label.setText(_translate("ParcelySearchForm", "LV:", None))
