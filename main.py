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

import sys
import platform

from PySide6.QtWidgets import QMainWindow, QApplication, QHeaderView
from PySide6.QtGui import QFontDatabase
from PySide6.QtCore import QSize, QEvent, Qt

from ui_main import Ui_MainWindow

# import methods
from ui_methods import (
    removeTitleBar,
    labelTitle,
    labelDescription,
    maximize_restore,
    enableMaximumSize,
    toggleMenu,
    addNewMenu,
    selectMenu,
    deselectMenu,
    selectStandardMenu,
    resetStyle,
    labelPage,
    userIcon,
    uiDefinitions,
)


class MainWindow(QMainWindow):
    # load methods
    removeTitleBar = removeTitleBar
    labelTitle = labelTitle
    labelDescription = labelDescription
    maximize_restore = maximize_restore
    enableMaximumSize = enableMaximumSize
    toggleMenu = toggleMenu
    addNewMenu = addNewMenu
    selectMenu = selectMenu
    deselectMenu = deselectMenu
    selectStandardMenu = selectStandardMenu
    resetStyle = resetStyle
    labelPage = labelPage
    userIcon = userIcon
    uiDefinitions = uiDefinitions

    # init
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.STATE = 0
        self.TITLE_BAR = True
        self.count = 1

        ## PRINT ==> SYSTEM
        print("System: " + platform.system())
        print("Version: " + platform.release())

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        self.removeTitleBar(False)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle("Main Window - Python Base")
        self.labelTitle("Main Window - Python Base")
        self.labelDescription("Set text")
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # self.enableMaximumSize(500, 720)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: self.toggleMenu(220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        self.addNewMenu(
            "HOME",
            "btn_home",
            "url(:/16x16/icons/16x16/cil-home.png)",
            True,
        )
        self.addNewMenu(
            "Add User",
            "btn_new_user",
            "url(:/16x16/icons/16x16/cil-user-follow.png)",
            True,
        )
        self.addNewMenu(
            "Custom Widgets",
            "btn_widgets",
            "url(:/16x16/icons/16x16/cil-equalizer.png)",
            False,
        )
        ## ==> END ##

        # START MENU => SELECTION
        self.selectStandardMenu("btn_home")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        self.userIcon("SG", "", True)
        ## ==> END ##

        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if self.STATE == 1:
                self.maximize_restore()

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        self.uiDefinitions()
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################

        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################

        ## ==> QTableWidget RARAMETERS
        ########################################################################
        self.ui.page_widgets.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        ## ==> END ##

        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            print("btn_home")
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            self.resetStyle("btn_home")
            self.labelPage("Home")
            btnWidget.setStyleSheet(self.selectMenu(btnWidget.styleSheet()))

        # PAGE NEW USER
        if btnWidget.objectName() == "btn_new_user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            self.resetStyle("btn_new_user")
            self.labelPage("New User")
            btnWidget.setStyleSheet(self.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_widgets":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            self.resetStyle("btn_widgets")
            self.labelPage("Custom Widgets")
            btnWidget.setStyleSheet(self.selectMenu(btnWidget.styleSheet()))

    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())

    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print("Mouse click: LEFT CLICK")
        if event.buttons() == Qt.RightButton:
            print("Mouse click: RIGHT CLICK")
        if event.buttons() == Qt.MiddleButton:
            print("Mouse click: MIDDLE BUTTON")

    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print("Key: " + str(event.key()) + " | Text Press: " + str(event.text()))

    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print("Height: " + str(self.height()) + " | Width: " + str(self.width()))

    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont("fonts/segoeui.ttf")
    QFontDatabase.addApplicationFont("fonts/segoeuib.ttf")
    window = MainWindow()
    sys.exit(app.exec_())
