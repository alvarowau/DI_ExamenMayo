# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(441, 191)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.txt_login = QLabel(self.centralwidget)
        self.txt_login.setObjectName(u"txt_login")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_login.sizePolicy().hasHeightForWidth())
        self.txt_login.setSizePolicy(sizePolicy)
        self.txt_login.setMinimumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.txt_login.setFont(font)
        self.txt_login.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.txt_login)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.txt_user = QLabel(self.centralwidget)
        self.txt_user.setObjectName(u"txt_user")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.txt_user.setFont(font1)
        self.txt_user.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.txt_user)

        self.line_user = QLineEdit(self.centralwidget)
        self.line_user.setObjectName(u"line_user")
        font2 = QFont()
        font2.setPointSize(14)
        self.line_user.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.line_user)

        self.txt_password = QLabel(self.centralwidget)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setFont(font1)
        self.txt_password.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.txt_password)

        self.line_password = QLineEdit(self.centralwidget)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setFont(font2)
        self.line_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.line_password)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_login = QPushButton(self.centralwidget)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy1)
        self.btn_login.setMinimumSize(QSize(100, 30))
        self.btn_login.setFont(font1)
        self.btn_login.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.horizontalLayout_2.addWidget(self.btn_login)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.formLayout)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
#if QT_CONFIG(accessibility)
        Login.setAccessibleDescription(QCoreApplication.translate("Login", u"Login", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(tooltip)
        self.txt_login.setToolTip(QCoreApplication.translate("Login", u"Login", None))
#endif // QT_CONFIG(tooltip)
        self.txt_login.setText(QCoreApplication.translate("Login", u"LOGIN", None))
#if QT_CONFIG(tooltip)
        self.txt_user.setToolTip(QCoreApplication.translate("Login", u"Usuario", None))
#endif // QT_CONFIG(tooltip)
        self.txt_user.setText(QCoreApplication.translate("Login", u"Usuario", None))
#if QT_CONFIG(tooltip)
        self.line_user.setToolTip(QCoreApplication.translate("Login", u"Ingrese su user", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.txt_password.setToolTip(QCoreApplication.translate("Login", u"Contrase\u00f1a", None))
#endif // QT_CONFIG(tooltip)
        self.txt_password.setText(QCoreApplication.translate("Login", u"Contrase\u00f1a", None))
#if QT_CONFIG(tooltip)
        self.line_password.setToolTip(QCoreApplication.translate("Login", u"Ingrese su contrase\u00f1a", None))
#endif // QT_CONFIG(tooltip)
        self.btn_login.setText(QCoreApplication.translate("Login", u"Acceder", None))
    # retranslateUi

