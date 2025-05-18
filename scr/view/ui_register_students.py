# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_students.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_students(object):
    def setupUi(self, students):
        if not students.objectName():
            students.setObjectName(u"students")
        students.resize(605, 487)
        students.setMinimumSize(QSize(605, 487))
        students.setMaximumSize(QSize(605, 487))
        self.verticalLayout = QVBoxLayout(students)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txt_title = QLabel(students)
        self.txt_title.setObjectName(u"txt_title")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.txt_title.setFont(font)
        self.txt_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.txt_title)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.txt_name = QLabel(students)
        self.txt_name.setObjectName(u"txt_name")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.txt_name.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.txt_name)

        self.line_name = QLineEdit(students)
        self.line_name.setObjectName(u"line_name")
        self.line_name.setMinimumSize(QSize(0, 35))
        self.line_name.setMaximumSize(QSize(16777215, 35))
        font2 = QFont()
        font2.setPointSize(11)
        self.line_name.setFont(font2)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.line_name)

        self.txt_surname = QLabel(students)
        self.txt_surname.setObjectName(u"txt_surname")
        self.txt_surname.setFont(font1)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.txt_surname)

        self.line_surname = QLineEdit(students)
        self.line_surname.setObjectName(u"line_surname")
        self.line_surname.setMinimumSize(QSize(0, 35))
        self.line_surname.setMaximumSize(QSize(16777215, 35))
        self.line_surname.setFont(font2)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.line_surname)

        self.txt_dni = QLabel(students)
        self.txt_dni.setObjectName(u"txt_dni")
        self.txt_dni.setFont(font1)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.txt_dni)

        self.line_dni = QLineEdit(students)
        self.line_dni.setObjectName(u"line_dni")
        self.line_dni.setMinimumSize(QSize(0, 35))
        self.line_dni.setMaximumSize(QSize(16777215, 35))
        self.line_dni.setFont(font2)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.line_dni)

        self.txt_dob = QLabel(students)
        self.txt_dob.setObjectName(u"txt_dob")
        self.txt_dob.setFont(font1)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.txt_dob)

        self.date_dob = QDateEdit(students)
        self.date_dob.setObjectName(u"date_dob")
        self.date_dob.setFont(font2)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.date_dob)

        self.txt_city = QLabel(students)
        self.txt_city.setObjectName(u"txt_city")
        self.txt_city.setFont(font1)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.txt_city)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.combo_city = QComboBox(students)
        self.combo_city.setObjectName(u"combo_city")
        self.combo_city.setFont(font2)

        self.horizontalLayout_2.addWidget(self.combo_city)

        self.txt_distant = QLabel(students)
        self.txt_distant.setObjectName(u"txt_distant")
        self.txt_distant.setFont(font1)

        self.horizontalLayout_2.addWidget(self.txt_distant)

        self.spint_distant = QSpinBox(students)
        self.spint_distant.setObjectName(u"spint_distant")
        self.spint_distant.setFont(font2)
        self.spint_distant.setMaximum(30)

        self.horizontalLayout_2.addWidget(self.spint_distant)


        self.formLayout_2.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.txt_tutor = QLabel(students)
        self.txt_tutor.setObjectName(u"txt_tutor")
        self.txt_tutor.setFont(font1)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.txt_tutor)

        self.line_tutor = QLineEdit(students)
        self.line_tutor.setObjectName(u"line_tutor")
        self.line_tutor.setMinimumSize(QSize(0, 35))
        self.line_tutor.setMaximumSize(QSize(16777215, 35))
        self.line_tutor.setFont(font2)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.line_tutor)

        self.vcverticalSpacer_5 = QSpacerItem(456, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_2.setItem(7, QFormLayout.FieldRole, self.vcverticalSpacer_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.txt_modality = QLabel(students)
        self.txt_modality.setObjectName(u"txt_modality")
        self.txt_modality.setFont(font1)
        self.txt_modality.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.txt_modality.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.txt_modality)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.radio_presencial = QRadioButton(students)
        self.radio_presencial.setObjectName(u"radio_presencial")
        self.radio_presencial.setFont(font2)

        self.verticalLayout_5.addWidget(self.radio_presencial)

        self.radio_distancia = QRadioButton(students)
        self.radio_distancia.setObjectName(u"radio_distancia")
        self.radio_distancia.setFont(font2)

        self.verticalLayout_5.addWidget(self.radio_distancia)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.txt_activity = QLabel(students)
        self.txt_activity.setObjectName(u"txt_activity")
        self.txt_activity.setFont(font1)
        self.txt_activity.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.txt_activity)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.check_ajedrez = QCheckBox(students)
        self.check_ajedrez.setObjectName(u"check_ajedrez")
        self.check_ajedrez.setFont(font2)

        self.verticalLayout_4.addWidget(self.check_ajedrez)

        self.check_danza = QCheckBox(students)
        self.check_danza.setObjectName(u"check_danza")
        self.check_danza.setFont(font2)

        self.verticalLayout_4.addWidget(self.check_danza)

        self.check_futbol = QCheckBox(students)
        self.check_futbol.setObjectName(u"check_futbol")
        self.check_futbol.setFont(font2)

        self.verticalLayout_4.addWidget(self.check_futbol)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.formLayout_2.setLayout(8, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.txt_tlf = QLabel(students)
        self.txt_tlf.setObjectName(u"txt_tlf")
        self.txt_tlf.setFont(font1)

        self.horizontalLayout_7.addWidget(self.txt_tlf)

        self.line_tlf = QLineEdit(students)
        self.line_tlf.setObjectName(u"line_tlf")
        self.line_tlf.setMinimumSize(QSize(0, 35))
        self.line_tlf.setMaximumSize(QSize(16777215, 35))
        self.line_tlf.setFont(font2)

        self.horizontalLayout_7.addWidget(self.line_tlf)


        self.formLayout_2.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout_7)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_delete = QPushButton(students)
        self.btn_delete.setObjectName(u"btn_delete")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy)
        self.btn_delete.setMinimumSize(QSize(90, 35))
        self.btn_delete.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_delete)

        self.btn_save = QPushButton(students)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(90, 35))
        self.btn_save.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_save)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(students)

        QMetaObject.connectSlotsByName(students)
    # setupUi

    def retranslateUi(self, students):
        students.setWindowTitle(QCoreApplication.translate("students", u"Alta alumnos", None))
        self.txt_title.setText(QCoreApplication.translate("students", u"ALTA ALUMNO", None))
        self.txt_name.setText(QCoreApplication.translate("students", u"Nombre", None))
        self.txt_surname.setText(QCoreApplication.translate("students", u"Apellidos", None))
        self.txt_dni.setText(QCoreApplication.translate("students", u"DNI", None))
        self.txt_dob.setText(QCoreApplication.translate("students", u"Fec. Nacimiento", None))
        self.txt_city.setText(QCoreApplication.translate("students", u"Poblaci\u00f3n", None))
        self.txt_distant.setText(QCoreApplication.translate("students", u"Distancia hasta el centro (Km)", None))
        self.txt_tutor.setText(QCoreApplication.translate("students", u"Tutor", None))
        self.txt_modality.setText(QCoreApplication.translate("students", u"Modalidad", None))
        self.radio_presencial.setText(QCoreApplication.translate("students", u"Presencial", None))
        self.radio_distancia.setText(QCoreApplication.translate("students", u"A Distancia", None))
        self.txt_activity.setText(QCoreApplication.translate("students", u"Extraescolares", None))
        self.check_ajedrez.setText(QCoreApplication.translate("students", u"Ajedrez", None))
        self.check_danza.setText(QCoreApplication.translate("students", u"Danza", None))
        self.check_futbol.setText(QCoreApplication.translate("students", u"F\u00fatbol", None))
        self.txt_tlf.setText(QCoreApplication.translate("students", u"Tlf.", None))
        self.btn_delete.setText(QCoreApplication.translate("students", u"Eliminar", None))
        self.btn_save.setText(QCoreApplication.translate("students", u"Confirmar", None))
    # retranslateUi

