# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'students.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_students(object):
    def setupUi(self, students):
        if not students.objectName():
            students.setObjectName(u"students")
        students.resize(796, 469)
        self.verticalLayout = QVBoxLayout(students)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txt_title = QLabel(students)
        self.txt_title.setObjectName(u"txt_title")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.txt_title.setFont(font)
        self.txt_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.txt_title)

        self.table_student = QTableView(students)
        self.table_student.setObjectName(u"table_student")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_student.sizePolicy().hasHeightForWidth())
        self.table_student.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(14)
        self.table_student.setFont(font1)

        self.verticalLayout.addWidget(self.table_student)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_new = QPushButton(students)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy1)
        self.btn_new.setMinimumSize(QSize(100, 40))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.btn_new.setFont(font2)

        self.horizontalLayout.addWidget(self.btn_new)

        self.btn_modify = QPushButton(students)
        self.btn_modify.setObjectName(u"btn_modify")
        sizePolicy1.setHeightForWidth(self.btn_modify.sizePolicy().hasHeightForWidth())
        self.btn_modify.setSizePolicy(sizePolicy1)
        self.btn_modify.setMinimumSize(QSize(100, 40))
        self.btn_modify.setFont(font2)

        self.horizontalLayout.addWidget(self.btn_modify)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(students)

        QMetaObject.connectSlotsByName(students)
    # setupUi

    def retranslateUi(self, students):
        students.setWindowTitle(QCoreApplication.translate("students", u"Dialog", None))
#if QT_CONFIG(tooltip)
        students.setToolTip(QCoreApplication.translate("students", u"Students", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.txt_title.setToolTip(QCoreApplication.translate("students", u"student", None))
#endif // QT_CONFIG(tooltip)
        self.txt_title.setText(QCoreApplication.translate("students", u"ESTUDIANTES", None))
#if QT_CONFIG(tooltip)
        self.table_student.setToolTip(QCoreApplication.translate("students", u"Listado de estudiantes", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_new.setToolTip(QCoreApplication.translate("students", u"Crear nuevo cliente", None))
#endif // QT_CONFIG(tooltip)
        self.btn_new.setText(QCoreApplication.translate("students", u"Nuevo", None))
#if QT_CONFIG(tooltip)
        self.btn_modify.setToolTip(QCoreApplication.translate("students", u"Modificar cliente seleccionado", None))
#endif // QT_CONFIG(tooltip)
        self.btn_modify.setText(QCoreApplication.translate("students", u"Ver Detalle", None))
    # retranslateUi

