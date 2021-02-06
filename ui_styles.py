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
GRAY_01 = (40, 40, 40)
WHITE_01 = (210, 210, 210)

COLOR_01 = (27, 29, 35)
COLOR_02 = (33, 37, 43)
COLOR_03 = (35, 40, 49)
COLOR_04 = (39, 44, 54)
COLOR_05 = (43, 50, 61)
COLOR_06 = (52, 59, 72)
COLOR_07 = (58, 66, 81)

COLOR_08 = (65, 130, 195)  # slider handle

COLOR_09 = (81, 255, 0)  # light green, table header

COLOR_11 = (85, 170, 255)

COLOR_12 = (91, 101, 124)
COLOR_13 = (94, 106, 130)
COLOR_14 = (98, 103, 111)

COLOR_15 = (105, 180, 255)


# rgba
COLOR_01a = COLOR_01 + (160,)
COLOR_04a = COLOR_04 + (150,)

# similar colors
COLOR_102 = COLOR_02  # (32, 34, 42)
COLOR_104 = COLOR_04  # (41, 45, 56) # Frame Div Content
COLOR_105 = COLOR_05  # (44, 49, 60)
COLOR_106 = COLOR_06  # (52, 58, 71)
COLOR_206 = COLOR_06  # (55, 62, 76)
COLOR_306 = COLOR_06  # (55, 63, 77) # Scrollbar lines
COLOR_107 = COLOR_07  # (57, 65, 80) # Push hover
COLOR_207 = COLOR_07  # (61, 70, 86)
COLOR_307 = COLOR_07  # (64, 71, 88) Combo hover


class Style:

    style_bt_standard = f"""
    QPushButton {{
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb{COLOR_01};
        background-color: rgb{COLOR_01};
        text-align: left;
        padding-left: 45px;
    }}
    QPushButton[Active=true] {{
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb{COLOR_01};
        border-right: 5px solid rgb{COLOR_105};
        background-color: rgb{COLOR_01};
        text-align: left;
        padding-left: 45px;
    }}
    QPushButton:hover {{
        background-color: rgb{COLOR_02};
        border-left: 28px solid rgb{COLOR_02};
    }}
    QPushButton:pressed {{
        background-color: rgb{COLOR_11};
        border-left: 28px solid rgb{COLOR_11};
    }}
    """

    style_main_window = f"""
    QMainWindow {{background: transparent; }}
        QToolTip {{
        color: #ffffff;
        background-color: rgba{COLOR_01a};
        border: 1px solid rgb{GRAY_01};
        border-radius: 2px;
    }}
    """

    style_frame_main = f"""
    /* ######### LINE EDIT ######### */
    QLineEdit {{
        background-color: rgb{COLOR_01};
        border-radius: 5px;
        border: 2px solid rgb{COLOR_01};
        padding-left: 10px;
    }}
    QLineEdit:hover {{
        border: 2px solid rgb{COLOR_307};
    }}
    QLineEdit:focus {{
        border: 2px solid rgb{COLOR_12};
    }}
    
    /* ######### SCROLL BARS ######### */
    QScrollBar:horizontal {{
        border: none;
        background: rgb{COLOR_06};
        height: 14px;
        margin: 0px 21px 0 21px;
        border-radius: 0px;
    }}
    QScrollBar::handle:horizontal {{
        background: rgb{COLOR_11};
        min-width: 25px;
        border-radius: 7px
    }}
    QScrollBar::add-line:horizontal {{
        border: none;
        background: rgb{COLOR_306};
        width: 20px;
        border-top-right-radius: 7px;
        border-bottom-right-radius: 7px;
        subcontrol-position: right;
        subcontrol-origin: margin;
    }}
    QScrollBar::sub-line:horizontal {{
        border: none;
        background: rgb{COLOR_306};
        width: 20px;
    
        border-top-left-radius: 7px;
        border-bottom-left-radius: 7px;
        subcontrol-position: left;
        subcontrol-origin: margin;
    }}
    QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {{
            background: none;
    }}
    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {{
            background: none;
    }}
    QScrollBar:vertical {{
        border: none;
        background: rgb{COLOR_06};
        width: 14px;
        margin: 21px 0 21px 0;
        border-radius: 0px;
    }}
    QScrollBar::handle:vertical {{	
        background: rgb{COLOR_11};
        min-height: 25px;
        border-radius: 7px
    }}
    QScrollBar::add-line:vertical {{
        border: none;
        background: rgb{COLOR_306};
        height: 20px;
        border-bottom-left-radius: 7px;
        border-bottom-right-radius: 7px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }}
    QScrollBar::sub-line:vertical {{
        border: none;
        background: rgb{COLOR_306};
        height: 20px;
        border-top-left-radius: 7px;
        border-top-right-radius: 7px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }}
    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {{
        background: none;
    }}
    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
        background: none;
    }}
    
    /* ######### CHECKBOX ######### */
    QCheckBox::indicator {{
        border: 3px solid rgb{COLOR_06};
        width: 15px;
        height: 15px;
        border-radius: 10px;
        background: rgb{COLOR_105};
    }}
    QCheckBox::indicator:hover {{
        border: 3px solid rgb{COLOR_07};
    }}
    QCheckBox::indicator:checked {{
        background: 3px solid rgb{COLOR_06};
        border: 3px solid rgb{COLOR_06};	
        background-image: url(:/16x16/icons/16x16/cil-check-alt.png);
    }}
    
    /* ######### RADIO BUTTON ######### */
    QRadioButton::indicator {{
        border: 3px solid rgb{COLOR_06};
        width: 15px;
        height: 15px;
        border-radius: 10px;
        background: rgb{COLOR_105};
    }}
    QRadioButton::indicator:hover {{
        border: 3px solid rgb{COLOR_07};
    }}
    QRadioButton::indicator:checked {{
        background: 3px solid rgb{COLOR_13};
        border: 3px solid rgb{COLOR_06};	
    }}
    
    /* ######### COMBOBOX ######### */
    QComboBox{{
        background-color: rgb{COLOR_01};
        border-radius: 5px;
        border: 2px solid rgb{COLOR_01};
        padding: 5px;
        padding-left: 10px;
    }}
    QComboBox:hover{{
        border: 2px solid rgb{COLOR_307};
    }}
    QComboBox::drop-down {{
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 25px; 
        border-left-width: 3px;
        border-left-color: rgba{COLOR_04a};
        border-left-style: solid;
        border-top-right-radius: 3px;
        border-bottom-right-radius: 3px;	
        background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);
        background-position: center;
        background-repeat: no-reperat;
    }}
    QComboBox QAbstractItemView {{
        color: rgb{COLOR_11};	
        background-color: rgb{COLOR_01};
        padding: 10px;
        selection-background-color: rgb{COLOR_04};
    }}
    
    /* ######### SLIDERS ######### */
    QSlider::groove:horizontal {{
        border-radius: 9px;
        height: 18px;
        margin: 0px;
        background-color: rgb{COLOR_06};
    }}
    QSlider::groove:horizontal:hover {{
        background-color: rgb{COLOR_206};
    }}
    QSlider::handle:horizontal {{
        background-color: rgb{COLOR_11};
        border: none;
        height: 18px;
        width: 18px;
        margin: 0px;
        border-radius: 9px;
    }}
    QSlider::handle:horizontal:hover {{
        background-color: rgb{COLOR_15};
    }}
    QSlider::handle:horizontal:pressed {{
        background-color: rgb{COLOR_08};
    }}
    
    QSlider::groove:vertical {{
        border-radius: 9px;
        width: 18px;
        margin: 0px;
        background-color: rgb{COLOR_06};
    }}
    QSlider::groove:vertical:hover {{
        background-color: rgb{COLOR_206};
    }}
    QSlider::handle:vertical {{
        background-color: rgb{COLOR_11};
        border: none;
        height: 18px;
        width: 18px;
        margin: 0px;
        border-radius: 9px;
    }}
    QSlider::handle:vertical:hover {{
        background-color: rgb{COLOR_15};
    }}
    QSlider::handle:vertical:pressed {{
        background-color: rgb{COLOR_08};
    }}
    
    """
    ########################################################
    style_btn_toggle_menu = f"""
    QPushButton {{
        background-image: url(:/24x24/icons/24x24/cil-menu.png);
        background-position: center;
        background-repeat: no-reperat;
        border: none;
        background-color: rgb{COLOR_01};
    }}
    QPushButton:hover {{
        background-color: rgb{COLOR_02};
    }}
    QPushButton:pressed {{
        background-color: rgb{COLOR_11};
    }}
    """

    style_frame_toggle = f"background-color: rgb{COLOR_01};"

    style_btn_minimize = f"""
    QPushButton {{
    	border: none;
    	background-color: transparent;
    }}
    QPushButton:hover {{
    	background-color: rgb{COLOR_06};
    }}
    QPushButton:pressed {{
    	background-color: rgb{COLOR_11};
    }}
    """

    style_btn_maximize_restore = f"""
    QPushButton {{
    	border: none;
    	background-color: transparent;
    }}
    QPushButton:hover {{
    	background-color: rgb{COLOR_06};
    }}
    QPushButton:pressed {{
    	background-color: rgb{COLOR_11};
    }}
    """

    style_btn_close = f"""
    QPushButton {{
    	border: none;
    	background-color: transparent;
    }}
    QPushButton:hover {{
    	background-color: rgb{COLOR_06};
    }}
    QPushButton:pressed {{
    	background-color: rgb{COLOR_11};
    }}
    """

    # QFrame
    style_frame_top_info = f"background-color: rgb{COLOR_04};"

    # QLabel
    style_label_top_info = f"color: rgb{COLOR_14}; "

    ###################################################

    style_label_user_icon = f"""
    QLabel {{
        border-radius: 30px;
        background-color: rgb{COLOR_105};
        border: 5px solid rgb{COLOR_04};
        background-position: center;
        background-repeat: no-repeat;
    }}
    """

    style_frame_content_right = f"background-color: rgb{COLOR_105};"

    # QFrame
    style_frame = "border-radius: 5px;"
    style_frame_div_content_1 = f"""
        background-color: rgb{COLOR_104}; 
        border-radius: 5px;
    """

    style_frame_title_wid_1 = f"background-color: rgb{COLOR_04};"

    # QLineEdit
    style_lineEdit = f"""
    QLineEdit {{
    	background-color: rgb{COLOR_01};
    	border-radius: 5px;
    	border: 2px solid rgb{COLOR_01};
    	padding-left: 10px;
    }}
    QLineEdit:hover {{
    	border: 2px solid rgb{COLOR_307};
    }}
    QLineEdit:focus {{
    	border: 2px solid rgb{COLOR_12};
    }}
    """

    style_pushButton = f"""
    QPushButton {{
    	border: 2px solid rgb{COLOR_06};
    	border-radius: 5px;	
    	background-color: rgb{COLOR_06};
    }}
    QPushButton:hover {{
    	background-color: rgb{COLOR_107};
    	border: 2px solid rgb{COLOR_207};
    }}
    QPushButton:pressed {{
    	background-color: rgb{COLOR_03};
    	border: 2px solid rgb{COLOR_05};
    }}
    """

    style_labelVersion_3 = f"color: rgb{COLOR_14};"

    style_frame_2 = f"background-color: rgb{COLOR_04}; border-radius: 5px;"

    style_verticalScrollBar = f"""
    QScrollBar:vertical {{
    	border: none;
        background: rgb{COLOR_06};
        width: 14px;
        margin: 21px 0 21px 0;
    	border-radius: 0px;
    }}
    """

    style_scrollArea = f"""
    QScrollArea {{
        border: none;
    	border-radius: 0px;
    }}
    QScrollBar:horizontal {{
        border: none;
        background: rgb{COLOR_06};
        height: 14px;
        margin: 0px 21px 0 21px;
    	border-radius: 0px;
    }}
    QScrollBar:vertical {{
    	border: none;
        background: rgb{COLOR_06};
        width: 14px;
        margin: 21px 0 21px 0;
    	border-radius: 0px;
    }}
    """

    style_plainTextEdit = f"""
    QPlainTextEdit {{
    	background-color: rgb{COLOR_01};
    	border-radius: 5px;
    	padding: 10px;
    }}
    QPlainTextEdit:hover {{
    	border: 2px solid rgb{COLOR_307};
    }}
    QPlainTextEdit:focus {{
    	border: 2px solid rgb{COLOR_12};
    }}
    """

    style_comboBox = f"""
    QComboBox{{
    	background-color: rgb{COLOR_01};
    	border-radius: 5px;
    	border: 2px solid rgb{COLOR_01};
    	padding: 5px;
    	padding-left: 10px;
    }}
    QComboBox:hover{{
    	border: 2px solid rgb{COLOR_307};
    }}
    QComboBox QAbstractItemView {{
    	color: rgb{COLOR_11};	
    	background-color: rgb{COLOR_01};
    	padding: 10px;
    	selection-background-color: rgb{COLOR_04};
    }}
    """

    style_horizontalScrollBar = f"""
    QScrollBar:horizontal {{
        border: none;
        background: rgb{COLOR_06};
        height: 14px;
        margin: 0px 21px 0 21px;
    	border-radius: 0px;
    }}
    """

    style_commandLinkButton = f"""
    QCommandLinkButton {{
    	color: rgb{COLOR_11};
    	border-radius: 5px;
    	padding: 5px;
    }}
    QCommandLinkButton:hover {{
    	color: rgb{WHITE_01};
    	background-color: rgb{COLOR_105};
    }}
    QCommandLinkButton:pressed {{
    	color: rgb{WHITE_01};
    	background-color: rgb{COLOR_106};
    }}
    """

    style_tableWidget = f"""
    QTableWidget {{	
    	background-color: rgb{COLOR_04};
    	padding: 10px;
    	border-radius: 5px;
    	gridline-color: rgb{COLOR_105};
    	border-bottom: 1px solid rgb{COLOR_105};
    }}
    QTableWidget::item{{
    	border-color: rgb{COLOR_105};
    	padding-left: 5px;
    	padding-right: 5px;
    	gridline-color: rgb{COLOR_105};
    }}
    QTableWidget::item:selected{{
    	background-color: rgb{COLOR_11};
    }}
    QScrollBar:horizontal {{
        border: none;
        background: rgb{COLOR_06};
        height: 14px;
        margin: 0px 21px 0 21px;
    	border-radius: 0px;
    }}
    QScrollBar:vertical {{
    	border: none;
        background: rgb{COLOR_06};
        width: 14px;
        margin: 21px 0 21px 0;
    	border-radius: 0px;
    }}
    QHeaderView::section{{
    	Background-color: rgb{COLOR_04};
    	max-width: 30px;
    	border: 1px solid rgb{COLOR_105};
    	border-style: none;
        border-bottom: 1px solid rgb{COLOR_105};
        border-right: 1px solid rgb{COLOR_105};
    }}
    
    QTableWidget::horizontalHeader {{
    	background-color: rgb{COLOR_09};
    }}
    QHeaderView::section:horizontal
    {{
        border: 1px solid rgb{COLOR_102};
    	background-color: rgb{COLOR_01};
    	padding: 3px;
    	border-top-left-radius: 7px;
        border-top-right-radius: 7px;
    }}
    QHeaderView::section:vertical
    {{
        border: 1px solid rgb{COLOR_105};
    }}
    """

    style_frame_grip = f"background-color: rgb{COLOR_02};"
    style_label_credits = f"color: rgb{COLOR_14};"

    style_label_version = f"color: rgb{COLOR_14};"
    style_frame_size_grip = f"""
    QSizeGrip {{
    	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);
    	background-position: center;
    	background-repeat: no-reperat;
    }}
    """
