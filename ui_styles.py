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


class Style:

    style_bt_standard = """
    QPushButton {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb(27, 29, 35);
        background-color: rgb(27, 29, 35);
        text-align: left;
        padding-left: 45px;
    }
    QPushButton[Active=true] {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb(27, 29, 35);
        border-right: 5px solid rgb(44, 49, 60);
        background-color: rgb(27, 29, 35);
        text-align: left;
        padding-left: 45px;
    }
    QPushButton:hover {
        background-color: rgb(33, 37, 43);
        border-left: 28px solid rgb(33, 37, 43);
    }
    QPushButton:pressed {
        background-color: rgb(85, 170, 255);
        border-left: 28px solid rgb(85, 170, 255);
    }
    """

    style_main_window = (
        "QMainWindow {background: transparent; }\n"
        "QToolTip {\n"
        "	color: #ffffff;\n"
        "	background-color: rgba(27, 29, 35, 160);\n"
        "	border: 1px solid rgb(40, 40, 40);\n"
        "	border-radius: 2px;\n"
        "}"
    )

    style_frame_main = (
        u"/* LINE EDIT */\n"
        "QLineEdit {\n"
        "	background-color: rgb(27, 29, 35);\n"
        "	border-radius: 5px;\n"
        "	border: 2px solid rgb(27, 29, 35);\n"
        "	padding-left: 10px;\n"
        "}\n"
        "QLineEdit:hover {\n"
        "	border: 2px solid rgb(64, 71, 88);\n"
        "}\n"
        "QLineEdit:focus {\n"
        "	border: 2px solid rgb(91, 101, 124);\n"
        "}\n"
        "\n"
        "/* SCROLL BARS */\n"
        "QScrollBar:horizontal {\n"
        "    border: none;\n"
        "    background: rgb(52, 59, 72);\n"
        "    height: 14px;\n"
        "    margin: 0px 21px 0 21px;\n"
        "	border-radius: 0px;\n"
        "}\n"
        "QScrollBar::handle:horizontal {\n"
        "    background: rgb(85, 170, 255);\n"
        "    min-width: 25px;\n"
        "	border-radius: 7px\n"
        "}\n"
        "QScrollBar::add-line:horizontal {\n"
        "    border: none;\n"
        "    background: rgb(55, 63, 77);\n"
        "    width: 20px;\n"
        "	border-top-right-radius: 7px;\n"
        "    border-bottom-right-radius: 7px;\n"
        "    subcontrol-position: right;\n"
        "    subcontrol-origin: margin;\n"
        "}\n"
        "QScrollBar::sub-line:horizontal {\n"
        "    border: none;\n"
        "    background: rgb(55, 63, 77);\n"
        "    width: 20px;\n"
        ""
        "	border-top-left-radius: 7px;\n"
        "    border-bottom-left-radius: 7px;\n"
        "    subcontrol-position: left;\n"
        "    subcontrol-origin: margin;\n"
        "}\n"
        "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
        "{\n"
        "     background: none;\n"
        "}\n"
        "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
        "{\n"
        "     background: none;\n"
        "}\n"
        " QScrollBar:vertical {\n"
        "	border: none;\n"
        "    background: rgb(52, 59, 72);\n"
        "    width: 14px;\n"
        "    margin: 21px 0 21px 0;\n"
        "	border-radius: 0px;\n"
        " }\n"
        " QScrollBar::handle:vertical {	\n"
        "	background: rgb(85, 170, 255);\n"
        "    min-height: 25px;\n"
        "	border-radius: 7px\n"
        " }\n"
        " QScrollBar::add-line:vertical {\n"
        "     border: none;\n"
        "    background: rgb(55, 63, 77);\n"
        "     height: 20px;\n"
        "	border-bottom-left-radius: 7px;\n"
        "    border-bottom-right-radius: 7px;\n"
        "     subcontrol-position: bottom;\n"
        "     subcontrol-origin: margin;\n"
        " }\n"
        " QScrollBar::sub-line:vertical {\n"
        "	border: none;\n"
        "    background: rgb(55, 63"
        ", 77);\n"
        "     height: 20px;\n"
        "	border-top-left-radius: 7px;\n"
        "    border-top-right-radius: 7px;\n"
        "     subcontrol-position: top;\n"
        "     subcontrol-origin: margin;\n"
        " }\n"
        " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
        "     background: none;\n"
        " }\n"
        "\n"
        " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
        "     background: none;\n"
        " }\n"
        "\n"
        "/* CHECKBOX */\n"
        "QCheckBox::indicator {\n"
        "    border: 3px solid rgb(52, 59, 72);\n"
        "	width: 15px;\n"
        "	height: 15px;\n"
        "	border-radius: 10px;\n"
        "    background: rgb(44, 49, 60);\n"
        "}\n"
        "QCheckBox::indicator:hover {\n"
        "    border: 3px solid rgb(58, 66, 81);\n"
        "}\n"
        "QCheckBox::indicator:checked {\n"
        "    background: 3px solid rgb(52, 59, 72);\n"
        "	border: 3px solid rgb(52, 59, 72);	\n"
        "	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
        "}\n"
        "\n"
        "/* RADIO BUTTON */\n"
        "QRadioButton::indicator {\n"
        "    border: 3px solid rgb(52, 59, 72);\n"
        "	width: 15px;\n"
        "	height: 15px;\n"
        "	border-radius"
        ": 10px;\n"
        "    background: rgb(44, 49, 60);\n"
        "}\n"
        "QRadioButton::indicator:hover {\n"
        "    border: 3px solid rgb(58, 66, 81);\n"
        "}\n"
        "QRadioButton::indicator:checked {\n"
        "    background: 3px solid rgb(94, 106, 130);\n"
        "	border: 3px solid rgb(52, 59, 72);	\n"
        "}\n"
        "\n"
        "/* COMBOBOX */\n"
        "QComboBox{\n"
        "	background-color: rgb(27, 29, 35);\n"
        "	border-radius: 5px;\n"
        "	border: 2px solid rgb(27, 29, 35);\n"
        "	padding: 5px;\n"
        "	padding-left: 10px;\n"
        "}\n"
        "QComboBox:hover{\n"
        "	border: 2px solid rgb(64, 71, 88);\n"
        "}\n"
        "QComboBox::drop-down {\n"
        "	subcontrol-origin: padding;\n"
        "	subcontrol-position: top right;\n"
        "	width: 25px; \n"
        "	border-left-width: 3px;\n"
        "	border-left-color: rgba(39, 44, 54, 150);\n"
        "	border-left-style: solid;\n"
        "	border-top-right-radius: 3px;\n"
        "	border-bottom-right-radius: 3px;	\n"
        "	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
        "	background-position: center;\n"
        "	background-repeat: no-reperat;\n"
        " }\n"
        "QComboBox QAbstractItemView {\n"
        "	color: rgb("
        "85, 170, 255);	\n"
        "	background-color: rgb(27, 29, 35);\n"
        "	padding: 10px;\n"
        "	selection-background-color: rgb(39, 44, 54);\n"
        "}\n"
        "\n"
        "/* SLIDERS */\n"
        "QSlider::groove:horizontal {\n"
        "    border-radius: 9px;\n"
        "    height: 18px;\n"
        "	margin: 0px;\n"
        "	background-color: rgb(52, 59, 72);\n"
        "}\n"
        "QSlider::groove:horizontal:hover {\n"
        "	background-color: rgb(55, 62, 76);\n"
        "}\n"
        "QSlider::handle:horizontal {\n"
        "    background-color: rgb(85, 170, 255);\n"
        "    border: none;\n"
        "    height: 18px;\n"
        "    width: 18px;\n"
        "    margin: 0px;\n"
        "	border-radius: 9px;\n"
        "}\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background-color: rgb(105, 180, 255);\n"
        "}\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background-color: rgb(65, 130, 195);\n"
        "}\n"
        "\n"
        "QSlider::groove:vertical {\n"
        "    border-radius: 9px;\n"
        "    width: 18px;\n"
        "    margin: 0px;\n"
        "	background-color: rgb(52, 59, 72);\n"
        "}\n"
        "QSlider::groove:vertical:hover {\n"
        "	background-color: rgb(55, 62, 76);\n"
        "}\n"
        "QSlider::handle:verti"
        "cal {\n"
        "    background-color: rgb(85, 170, 255);\n"
        "	border: none;\n"
        "    height: 18px;\n"
        "    width: 18px;\n"
        "    margin: 0px;\n"
        "	border-radius: 9px;\n"
        "}\n"
        "QSlider::handle:vertical:hover {\n"
        "    background-color: rgb(105, 180, 255);\n"
        "}\n"
        "QSlider::handle:vertical:pressed {\n"
        "    background-color: rgb(65, 130, 195);\n"
        "}\n"
        "\n"
        ""
    )

    style_btn_toggle_menu = (
        u"QPushButton {\n"
        "	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
        "	background-position: center;\n"
        "	background-repeat: no-reperat;\n"
        "	border: none;\n"
        "	background-color: rgb(27, 29, 35);\n"
        "}\n"
        "QPushButton:hover {\n"
        "	background-color: rgb(33, 37, 43);\n"
        "}\n"
        "QPushButton:pressed {	\n"
        "	background-color: rgb(85, 170, 255);\n"
        "}"
    )

    style_frame_toggle = u"background-color: rgb(27, 29, 35);"

    style_btn_maximize_restore = (
        u"QPushButton {	\n"
        "	border: none;\n"
        "	background-color: transparent;\n"
        "}\n"
        "QPushButton:hover {\n"
        "	background-color: rgb(52, 59, 72);\n"
        "}\n"
        "QPushButton:pressed {	\n"
        "	background-color: rgb(85, 170, 255);\n"
        "}"
    )

    style_btn_close = (
        u"QPushButton {	\n"
        "	border: none;\n"
        "	background-color: transparent;\n"
        "}\n"
        "QPushButton:hover {\n"
        "	background-color: rgb(52, 59, 72);\n"
        "}\n"
        "QPushButton:pressed {	\n"
        "	background-color: rgb(85, 170, 255);\n"
        "}"
    )

    # QFrame
    style_frame_top_info = u"background-color: rgb(39, 44, 54);"

    # QLabel
    style_label_top_info = u"color: rgb(98, 103, 111); "

    ###################################################

    style_label_user_icon = (
        u"QLabel {\n"
        "	border-radius: 30px;\n"
        "	background-color: rgb(44, 49, 60);\n"
        "	border: 5px solid rgb(39, 44, 54);\n"
        "	background-position: center;\n"
        "	background-repeat: no-repeat;\n"
        "}"
    )

    style_frame_content_right = u"background-color: rgb(44, 49, 60);"

    # QFrame
    style_frame = u"border-radius: 5px;"
    style_frame_div_content_1 = (
        u"background-color: rgb(41, 45, 56);\n" "border-radius: 5px;\n" ""
    )

    style_frame_title_wid_1 = u"background-color: rgb(39, 44, 54);"

    # QLineEdit
    style_lineEdit = (
        u"QLineEdit {\n"
        "	background-color: rgb(27, 29, 35);\n"
        "	border-radius: 5px;\n"
        "	border: 2px solid rgb(27, 29, 35);\n"
        "	padding-left: 10px;\n"
        "}\n"
        "QLineEdit:hover {\n"
        "	border: 2px solid rgb(64, 71, 88);\n"
        "}\n"
        "QLineEdit:focus {\n"
        "	border: 2px solid rgb(91, 101, 124);\n"
        "}"
    )

    style_pushButton = (
        u"QPushButton {\n"
        "	border: 2px solid rgb(52, 59, 72);\n"
        "	border-radius: 5px;	\n"
        "	background-color: rgb(52, 59, 72);\n"
        "}\n"
        "QPushButton:hover {\n"
        "	background-color: rgb(57, 65, 80);\n"
        "	border: 2px solid rgb(61, 70, 86);\n"
        "}\n"
        "QPushButton:pressed {	\n"
        "	background-color: rgb(35, 40, 49);\n"
        "	border: 2px solid rgb(43, 50, 61);\n"
        "}"
    )

    style_labelVersion_3 = u"color: rgb(98, 103, 111);"

    style_frame_2 = u"background-color: rgb(39, 44, 54);\n" "border-radius: 5px;"

    style_verticalScrollBar = (
        u" QScrollBar:vertical {\n"
        "	border: none;\n"
        "    background: rgb(52, 59, 72);\n"
        "    width: 14px;\n"
        "    margin: 21px 0 21px 0;\n"
        "	border-radius: 0px;\n"
        " }"
    )

    style_scrollArea = (
        u"QScrollArea {\n"
        "	border: none;\n"
        "	border-radius: 0px;\n"
        "}\n"
        "QScrollBar:horizontal {\n"
        "    border: none;\n"
        "    background: rgb(52, 59, 72);\n"
        "    height: 14px;\n"
        "    margin: 0px 21px 0 21px;\n"
        "	border-radius: 0px;\n"
        "}\n"
        " QScrollBar:vertical {\n"
        "	border: none;\n"
        "    background: rgb(52, 59, 72);\n"
        "    width: 14px;\n"
        "    margin: 21px 0 21px 0;\n"
        "	border-radius: 0px;\n"
        " }\n"
        ""
    )

    style_plainTextEdit = (
        u"QPlainTextEdit {\n"
        "	background-color: rgb(27, 29, 35);\n"
        "	border-radius: 5px;\n"
        "	padding: 10px;\n"
        "}\n"
        "QPlainTextEdit:hover {\n"
        "	border: 2px solid rgb(64, 71, 88);\n"
        "}\n"
        "QPlainTextEdit:focus {\n"
        "	border: 2px solid rgb(91, 101, 124);\n"
        "}"
    )

    style_comboBox = (
        u"QComboBox{\n"
        "	background-color: rgb(27, 29, 35);\n"
        "	border-radius: 5px;\n"
        "	border: 2px solid rgb(27, 29, 35);\n"
        "	padding: 5px;\n"
        "	padding-left: 10px;\n"
        "}\n"
        "QComboBox:hover{\n"
        "	border: 2px solid rgb(64, 71, 88);\n"
        "}\n"
        "QComboBox QAbstractItemView {\n"
        "	color: rgb(85, 170, 255);	\n"
        "	background-color: rgb(27, 29, 35);\n"
        "	padding: 10px;\n"
        "	selection-background-color: rgb(39, 44, 54);\n"
        "}"
    )

    style_horizontalScrollBar = (
        u"QScrollBar:horizontal {\n"
        "    border: none;\n"
        "    background: rgb(52, 59, 72);\n"
        "    height: 14px;\n"
        "    margin: 0px 21px 0 21px;\n"
        "	border-radius: 0px;\n"
        "}\n"
        ""
    )

    style_commandLinkButton = (
        u"QCommandLinkButton {	\n"
        "	color: rgb(85, 170, 255);\n"
        "	border-radius: 5px;\n"
        "	padding: 5px;\n"
        "}\n"
        "QCommandLinkButton:hover {	\n"
        "	color: rgb(210, 210, 210);\n"
        "	background-color: rgb(44, 49, 60);\n"
        "}\n"
        "QCommandLinkButton:pressed {	\n"
        "	color: rgb(210, 210, 210);\n"
        "	background-color: rgb(52, 58, 71);\n"
        "}"
    )

    style_tableWidget = (
        u"QTableWidget {	\n"
        "	background-color: rgb(39, 44, 54);\n"
        "	padding: 10px;\n"
        "	border-radius: 5px;\n"
        "	gridline-color: rgb(44, 49, 60);\n"
        "	border-bottom: 1px solid rgb(44, 49, 60);\n"
        "}\n"
        "QTableWidget::item{\n"
        "	border-color: rgb(44, 49, 60);\n"
        "	padding-left: 5px;\n"
        "	padding-right: 5px;\n"
        "	gridline-color: rgb(44, 49, 60);\n"
        "}\n"
        "QTableWidget::item:selected{\n"
        "	background-color: rgb(85, 170, 255);\n"
        "}\n"
        "QScrollBar:horizontal {\n"
        "    border: none;\n"
        "    background: rgb(52, 59, 72);\n"
        "    height: 14px;\n"
        "    margin: 0px 21px 0 21px;\n"
        "	border-radius: 0px;\n"
        "}\n"
        " QScrollBar:vertical {\n"
        "	border: none;\n"
        "    background: rgb(52, 59, 72);\n"
        "    width: 14px;\n"
        "    margin: 21px 0 21px 0;\n"
        "	border-radius: 0px;\n"
        " }\n"
        "QHeaderView::section{\n"
        "	Background-color: rgb(39, 44, 54);\n"
        "	max-width: 30px;\n"
        "	border: 1px solid rgb(44, 49, 60);\n"
        "	border-style: none;\n"
        "    border-bottom: 1px solid rgb(44, 49, 60);\n"
        "    border-right: 1px solid rgb(44, 49, 60);\n"
        "}\n"
        ""
        "QTableWidget::horizontalHeader {	\n"
        "	background-color: rgb(81, 255, 0);\n"
        "}\n"
        "QHeaderView::section:horizontal\n"
        "{\n"
        "    border: 1px solid rgb(32, 34, 42);\n"
        "	background-color: rgb(27, 29, 35);\n"
        "	padding: 3px;\n"
        "	border-top-left-radius: 7px;\n"
        "    border-top-right-radius: 7px;\n"
        "}\n"
        "QHeaderView::section:vertical\n"
        "{\n"
        "    border: 1px solid rgb(44, 49, 60);\n"
        "}\n"
        ""
    )

    style_frame_grip = u"background-color: rgb(33, 37, 43);"
    style_label_credits = u"color: rgb(98, 103, 111);"

    style_label_version = u"color: rgb(98, 103, 111);"
    style_frame_size_grip = (
        u"QSizeGrip {\n"
        "	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
        "	background-position: center;\n"
        "	background-repeat: no-reperat;\n"
        "}"
    )
