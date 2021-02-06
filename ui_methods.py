################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide6
## V: 1.0.0
##
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##
################################################################################

## imports
from PySide6.QtCore import QSize, QPropertyAnimation, Qt, QEasingCurve, QTimer, QEvent
from PySide6.QtGui import QFont, QIcon, QColor
from PySide6.QtWidgets import (
    QPushButton,
    QSizePolicy,
    QGraphicsDropShadowEffect,
    QSizeGrip,
)

from ui_styles import Style


########################################################################
## START - GUI FUNCTIONS
########################################################################

## ==> MAXIMIZE/RESTORE
def maximize_restore(self):
    if self.STATE == 0:
        self.showMaximized()
        self.STATE = 1
        self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ui.btn_maximize_restore.setToolTip("Restore")
        self.ui.btn_maximize_restore.setIcon(
            QIcon(u":/16x16/icons/16x16/cil-window-restore.png")
        )
        self.ui.frame_top_btns.setStyleSheet("background-color: rgb(27, 29, 35)")
        self.ui.frame_size_grip.hide()
    else:
        self.STATE = 0
        self.showNormal()
        self.resize(self.width() + 1, self.height() + 1)
        self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.ui.btn_maximize_restore.setToolTip("Maximize")
        self.ui.btn_maximize_restore.setIcon(
            QIcon(u":/16x16/icons/16x16/cil-window-maximize.png")
        )
        self.ui.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
        self.ui.frame_size_grip.show()


## ==> ENABLE MAXIMUM SIZE
def enableMaximumSize(self, width, height):
    if width != "" and height != "":
        self.setMaximumSize(QSize(width, height))
        self.ui.frame_size_grip.hide()
        self.ui.btn_maximize_restore.hide()


## ==> TOGGLE MENU
def toggleMenu(self, maxWidth, enable):
    if enable:
        # GET WIDTH
        width = self.ui.frame_left_menu.width()
        maxExtend = maxWidth
        standard = 70

        # SET MAX WIDTH
        if width == 70:
            widthExtended = maxExtend
        else:
            widthExtended = standard

        # ANIMATION
        self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()


## ==> SET TITLE BAR
########################################################################
def removeTitleBar(self, status):
    self.TITLE_BAR = status


## ==> HEADER TEXTS
########################################################################
# LABEL TITLE
def labelTitle(self, text):
    self.ui.label_title_bar_top.setText(text)


# LABEL DESCRIPTION
def labelDescription(self, text):
    self.ui.label_top_info_1.setText(text)


## ==> DYNAMIC MENUS
def addNewMenu(self, name, selfName, icon, isTopMenu):
    font = QFont()
    font.setFamily(u"Segoe UI")
    button = QPushButton(str(self.count), self)
    button.setObjectName(selfName)
    sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    sizePolicy3.setHorizontalStretch(0)
    sizePolicy3.setVerticalStretch(0)
    sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
    button.setSizePolicy(sizePolicy3)
    button.setMinimumSize(QSize(0, 70))
    button.setLayoutDirection(Qt.LeftToRight)
    button.setFont(font)
    button.setStyleSheet(Style.style_bt_standard.replace("ICON_REPLACE", icon))
    button.setText(name)
    button.setToolTip(name)
    button.clicked.connect(self.Button)

    if isTopMenu:
        self.ui.layout_menus.addWidget(button)
    else:
        self.ui.layout_menu_bottom.addWidget(button)


## ==> SELECT/DESELECT MENU
## ==> SELECT
def selectMenu(self, getStyle):
    select = getStyle + ("QPushButton { border-right: 7px solid rgb(44, 49, 60); }")
    return select


## ==> DESELECT
def deselectMenu(self, getStyle):
    deselect = getStyle.replace(
        "QPushButton { border-right: 7px solid rgb(44, 49, 60); }", ""
    )
    return deselect


## ==> START SELECTION
def selectStandardMenu(self, widget):
    for w in self.ui.frame_left_menu.findChildren(QPushButton):
        if w.objectName() == widget:
            w.setStyleSheet(self.selectMenu(w.styleSheet()))


## ==> RESET SELECTION
def resetStyle(self, widget):
    for w in self.ui.frame_left_menu.findChildren(QPushButton):
        if w.objectName() != widget:
            w.setStyleSheet(self.deselectMenu(w.styleSheet()))


## ==> CHANGE PAGE LABEL TEXT
def labelPage(self, text):
    newText = "| " + text.upper()
    self.ui.label_top_info_2.setText(newText)


## ==> USER ICON
def userIcon(self, initialsTooltip, icon, showHide):
    if showHide:
        # SET TEXT
        self.ui.label_user_icon.setText(initialsTooltip)

        # SET ICON
        if icon:
            style = self.ui.label_user_icon.styleSheet()
            setIcon = "QLabel { background-image: " + icon + "; }"
            self.ui.label_user_icon.setStyleSheet(style + setIcon)
            self.ui.label_user_icon.setText("")
            self.ui.label_user_icon.setToolTip(initialsTooltip)
    else:
        self.ui.label_user_icon.hide()


########################################################################
## END - GUI FUNCTIONS
########################################################################

########################################################################
## START - GUI DEFINITIONS
########################################################################

## ==> UI DEFINITIONS
########################################################################
def uiDefinitions(self):
    def doubleClickMaximizeRestore(event):
        # IF DOUBLE CLICK CHANGE STATUS
        if event.type() == QEvent.MouseButtonDblClick:
            QTimer.singleShot(250, lambda: self.maximize_restore())

    ## REMOVE ==> STANDARD TITLE BAR
    if self.TITLE_BAR:
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.frame_label_top_btns.mouseDoubleClickEvent = doubleClickMaximizeRestore
    else:
        self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ui.frame_label_top_btns.setContentsMargins(8, 0, 0, 5)
        self.ui.frame_label_top_btns.setMinimumHeight(42)
        self.ui.frame_icon_top_bar.hide()
        self.ui.frame_btns_right.hide()
        self.ui.frame_size_grip.hide()

    ## SHOW ==> DROP SHADOW
    self.shadow = QGraphicsDropShadowEffect(self)
    self.shadow.setBlurRadius(17)
    self.shadow.setXOffset(0)
    self.shadow.setYOffset(0)
    self.shadow.setColor(QColor(0, 0, 0, 150))
    self.ui.frame_main.setGraphicsEffect(self.shadow)

    ## ==> RESIZE WINDOW
    self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
    self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

    ### ==> MINIMIZE
    self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

    ## ==> MAXIMIZE/RESTORE
    self.ui.btn_maximize_restore.clicked.connect(lambda: self.maximize_restore())

    ## SHOW ==> CLOSE APPLICATION
    self.ui.btn_close.clicked.connect(lambda: self.close())


########################################################################
## END - GUI DEFINITIONS
########################################################################
