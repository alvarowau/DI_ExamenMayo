# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connection_bd.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_connection_bd(object):
    def setupUi(self, connection_bd):
        if not connection_bd.objectName():
            connection_bd.setObjectName(u"connection_bd")
        connection_bd.resize(509, 329)
        connection_bd.setMinimumSize(QSize(477, 286))
        connection_bd.setMaximumSize(QSize(999, 999))
        self.verticalLayout = QVBoxLayout(connection_bd)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txt_title = QLabel(connection_bd)
        self.txt_title.setObjectName(u"txt_title")
        self.txt_title.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.txt_title.setFont(font)
        self.txt_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.txt_title)

        self.txt_subtitle = QLabel(connection_bd)
        self.txt_subtitle.setObjectName(u"txt_subtitle")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.txt_subtitle.setFont(font1)
        self.txt_subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.txt_subtitle)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.txt_bd = QLabel(connection_bd)
        self.txt_bd.setObjectName(u"txt_bd")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.txt_bd.setFont(font2)
        self.txt_bd.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.txt_bd)

        self.line_bd = QLineEdit(connection_bd)
        self.line_bd.setObjectName(u"line_bd")
        self.line_bd.setEnabled(True)
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        self.line_bd.setFont(font3)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.line_bd)

        self.txt_user = QLabel(connection_bd)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setFont(font2)
        self.txt_user.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.txt_user)

        self.line_user = QLineEdit(connection_bd)
        self.line_user.setObjectName(u"line_user")
        self.line_user.setEnabled(True)
        font4 = QFont()
        font4.setPointSize(14)
        self.line_user.setFont(font4)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.line_user)

        self.txt_password = QLabel(connection_bd)
        self.txt_password.setObjectName(u"txt_password")
        font5 = QFont()
        font5.setPointSize(13)
        font5.setBold(True)
        self.txt_password.setFont(font5)
        self.txt_password.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.txt_password)

        self.line_password = QLineEdit(connection_bd)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setEnabled(True)
        self.line_password.setFont(font4)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.line_password)

        self.txt_host = QLabel(connection_bd)
        self.txt_host.setObjectName(u"txt_host")
        self.txt_host.setFont(font2)
        self.txt_host.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.txt_host)

        self.line_host = QLineEdit(connection_bd)
        self.line_host.setObjectName(u"line_host")
        self.line_host.setEnabled(True)
        self.line_host.setFont(font4)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.line_host)

        self.txt_port = QLabel(connection_bd)
        self.txt_port.setObjectName(u"txt_port")
        self.txt_port.setFont(font2)
        self.txt_port.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.txt_port)

        self.line_port = QLineEdit(connection_bd)
        self.line_port.setObjectName(u"line_port")
        self.line_port.setEnabled(True)
        self.line_port.setFont(font4)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.line_port)


        self.verticalLayout.addLayout(self.formLayout)

        self.btn_acept = QPushButton(connection_bd)
        self.btn_acept.setObjectName(u"btn_acept")
        self.btn_acept.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_acept.sizePolicy().hasHeightForWidth())
        self.btn_acept.setSizePolicy(sizePolicy)
        self.btn_acept.setFont(font2)
        self.btn_acept.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.verticalLayout.addWidget(self.btn_acept)


        self.retranslateUi(connection_bd)

        QMetaObject.connectSlotsByName(connection_bd)
    # setupUi

    def retranslateUi(self, connection_bd):
        connection_bd.setWindowTitle(QCoreApplication.translate("connection_bd", u"Connection data base", None))
#if QT_CONFIG(tooltip)
        connection_bd.setToolTip(QCoreApplication.translate("connection_bd", u"connection_db", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.txt_title.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.txt_title.setText(QCoreApplication.translate("connection_bd", u"CONEXI\u00d3N A BASE DE DATOS", None))
#if QT_CONFIG(tooltip)
        self.txt_subtitle.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.txt_subtitle.setText(QCoreApplication.translate("connection_bd", u"Ingrese los datos de su conexi\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.txt_bd.setToolTip(QCoreApplication.translate("connection_bd", u"Nombre del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
        self.txt_bd.setText(QCoreApplication.translate("connection_bd", u"Base de datos", None))
#if QT_CONFIG(tooltip)
        self.line_bd.setToolTip(QCoreApplication.translate("connection_bd", u"Nombre de la base de datos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.txt_user.setToolTip(QCoreApplication.translate("connection_bd", u"Nombre del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
        self.txt_user.setText(QCoreApplication.translate("connection_bd", u"Usuario", None))
#if QT_CONFIG(tooltip)
        self.line_user.setToolTip(QCoreApplication.translate("connection_bd", u"Usuario de la Base de datos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.txt_password.setToolTip(QCoreApplication.translate("connection_bd", u"Nombre del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
        self.txt_password.setText(QCoreApplication.translate("connection_bd", u"Contrase\u00f1a", None))
#if QT_CONFIG(tooltip)
        self.line_password.setToolTip(QCoreApplication.translate("connection_bd", u"Contrase\u00f1a de la base de datos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.txt_host.setToolTip(QCoreApplication.translate("connection_bd", u"Nombre del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
        self.txt_host.setText(QCoreApplication.translate("connection_bd", u"Host", None))
#if QT_CONFIG(tooltip)
        self.line_host.setToolTip(QCoreApplication.translate("connection_bd", u"Contrase\u00f1a de la base de datos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.txt_port.setToolTip(QCoreApplication.translate("connection_bd", u"Nombre del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
        self.txt_port.setText(QCoreApplication.translate("connection_bd", u"Puerto", None))
#if QT_CONFIG(tooltip)
        self.line_port.setToolTip(QCoreApplication.translate("connection_bd", u"Contrase\u00f1a de la base de datos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_acept.setToolTip(QCoreApplication.translate("connection_bd", u"Confirmar cambios", None))
#endif // QT_CONFIG(tooltip)
        self.btn_acept.setText(QCoreApplication.translate("connection_bd", u"Confirmar", None))
    # retranslateUi

