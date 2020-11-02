# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1324, 849)
        Form.setStyleSheet("background-color: white")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1330, 840))
        self.scrollArea.setMinimumSize(QtCore.QSize(1330, 840))
        self.scrollArea.setMaximumSize(QtCore.QSize(1330, 840))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.container_widget = QtWidgets.QWidget()
        self.container_widget.setGeometry(QtCore.QRect(0, 0, 1328, 838))
        self.container_widget.setObjectName("container_widget")
        self.main_menu_tab = QtWidgets.QTabWidget(self.container_widget)
        self.main_menu_tab.setEnabled(True)
        self.main_menu_tab.setGeometry(QtCore.QRect(29, 67, 1291, 781))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_menu_tab.sizePolicy().hasHeightForWidth())
        self.main_menu_tab.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.main_menu_tab.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.main_menu_tab.setFont(font)
        self.main_menu_tab.setAutoFillBackground(False)
        self.main_menu_tab.setStyleSheet("background-color: white;\n"
"margin: 0px;\n"
"padding:0px;\n"
"border: 0px;")
        self.main_menu_tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.main_menu_tab.setTabBarAutoHide(True)
        self.main_menu_tab.setObjectName("main_menu_tab")
        self.main_menu_acquisition_tab = QtWidgets.QWidget()
        self.main_menu_acquisition_tab.setObjectName("main_menu_acquisition_tab")
        self.detector_frame = QtWidgets.QFrame(self.main_menu_acquisition_tab)
        self.detector_frame.setGeometry(QtCore.QRect(43, 77, 241, 141))
        self.detector_frame.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 4ps;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;")
        self.detector_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.detector_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.detector_frame.setObjectName("detector_frame")
        self.spectrometer_name_input = QtWidgets.QLineEdit(self.main_menu_acquisition_tab)
        self.spectrometer_name_input.setGeometry(QtCore.QRect(326, 251, 181, 21))
        self.spectrometer_name_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrometer_name_input.setObjectName("spectrometer_name_input")
        self.load_acquisition_settings_button = QtWidgets.QPushButton(self.main_menu_acquisition_tab)
        self.load_acquisition_settings_button.setGeometry(QtCore.QRect(42, 20, 71, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.load_acquisition_settings_button.setFont(font)
        self.load_acquisition_settings_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.load_acquisition_settings_button.setObjectName("load_acquisition_settings_button")
        self.image_frame = QtWidgets.QFrame(self.main_menu_acquisition_tab)
        self.image_frame.setGeometry(QtCore.QRect(300, 77, 231, 141))
        self.image_frame.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 4ps;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;")
        self.image_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_frame.setObjectName("image_frame")
        self.image_settings_label = QtWidgets.QLabel(self.main_menu_acquisition_tab)
        self.image_settings_label.setGeometry(QtCore.QRect(370, 69, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.image_settings_label.setFont(font)
        self.image_settings_label.setStyleSheet("color: #24262b;")
        self.image_settings_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_settings_label.setObjectName("image_settings_label")
        self.spectrum_settings_label = QtWidgets.QLabel(self.main_menu_acquisition_tab)
        self.spectrum_settings_label.setGeometry(QtCore.QRect(100, 231, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.spectrum_settings_label.setFont(font)
        self.spectrum_settings_label.setStyleSheet("color: #24262b;")
        self.spectrum_settings_label.setAlignment(QtCore.Qt.AlignCenter)
        self.spectrum_settings_label.setObjectName("spectrum_settings_label")
        self.spectrometer_name_label = QtWidgets.QLabel(self.main_menu_acquisition_tab)
        self.spectrometer_name_label.setGeometry(QtCore.QRect(340, 230, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.spectrometer_name_label.setFont(font)
        self.spectrometer_name_label.setStyleSheet("color: #24262b;")
        self.spectrometer_name_label.setObjectName("spectrometer_name_label")
        self.detector_settings_label = QtWidgets.QLabel(self.main_menu_acquisition_tab)
        self.detector_settings_label.setGeometry(QtCore.QRect(119, 69, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.detector_settings_label.setFont(font)
        self.detector_settings_label.setStyleSheet("color: #24262b;")
        self.detector_settings_label.setAlignment(QtCore.Qt.AlignCenter)
        self.detector_settings_label.setObjectName("detector_settings_label")
        self.save_acquisition_settings_button = QtWidgets.QPushButton(self.main_menu_acquisition_tab)
        self.save_acquisition_settings_button.setGeometry(QtCore.QRect(114, 20, 71, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.save_acquisition_settings_button.setFont(font)
        self.save_acquisition_settings_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.save_acquisition_settings_button.setObjectName("save_acquisition_settings_button")
        self.spectrometer_name_frame = QtWidgets.QFrame(self.main_menu_acquisition_tab)
        self.spectrometer_name_frame.setGeometry(QtCore.QRect(300, 240, 231, 51))
        self.spectrometer_name_frame.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 4ps;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;")
        self.spectrometer_name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spectrometer_name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spectrometer_name_frame.setObjectName("spectrometer_name_frame")
        self.apply_acquisition_settings_button = QtWidgets.QPushButton(self.main_menu_acquisition_tab)
        self.apply_acquisition_settings_button.setGeometry(QtCore.QRect(302, 317, 121, 41))
        self.apply_acquisition_settings_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.apply_acquisition_settings_button.setObjectName("apply_acquisition_settings_button")
        self.spectrum_frame = QtWidgets.QFrame(self.main_menu_acquisition_tab)
        self.spectrum_frame.setGeometry(QtCore.QRect(43, 240, 241, 171))
        self.spectrum_frame.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 4ps;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;")
        self.spectrum_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spectrum_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spectrum_frame.setObjectName("spectrum_frame")
        self.live_button = QtWidgets.QPushButton(self.main_menu_acquisition_tab)
        self.live_button.setGeometry(QtCore.QRect(440, 318, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.live_button.setFont(font)
        self.live_button.setStyleSheet("background-color:#14274e;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.live_button.setObjectName("live_button")
        self.image_label = QtWidgets.QLabel(self.main_menu_acquisition_tab)
        self.image_label.setGeometry(QtCore.QRect(700, 77, 541, 331))
        self.image_label.setMaximumSize(QtCore.QSize(800, 16777215))
        self.image_label.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 4ps;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;")
        self.image_label.setText("")
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.main_menu_acquisition_tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(216, 253, 61, 151))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.spectrum_vertical_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.spectrum_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.spectrum_vertical_layout.setSpacing(0)
        self.spectrum_vertical_layout.setObjectName("spectrum_vertical_layout")
        self.spectrum_rotation_global_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.spectrum_rotation_global_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_rotation_global_input.setObjectName("spectrum_rotation_global_input")
        self.spectrum_vertical_layout.addWidget(self.spectrum_rotation_global_input)
        self.spectrum_rotation_spectrum_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.spectrum_rotation_spectrum_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_rotation_spectrum_input.setObjectName("spectrum_rotation_spectrum_input")
        self.spectrum_vertical_layout.addWidget(self.spectrum_rotation_spectrum_input)
        self.spectrum_start_x_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.spectrum_start_x_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_start_x_input.setObjectName("spectrum_start_x_input")
        self.spectrum_vertical_layout.addWidget(self.spectrum_start_x_input)
        self.spectrum_stop_x_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.spectrum_stop_x_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_stop_x_input.setObjectName("spectrum_stop_x_input")
        self.spectrum_vertical_layout.addWidget(self.spectrum_stop_x_input)
        self.spectrum_line_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.spectrum_line_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_line_input.setObjectName("spectrum_line_input")
        self.spectrum_vertical_layout.addWidget(self.spectrum_line_input)
        self.spectrum_lines_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.spectrum_lines_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_lines_input.setObjectName("spectrum_lines_input")
        self.spectrum_vertical_layout.addWidget(self.spectrum_lines_input)
        self.gridLayoutWidget = QtWidgets.QWidget(self.main_menu_acquisition_tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(56, 90, 221, 112))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.detector_grid_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.detector_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.detector_grid_layout.setSpacing(0)
        self.detector_grid_layout.setObjectName("detector_grid_layout")
        self.detector_width_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.detector_width_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.detector_width_input.setObjectName("detector_width_input")
        self.detector_grid_layout.addWidget(self.detector_width_input, 3, 1, 1, 1)
        self.detector_integration_time_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.detector_integration_time_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.detector_integration_time_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.detector_integration_time_label.setObjectName("detector_integration_time_label")
        self.detector_grid_layout.addWidget(self.detector_integration_time_label, 0, 0, 1, 1)
        self.detector_gain_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.detector_gain_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.detector_gain_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.detector_gain_label.setObjectName("detector_gain_label")
        self.detector_grid_layout.addWidget(self.detector_gain_label, 2, 0, 1, 1)
        self.detector_averages_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.detector_averages_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.detector_averages_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.detector_averages_label.setObjectName("detector_averages_label")
        self.detector_grid_layout.addWidget(self.detector_averages_label, 1, 0, 1, 1)
        self.detector_gain_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.detector_gain_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.detector_gain_input.setObjectName("detector_gain_input")
        self.detector_grid_layout.addWidget(self.detector_gain_input, 0, 1, 1, 1)
        self.detector_averages_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.detector_averages_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.detector_averages_input.setObjectName("detector_averages_input")
        self.detector_grid_layout.addWidget(self.detector_averages_input, 1, 1, 1, 1)
        self.detector_height_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.detector_height_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.detector_height_input.setObjectName("detector_height_input")
        self.detector_grid_layout.addWidget(self.detector_height_input, 3, 3, 1, 1)
        self.detector_resolution_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.detector_resolution_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.detector_resolution_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.detector_resolution_label.setObjectName("detector_resolution_label")
        self.detector_grid_layout.addWidget(self.detector_resolution_label, 3, 0, 1, 1)
        self.detector_integration_time_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.detector_integration_time_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.detector_integration_time_input.setObjectName("detector_integration_time_input")
        self.detector_grid_layout.addWidget(self.detector_integration_time_input, 2, 1, 1, 1)
        self.detector_resolution_x_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.detector_resolution_x_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.detector_resolution_x_label.setAlignment(QtCore.Qt.AlignCenter)
        self.detector_resolution_x_label.setObjectName("detector_resolution_x_label")
        self.detector_grid_layout.addWidget(self.detector_resolution_x_label, 3, 2, 1, 1)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.main_menu_acquisition_tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(92, 253, 121, 151))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.spectrum_vertical_layout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.spectrum_vertical_layout_2.setContentsMargins(0, 0, 0, 0)
        self.spectrum_vertical_layout_2.setSpacing(0)
        self.spectrum_vertical_layout_2.setObjectName("spectrum_vertical_layout_2")
        self.spectrum_rotation_global_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.spectrum_rotation_global_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.spectrum_rotation_global_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spectrum_rotation_global_label.setObjectName("spectrum_rotation_global_label")
        self.spectrum_vertical_layout_2.addWidget(self.spectrum_rotation_global_label)
        self.spectrum_rotation_spectrum_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.spectrum_rotation_spectrum_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.spectrum_rotation_spectrum_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spectrum_rotation_spectrum_label.setObjectName("spectrum_rotation_spectrum_label")
        self.spectrum_vertical_layout_2.addWidget(self.spectrum_rotation_spectrum_label)
        self.spectrum_start_x_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.spectrum_start_x_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.spectrum_start_x_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spectrum_start_x_label.setObjectName("spectrum_start_x_label")
        self.spectrum_vertical_layout_2.addWidget(self.spectrum_start_x_label)
        self.spectrum_stop_x_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.spectrum_stop_x_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.spectrum_stop_x_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spectrum_stop_x_label.setObjectName("spectrum_stop_x_label")
        self.spectrum_vertical_layout_2.addWidget(self.spectrum_stop_x_label)
        self.spectrum_line_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.spectrum_line_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px;\n"
"\n"
"")
        self.spectrum_line_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spectrum_line_label.setObjectName("spectrum_line_label")
        self.spectrum_vertical_layout_2.addWidget(self.spectrum_line_label)
        self.spectrum_lines_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.spectrum_lines_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px;\n"
"")
        self.spectrum_lines_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spectrum_lines_label.setObjectName("spectrum_lines_label")
        self.spectrum_vertical_layout_2.addWidget(self.spectrum_lines_label)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.main_menu_acquisition_tab)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(320, 90, 160, 101))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.image_vertical_layout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.image_vertical_layout_2.setContentsMargins(0, 0, 0, 0)
        self.image_vertical_layout_2.setSpacing(0)
        self.image_vertical_layout_2.setObjectName("image_vertical_layout_2")
        self.image_scale_cropped_label = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.image_scale_cropped_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.image_scale_cropped_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.image_scale_cropped_label.setObjectName("image_scale_cropped_label")
        self.image_vertical_layout_2.addWidget(self.image_scale_cropped_label)
        self.image_crop_label = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.image_crop_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.image_crop_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.image_crop_label.setObjectName("image_crop_label")
        self.image_vertical_layout_2.addWidget(self.image_crop_label)
        self.image_scale_overview_label = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.image_scale_overview_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.image_scale_overview_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.image_scale_overview_label.setObjectName("image_scale_overview_label")
        self.image_vertical_layout_2.addWidget(self.image_scale_overview_label)
        self.image_camera_no_label = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.image_camera_no_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.image_camera_no_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.image_camera_no_label.setObjectName("image_camera_no_label")
        self.image_vertical_layout_2.addWidget(self.image_camera_no_label)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.main_menu_acquisition_tab)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(483, 90, 41, 101))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.image_vertical_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.image_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.image_vertical_layout.setSpacing(0)
        self.image_vertical_layout.setObjectName("image_vertical_layout")
        self.image_scale_overview_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.image_scale_overview_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.image_scale_overview_input.setObjectName("image_scale_overview_input")
        self.image_vertical_layout.addWidget(self.image_scale_overview_input)
        self.image_scale_cropped_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.image_scale_cropped_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.image_scale_cropped_input.setObjectName("image_scale_cropped_input")
        self.image_vertical_layout.addWidget(self.image_scale_cropped_input)
        self.image_crop_box = QtWidgets.QCheckBox(self.verticalLayoutWidget_7)
        self.image_crop_box.setEnabled(True)
        self.image_crop_box.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.image_crop_box.setText("")
        self.image_crop_box.setCheckable(True)
        self.image_crop_box.setChecked(False)
        self.image_crop_box.setObjectName("image_crop_box")
        self.image_vertical_layout.addWidget(self.image_crop_box, 0, QtCore.Qt.AlignHCenter)
        self.image_camera_no_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.image_camera_no_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.image_camera_no_input.setObjectName("image_camera_no_input")
        self.image_vertical_layout.addWidget(self.image_camera_no_input)
        self.detector_frame.raise_()
        self.spectrometer_name_frame.raise_()
        self.spectrum_frame.raise_()
        self.image_frame.raise_()
        self.spectrometer_name_input.raise_()
        self.load_acquisition_settings_button.raise_()
        self.image_settings_label.raise_()
        self.spectrum_settings_label.raise_()
        self.spectrometer_name_label.raise_()
        self.detector_settings_label.raise_()
        self.save_acquisition_settings_button.raise_()
        self.apply_acquisition_settings_button.raise_()
        self.live_button.raise_()
        self.image_label.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.gridLayoutWidget.raise_()
        self.verticalLayoutWidget_4.raise_()
        self.verticalLayoutWidget_8.raise_()
        self.verticalLayoutWidget_7.raise_()
        self.main_menu_tab.addTab(self.main_menu_acquisition_tab, "")
        self.main_menu_calibration_tab = QtWidgets.QWidget()
        self.main_menu_calibration_tab.setObjectName("main_menu_calibration_tab")
        self.experiment_flow_frame_2 = QtWidgets.QFrame(self.main_menu_calibration_tab)
        self.experiment_flow_frame_2.setGeometry(QtCore.QRect(43, 80, 491, 331))
        self.experiment_flow_frame_2.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 4ps;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;")
        self.experiment_flow_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.experiment_flow_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.experiment_flow_frame_2.setObjectName("experiment_flow_frame_2")
        self.clear_experiment_button_2 = QtWidgets.QPushButton(self.experiment_flow_frame_2)
        self.clear_experiment_button_2.setGeometry(QtCore.QRect(310, 290, 181, 41))
        self.clear_experiment_button_2.setStyleSheet("color: #24262b;")
        self.clear_experiment_button_2.setObjectName("clear_experiment_button_2")
        self.export_experiment_button_2 = QtWidgets.QPushButton(self.experiment_flow_frame_2)
        self.export_experiment_button_2.setGeometry(QtCore.QRect(0, 290, 311, 41))
        self.export_experiment_button_2.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.export_experiment_button_2.setObjectName("export_experiment_button_2")
        self.experiment_menu_transmission_button_2 = QtWidgets.QPushButton(self.main_menu_calibration_tab)
        self.experiment_menu_transmission_button_2.setGeometry(QtCore.QRect(140, 64, 141, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.experiment_menu_transmission_button_2.setFont(font)
        self.experiment_menu_transmission_button_2.setStyleSheet("color: #24262b;\n"
"border-bottom-width: 2px;\n"
"border-color: #24262b;\n"
"border-style:solid;\n"
"")
        self.experiment_menu_transmission_button_2.setObjectName("experiment_menu_transmission_button_2")
        self.experiment_menu_emission_button_2 = QtWidgets.QPushButton(self.main_menu_calibration_tab)
        self.experiment_menu_emission_button_2.setGeometry(QtCore.QRect(290, 64, 141, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.experiment_menu_emission_button_2.setFont(font)
        self.experiment_menu_emission_button_2.setStyleSheet("color: #24262b;\n"
"border-bottom-width: 0px;\n"
"border-color: #24262b;\n"
"border-style:solid;")
        self.experiment_menu_emission_button_2.setObjectName("experiment_menu_emission_button_2")
        self.experiment_menu_frame_2 = QtWidgets.QFrame(self.main_menu_calibration_tab)
        self.experiment_menu_frame_2.setGeometry(QtCore.QRect(160, 66, 241, 31))
        self.experiment_menu_frame_2.setStyleSheet("border-width: 0px;\n"
"border-style:solid;\n"
"")
        self.experiment_menu_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.experiment_menu_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.experiment_menu_frame_2.setObjectName("experiment_menu_frame_2")
        self.experiment_flow_frame_2.raise_()
        self.experiment_menu_frame_2.raise_()
        self.experiment_menu_emission_button_2.raise_()
        self.experiment_menu_transmission_button_2.raise_()
        self.main_menu_tab.addTab(self.main_menu_calibration_tab, "")
        self.main_menu_experiment_tab = QtWidgets.QWidget()
        self.main_menu_experiment_tab.setObjectName("main_menu_experiment_tab")
        self.experiment_flow_frame = QtWidgets.QFrame(self.main_menu_experiment_tab)
        self.experiment_flow_frame.setGeometry(QtCore.QRect(43, 80, 491, 331))
        self.experiment_flow_frame.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 4ps;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;")
        self.experiment_flow_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.experiment_flow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.experiment_flow_frame.setObjectName("experiment_flow_frame")
        self.clear_experiment_button = QtWidgets.QPushButton(self.experiment_flow_frame)
        self.clear_experiment_button.setGeometry(QtCore.QRect(310, 290, 181, 41))
        self.clear_experiment_button.setStyleSheet("color: #24262b;")
        self.clear_experiment_button.setObjectName("clear_experiment_button")
        self.export_experiment_button = QtWidgets.QPushButton(self.experiment_flow_frame)
        self.export_experiment_button.setGeometry(QtCore.QRect(0, 290, 311, 41))
        self.export_experiment_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.export_experiment_button.setObjectName("export_experiment_button")
        self.experiment_menu_frame = QtWidgets.QFrame(self.main_menu_experiment_tab)
        self.experiment_menu_frame.setGeometry(QtCore.QRect(163, 60, 241, 31))
        self.experiment_menu_frame.setStyleSheet("border-width: 0px;\n"
"border-style:solid;\n"
"")
        self.experiment_menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.experiment_menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.experiment_menu_frame.setObjectName("experiment_menu_frame")
        self.experiment_menu_emission_button = QtWidgets.QPushButton(self.main_menu_experiment_tab)
        self.experiment_menu_emission_button.setGeometry(QtCore.QRect(290, 64, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.experiment_menu_emission_button.setFont(font)
        self.experiment_menu_emission_button.setStyleSheet("color: #24262b;\n"
"border-bottom-width: 0px;\n"
"border-color: #24262b;\n"
"border-style:solid;")
        self.experiment_menu_emission_button.setObjectName("experiment_menu_emission_button")
        self.experiment_menu_transmission_button = QtWidgets.QPushButton(self.main_menu_experiment_tab)
        self.experiment_menu_transmission_button.setGeometry(QtCore.QRect(168, 64, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.experiment_menu_transmission_button.setFont(font)
        self.experiment_menu_transmission_button.setStyleSheet("color: #24262b;\n"
"border-bottom-width: 2px;\n"
"border-color: #24262b;\n"
"border-style:solid;\n"
"")
        self.experiment_menu_transmission_button.setObjectName("experiment_menu_transmission_button")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.main_menu_experiment_tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 110, 391, 238))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.experiment_flow_horizontal_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.experiment_flow_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.experiment_flow_horizontal_layout.setObjectName("experiment_flow_horizontal_layout")
        self.experiment_flow_vertical_layout = QtWidgets.QVBoxLayout()
        self.experiment_flow_vertical_layout.setObjectName("experiment_flow_vertical_layout")
        self.experiment_no_1_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.experiment_no_1_label.setFont(font)
        self.experiment_no_1_label.setStyleSheet("color:#14274e")
        self.experiment_no_1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.experiment_no_1_label.setObjectName("experiment_no_1_label")
        self.experiment_flow_vertical_layout.addWidget(self.experiment_no_1_label)
        self.experiment_no_2_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.experiment_no_2_label.setFont(font)
        self.experiment_no_2_label.setStyleSheet("color:#14274e")
        self.experiment_no_2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.experiment_no_2_label.setObjectName("experiment_no_2_label")
        self.experiment_flow_vertical_layout.addWidget(self.experiment_no_2_label)
        self.experiment_no_3_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.experiment_no_3_label.setFont(font)
        self.experiment_no_3_label.setStyleSheet("color:#14274e")
        self.experiment_no_3_label.setAlignment(QtCore.Qt.AlignCenter)
        self.experiment_no_3_label.setObjectName("experiment_no_3_label")
        self.experiment_flow_vertical_layout.addWidget(self.experiment_no_3_label)
        self.experiment_flow_horizontal_layout.addLayout(self.experiment_flow_vertical_layout)
        self.experiment_flow_vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.experiment_flow_vertical_layout_2.setObjectName("experiment_flow_vertical_layout_2")
        self.acquire_dark_spectrum_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.acquire_dark_spectrum_button.setStyleSheet("background-color:#14274e;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;\n"
"padding: 15px;")
        self.acquire_dark_spectrum_button.setObjectName("acquire_dark_spectrum_button")
        self.experiment_flow_vertical_layout_2.addWidget(self.acquire_dark_spectrum_button, 0, QtCore.Qt.AlignVCenter)
        self.acquire_emission_spectrum_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.acquire_emission_spectrum_button.setStyleSheet("background-color:#14274e;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;\n"
"padding: 15px;")
        self.acquire_emission_spectrum_button.setObjectName("acquire_emission_spectrum_button")
        self.experiment_flow_vertical_layout_2.addWidget(self.acquire_emission_spectrum_button, 0, QtCore.Qt.AlignVCenter)
        self.acquire_reference_spectrum_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.acquire_reference_spectrum_button.setStyleSheet("background-color:#14274e;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;\n"
"padding: 15px;")
        self.acquire_reference_spectrum_button.setObjectName("acquire_reference_spectrum_button")
        self.experiment_flow_vertical_layout_2.addWidget(self.acquire_reference_spectrum_button, 0, QtCore.Qt.AlignVCenter)
        self.acquire_transmission_spectrum_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.acquire_transmission_spectrum_button.setStyleSheet("background-color:#14274e;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;\n"
"padding: 15px;")
        self.acquire_transmission_spectrum_button.setObjectName("acquire_transmission_spectrum_button")
        self.experiment_flow_vertical_layout_2.addWidget(self.acquire_transmission_spectrum_button, 0, QtCore.Qt.AlignVCenter)
        self.experiment_flow_horizontal_layout.addLayout(self.experiment_flow_vertical_layout_2)
        self.experiment_flow_vertical_layout_3 = QtWidgets.QVBoxLayout()
        self.experiment_flow_vertical_layout_3.setObjectName("experiment_flow_vertical_layout_3")
        self.check_label_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.check_label_1.setText("")
        self.check_label_1.setObjectName("check_label_1")
        self.experiment_flow_vertical_layout_3.addWidget(self.check_label_1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.check_label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.check_label_2.setText("")
        self.check_label_2.setObjectName("check_label_2")
        self.experiment_flow_vertical_layout_3.addWidget(self.check_label_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.check_label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.check_label_3.setText("")
        self.check_label_3.setObjectName("check_label_3")
        self.experiment_flow_vertical_layout_3.addWidget(self.check_label_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.experiment_flow_horizontal_layout.addLayout(self.experiment_flow_vertical_layout_3)
        self.calc_plot_3_frame = QtWidgets.QFrame(self.main_menu_experiment_tab)
        self.calc_plot_3_frame.setGeometry(QtCore.QRect(640, 420, 631, 341))
        self.calc_plot_3_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calc_plot_3_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calc_plot_3_frame.setObjectName("calc_plot_3_frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.calc_plot_3_frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 611, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.calc_plot_3_grid_layout = QtWidgets.QGridLayout(self.verticalLayoutWidget)
        self.calc_plot_3_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.calc_plot_3_grid_layout.setObjectName("calc_plot_3_grid_layout")
        self.calc_plot_3_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_3_label.setFont(font)
        self.calc_plot_3_label.setStyleSheet("color: #24262b;")
        self.calc_plot_3_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_3_label.setObjectName("calc_plot_3_label")
        self.calc_plot_3_grid_layout.addWidget(self.calc_plot_3_label, 6, 1, 1, 1)
        self.calc_plot_3_lambda_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_3_lambda_label.setFont(font)
        self.calc_plot_3_lambda_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_3_lambda_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_3_lambda_label.setWordWrap(False)
        self.calc_plot_3_lambda_label.setObjectName("calc_plot_3_lambda_label")
        self.calc_plot_3_grid_layout.addWidget(self.calc_plot_3_lambda_label, 8, 1, 1, 1)
        self.calc_plot_3_i_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_3_i_label.setFont(font)
        self.calc_plot_3_i_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_3_i_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_3_i_label.setWordWrap(False)
        self.calc_plot_3_i_label.setObjectName("calc_plot_3_i_label")
        self.calc_plot_3_grid_layout.addWidget(self.calc_plot_3_i_label, 7, 0, 1, 1)
        self.calc_plot_3 = PlotWidget(self.verticalLayoutWidget)
        self.calc_plot_3.setEnabled(False)
        self.calc_plot_3.setObjectName("calc_plot_3")
        self.calc_plot_3_grid_layout.addWidget(self.calc_plot_3, 7, 1, 1, 1)
        self.save_calc_plot_1_txt_button = QtWidgets.QPushButton(self.main_menu_experiment_tab)
        self.save_calc_plot_1_txt_button.setGeometry(QtCore.QRect(1219, 70, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_calc_plot_1_txt_button.setFont(font)
        self.save_calc_plot_1_txt_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.save_calc_plot_1_txt_button.setObjectName("save_calc_plot_1_txt_button")
        self.save_calc_plot_1_png_button = QtWidgets.QPushButton(self.main_menu_experiment_tab)
        self.save_calc_plot_1_png_button.setGeometry(QtCore.QRect(1176, 70, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_calc_plot_1_png_button.setFont(font)
        self.save_calc_plot_1_png_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.save_calc_plot_1_png_button.setObjectName("save_calc_plot_1_png_button")
        self.save_calc_plot_3_png_button = QtWidgets.QPushButton(self.main_menu_experiment_tab)
        self.save_calc_plot_3_png_button.setGeometry(QtCore.QRect(1176, 440, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_calc_plot_3_png_button.setFont(font)
        self.save_calc_plot_3_png_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.save_calc_plot_3_png_button.setObjectName("save_calc_plot_3_png_button")
        self.save_calc_plot_3_txt_button = QtWidgets.QPushButton(self.main_menu_experiment_tab)
        self.save_calc_plot_3_txt_button.setGeometry(QtCore.QRect(1219, 440, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_calc_plot_3_txt_button.setFont(font)
        self.save_calc_plot_3_txt_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.save_calc_plot_3_txt_button.setObjectName("save_calc_plot_3_txt_button")
        self.save_calc_plot_2_txt_button = QtWidgets.QPushButton(self.main_menu_experiment_tab)
        self.save_calc_plot_2_txt_button.setGeometry(QtCore.QRect(1219, 248, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_calc_plot_2_txt_button.setFont(font)
        self.save_calc_plot_2_txt_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.save_calc_plot_2_txt_button.setObjectName("save_calc_plot_2_txt_button")
        self.save_calc_plot_2_png_button = QtWidgets.QPushButton(self.main_menu_experiment_tab)
        self.save_calc_plot_2_png_button.setGeometry(QtCore.QRect(1176, 248, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_calc_plot_2_png_button.setFont(font)
        self.save_calc_plot_2_png_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.save_calc_plot_2_png_button.setObjectName("save_calc_plot_2_png_button")
        self.calc_plot_1_2_combo_frame = QtWidgets.QFrame(self.main_menu_experiment_tab)
        self.calc_plot_1_2_combo_frame.setGeometry(QtCore.QRect(640, 60, 631, 351))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calc_plot_1_2_combo_frame.sizePolicy().hasHeightForWidth())
        self.calc_plot_1_2_combo_frame.setSizePolicy(sizePolicy)
        self.calc_plot_1_2_combo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calc_plot_1_2_combo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calc_plot_1_2_combo_frame.setObjectName("calc_plot_1_2_combo_frame")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.calc_plot_1_2_combo_frame)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(9, 10, 611, 341))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.calc_plot_1_2_grid_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.calc_plot_1_2_grid_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.calc_plot_1_2_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.calc_plot_1_2_grid_layout.setObjectName("calc_plot_1_2_grid_layout")
        self.calc_plot_2_combo_label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_2_combo_label.setFont(font)
        self.calc_plot_2_combo_label.setStyleSheet("color: #24262b;")
        self.calc_plot_2_combo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_2_combo_label.setObjectName("calc_plot_2_combo_label")
        self.calc_plot_1_2_grid_layout.addWidget(self.calc_plot_2_combo_label, 5, 1, 1, 1)
        self.calc_plot_2_combo_i_label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_2_combo_i_label.setFont(font)
        self.calc_plot_2_combo_i_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_2_combo_i_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_2_combo_i_label.setWordWrap(False)
        self.calc_plot_2_combo_i_label.setObjectName("calc_plot_2_combo_i_label")
        self.calc_plot_1_2_grid_layout.addWidget(self.calc_plot_2_combo_i_label, 6, 0, 1, 1)
        self.calc_plot_1_combo_label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_1_combo_label.setFont(font)
        self.calc_plot_1_combo_label.setStyleSheet("color: #24262b;")
        self.calc_plot_1_combo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_1_combo_label.setObjectName("calc_plot_1_combo_label")
        self.calc_plot_1_2_grid_layout.addWidget(self.calc_plot_1_combo_label, 0, 1, 1, 1)
        self.calc_plot_1_combo_i_label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_1_combo_i_label.setFont(font)
        self.calc_plot_1_combo_i_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_1_combo_i_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_1_combo_i_label.setWordWrap(False)
        self.calc_plot_1_combo_i_label.setObjectName("calc_plot_1_combo_i_label")
        self.calc_plot_1_2_grid_layout.addWidget(self.calc_plot_1_combo_i_label, 1, 0, 1, 1)
        self.calc_plot_1_combo_lambda_label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.calc_plot_1_combo_lambda_label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_1_combo_lambda_label.setFont(font)
        self.calc_plot_1_combo_lambda_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_1_combo_lambda_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_1_combo_lambda_label.setWordWrap(False)
        self.calc_plot_1_combo_lambda_label.setObjectName("calc_plot_1_combo_lambda_label")
        self.calc_plot_1_2_grid_layout.addWidget(self.calc_plot_1_combo_lambda_label, 2, 1, 1, 1)
        self.calc_plot_2_combo_lambda_label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_2_combo_lambda_label.setFont(font)
        self.calc_plot_2_combo_lambda_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_2_combo_lambda_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_2_combo_lambda_label.setWordWrap(False)
        self.calc_plot_2_combo_lambda_label.setObjectName("calc_plot_2_combo_lambda_label")
        self.calc_plot_1_2_grid_layout.addWidget(self.calc_plot_2_combo_lambda_label, 7, 1, 1, 1)
        self.calc_plot_1_combo = PlotWidget(self.gridLayoutWidget_4)
        self.calc_plot_1_combo.setEnabled(False)
        self.calc_plot_1_combo.setObjectName("calc_plot_1_combo")
        self.calc_plot_1_2_grid_layout.addWidget(self.calc_plot_1_combo, 1, 1, 1, 1)
        self.calc_plot_2_combo = PlotWidget(self.gridLayoutWidget_4)
        self.calc_plot_2_combo.setEnabled(False)
        self.calc_plot_2_combo.setObjectName("calc_plot_2_combo")
        self.calc_plot_1_2_grid_layout.addWidget(self.calc_plot_2_combo, 6, 1, 1, 1)
        self.calc_plot_1_frame = QtWidgets.QFrame(self.main_menu_experiment_tab)
        self.calc_plot_1_frame.setGeometry(QtCore.QRect(640, 70, 631, 341))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calc_plot_1_frame.sizePolicy().hasHeightForWidth())
        self.calc_plot_1_frame.setSizePolicy(sizePolicy)
        self.calc_plot_1_frame.setStyleSheet("")
        self.calc_plot_1_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calc_plot_1_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calc_plot_1_frame.setObjectName("calc_plot_1_frame")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.calc_plot_1_frame)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(10, 0, 611, 341))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.calc_plot_1_grid_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.calc_plot_1_grid_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.calc_plot_1_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.calc_plot_1_grid_layout.setObjectName("calc_plot_1_grid_layout")
        self.calc_plot_1_i_label = QtWidgets.QLabel(self.gridLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_1_i_label.setFont(font)
        self.calc_plot_1_i_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_1_i_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_1_i_label.setWordWrap(False)
        self.calc_plot_1_i_label.setObjectName("calc_plot_1_i_label")
        self.calc_plot_1_grid_layout.addWidget(self.calc_plot_1_i_label, 1, 0, 1, 1)
        self.calc_plot_1_label = QtWidgets.QLabel(self.gridLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_1_label.setFont(font)
        self.calc_plot_1_label.setStyleSheet("color: #24262b;")
        self.calc_plot_1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_1_label.setObjectName("calc_plot_1_label")
        self.calc_plot_1_grid_layout.addWidget(self.calc_plot_1_label, 0, 1, 1, 1)
        self.calc_plot_1_lambda_label = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.calc_plot_1_lambda_label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_1_lambda_label.setFont(font)
        self.calc_plot_1_lambda_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_1_lambda_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_1_lambda_label.setWordWrap(False)
        self.calc_plot_1_lambda_label.setObjectName("calc_plot_1_lambda_label")
        self.calc_plot_1_grid_layout.addWidget(self.calc_plot_1_lambda_label, 2, 1, 1, 1)
        self.calc_plot_1 = PlotWidget(self.gridLayoutWidget_6)
        self.calc_plot_1.setEnabled(False)
        self.calc_plot_1.setObjectName("calc_plot_1")
        self.calc_plot_1_grid_layout.addWidget(self.calc_plot_1, 1, 1, 1, 1)
        self.calc_plot_2_frame = QtWidgets.QFrame(self.main_menu_experiment_tab)
        self.calc_plot_2_frame.setGeometry(QtCore.QRect(640, 60, 631, 351))
        self.calc_plot_2_frame.setStyleSheet("")
        self.calc_plot_2_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calc_plot_2_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calc_plot_2_frame.setObjectName("calc_plot_2_frame")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.calc_plot_2_frame)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 0, 611, 341))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.calc_plot_2_grid_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.calc_plot_2_grid_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.calc_plot_2_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.calc_plot_2_grid_layout.setObjectName("calc_plot_2_grid_layout")
        self.calc_plot_2_i_label = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_2_i_label.setFont(font)
        self.calc_plot_2_i_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_2_i_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_2_i_label.setWordWrap(False)
        self.calc_plot_2_i_label.setObjectName("calc_plot_2_i_label")
        self.calc_plot_2_grid_layout.addWidget(self.calc_plot_2_i_label, 3, 0, 1, 1)
        self.calc_plot_2_label = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_2_label.setFont(font)
        self.calc_plot_2_label.setStyleSheet("color: #24262b;")
        self.calc_plot_2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_2_label.setObjectName("calc_plot_2_label")
        self.calc_plot_2_grid_layout.addWidget(self.calc_plot_2_label, 2, 1, 1, 1)
        self.calc_plot_2_lambda_label = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_2_lambda_label.setFont(font)
        self.calc_plot_2_lambda_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_2_lambda_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_2_lambda_label.setWordWrap(False)
        self.calc_plot_2_lambda_label.setObjectName("calc_plot_2_lambda_label")
        self.calc_plot_2_grid_layout.addWidget(self.calc_plot_2_lambda_label, 4, 1, 1, 1)
        self.calc_plot_2 = PlotWidget(self.gridLayoutWidget_5)
        self.calc_plot_2.setEnabled(False)
        self.calc_plot_2.setObjectName("calc_plot_2")
        self.calc_plot_2_grid_layout.addWidget(self.calc_plot_2, 3, 1, 1, 1)
        self.calc_plot_2_frame.raise_()
        self.calc_plot_1_frame.raise_()
        self.calc_plot_1_2_combo_frame.raise_()
        self.experiment_flow_frame.raise_()
        self.experiment_menu_frame.raise_()
        self.experiment_menu_emission_button.raise_()
        self.experiment_menu_transmission_button.raise_()
        self.horizontalLayoutWidget.raise_()
        self.calc_plot_3_frame.raise_()
        self.save_calc_plot_1_txt_button.raise_()
        self.save_calc_plot_1_png_button.raise_()
        self.save_calc_plot_3_png_button.raise_()
        self.save_calc_plot_3_txt_button.raise_()
        self.save_calc_plot_2_txt_button.raise_()
        self.save_calc_plot_2_png_button.raise_()
        self.main_menu_tab.addTab(self.main_menu_experiment_tab, "")
        self.main_header_frame = QtWidgets.QFrame(self.container_widget)
        self.main_header_frame.setGeometry(QtCore.QRect(-7, 20, 1331, 91))
        self.main_header_frame.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #9ba4b4;\n"
"background-color:#14274e")
        self.main_header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_header_frame.setObjectName("main_header_frame")
        self.calibration_button = QtWidgets.QPushButton(self.container_widget)
        self.calibration_button.setGeometry(QtCore.QRect(576, 67, 140, 35))
        font = QtGui.QFont()
        font.setFamily("helvetica")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calibration_button.setFont(font)
        self.calibration_button.setStyleSheet("background-color:#14274e;\n"
"color:#f1f6f9;\n"
"border-radius: 0px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-bottom-width: 0px;\n"
"border-color: #f1f6f9;\n"
"font-family: helvetica;\n"
"")
        self.calibration_button.setObjectName("calibration_button")
        self.spec_streamer_label = QtWidgets.QLabel(self.container_widget)
        self.spec_streamer_label.setGeometry(QtCore.QRect(546, 22, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.spec_streamer_label.setFont(font)
        self.spec_streamer_label.setAutoFillBackground(False)
        self.spec_streamer_label.setStyleSheet("color:#f1f6f9;\n"
"border-width:0px;\n"
"background-color: #14274e")
        self.spec_streamer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.spec_streamer_label.setObjectName("spec_streamer_label")
        self.acquisition_button = QtWidgets.QPushButton(self.container_widget)
        self.acquisition_button.setGeometry(QtCore.QRect(443, 67, 100, 35))
        font = QtGui.QFont()
        font.setFamily("helvetica")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.acquisition_button.setFont(font)
        self.acquisition_button.setStyleSheet("background-color:#14274e;\n"
"color:#f1f6f9;\n"
"border-radius: 0px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-bottom-width: 2px;\n"
"border-color: #f1f6f9;\n"
"font-family: helvetica;\n"
"")
        self.acquisition_button.setObjectName("acquisition_button")
        self.raw_plot_frame = QtWidgets.QFrame(self.container_widget)
        self.raw_plot_frame.setGeometry(QtCore.QRect(16, 510, 551, 341))
        self.raw_plot_frame.setStyleSheet("outline-width: 0ps;\n"
"border-radius: 0px;\n"
"border-style: solid;\n"
"border-width: 0px;")
        self.raw_plot_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.raw_plot_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.raw_plot_frame.setObjectName("raw_plot_frame")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.raw_plot_frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(5, 19, 541, 311))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.raw_spectrum_grid_layout = QtWidgets.QGridLayout(self.verticalLayoutWidget_2)
        self.raw_spectrum_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.raw_spectrum_grid_layout.setObjectName("raw_spectrum_grid_layout")
        self.raw_plot_i_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.raw_plot_i_label.setFont(font)
        self.raw_plot_i_label.setStyleSheet("color: #9ba4b4;")
        self.raw_plot_i_label.setAlignment(QtCore.Qt.AlignCenter)
        self.raw_plot_i_label.setWordWrap(False)
        self.raw_plot_i_label.setObjectName("raw_plot_i_label")
        self.raw_spectrum_grid_layout.addWidget(self.raw_plot_i_label, 1, 0, 1, 1)
        self.raw_plot_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.raw_plot_label.setFont(font)
        self.raw_plot_label.setStyleSheet("color: #24262b;")
        self.raw_plot_label.setAlignment(QtCore.Qt.AlignCenter)
        self.raw_plot_label.setWordWrap(False)
        self.raw_plot_label.setObjectName("raw_plot_label")
        self.raw_spectrum_grid_layout.addWidget(self.raw_plot_label, 0, 1, 1, 1)
        self.raw_plot_lambda_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.raw_plot_lambda_label.setFont(font)
        self.raw_plot_lambda_label.setStyleSheet("color: #9ba4b4;")
        self.raw_plot_lambda_label.setAlignment(QtCore.Qt.AlignCenter)
        self.raw_plot_lambda_label.setWordWrap(False)
        self.raw_plot_lambda_label.setObjectName("raw_plot_lambda_label")
        self.raw_spectrum_grid_layout.addWidget(self.raw_plot_lambda_label, 2, 1, 1, 1)
        self.raw_plot = PlotWidget(self.verticalLayoutWidget_2)
        self.raw_plot.setObjectName("raw_plot")
        self.raw_spectrum_grid_layout.addWidget(self.raw_plot, 1, 1, 1, 1)
        self.spec_streamer_v_label = QtWidgets.QLabel(self.container_widget)
        self.spec_streamer_v_label.setGeometry(QtCore.QRect(734, 27, 31, 20))
        font = QtGui.QFont()
        font.setFamily("helvetica")
        self.spec_streamer_v_label.setFont(font)
        self.spec_streamer_v_label.setStyleSheet("background-color:#14274e;\n"
"font-family: helvetica;\n"
"color:#9ba4b4;")
        self.spec_streamer_v_label.setObjectName("spec_streamer_v_label")
        self.spec_tools_label = QtWidgets.QLabel(self.container_widget)
        self.spec_tools_label.setGeometry(QtCore.QRect(1210, 0, 141, 20))
        font = QtGui.QFont()
        font.setFamily("helvetica")
        self.spec_tools_label.setFont(font)
        self.spec_tools_label.setStyleSheet("background-color:white;\n"
"font-family: helvetica;\n"
"color:#14274e;")
        self.spec_tools_label.setOpenExternalLinks(True)
        self.spec_tools_label.setObjectName("spec_tools_label")
        self.experiment_button = QtWidgets.QPushButton(self.container_widget)
        self.experiment_button.setGeometry(QtCore.QRect(733, 67, 140, 35))
        font = QtGui.QFont()
        font.setFamily("helvetica")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.experiment_button.setFont(font)
        self.experiment_button.setStyleSheet("background-color:#14274e;\n"
"color:#f1f6f9;\n"
"border-radius: 0px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-bottom-width: 0px;\n"
"border-color: #f1f6f9;\n"
"font-family: helvetica;\n"
"\n"
"")
        self.experiment_button.setObjectName("experiment_button")
        self.save_raw_plot_txt_button = QtWidgets.QPushButton(self.container_widget)
        self.save_raw_plot_txt_button.setGeometry(QtCore.QRect(520, 530, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_raw_plot_txt_button.setFont(font)
        self.save_raw_plot_txt_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.save_raw_plot_txt_button.setObjectName("save_raw_plot_txt_button")
        self.save_raw_plot_png_button = QtWidgets.QPushButton(self.container_widget)
        self.save_raw_plot_png_button.setGeometry(QtCore.QRect(477, 530, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_raw_plot_png_button.setFont(font)
        self.save_raw_plot_png_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.save_raw_plot_png_button.setObjectName("save_raw_plot_png_button")
        self.scrollArea.setWidget(self.container_widget)

        self.retranslateUi(Form)
        self.main_menu_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.detector_gain_input, self.detector_averages_input)
        Form.setTabOrder(self.detector_averages_input, self.detector_integration_time_input)
        Form.setTabOrder(self.detector_integration_time_input, self.detector_width_input)
        Form.setTabOrder(self.detector_width_input, self.detector_height_input)
        Form.setTabOrder(self.detector_height_input, self.image_scale_overview_input)
        Form.setTabOrder(self.image_scale_overview_input, self.image_scale_cropped_input)
        Form.setTabOrder(self.image_scale_cropped_input, self.image_crop_box)
        Form.setTabOrder(self.image_crop_box, self.image_camera_no_input)
        Form.setTabOrder(self.image_camera_no_input, self.spectrum_rotation_global_input)
        Form.setTabOrder(self.spectrum_rotation_global_input, self.spectrum_rotation_spectrum_input)
        Form.setTabOrder(self.spectrum_rotation_spectrum_input, self.spectrum_start_x_input)
        Form.setTabOrder(self.spectrum_start_x_input, self.spectrum_stop_x_input)
        Form.setTabOrder(self.spectrum_stop_x_input, self.spectrum_line_input)
        Form.setTabOrder(self.spectrum_line_input, self.spectrum_lines_input)
        Form.setTabOrder(self.spectrum_lines_input, self.spectrometer_name_input)
        Form.setTabOrder(self.spectrometer_name_input, self.apply_acquisition_settings_button)
        Form.setTabOrder(self.apply_acquisition_settings_button, self.live_button)
        Form.setTabOrder(self.live_button, self.load_acquisition_settings_button)
        Form.setTabOrder(self.load_acquisition_settings_button, self.save_acquisition_settings_button)
        Form.setTabOrder(self.save_acquisition_settings_button, self.acquisition_button)
        Form.setTabOrder(self.acquisition_button, self.calibration_button)
        Form.setTabOrder(self.calibration_button, self.experiment_button)
        Form.setTabOrder(self.experiment_button, self.main_menu_tab)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "spec-tool // Open source spectral analysis"))
        self.spectrometer_name_input.setText(_translate("Form", "ELP"))
        self.load_acquisition_settings_button.setText(_translate("Form", "Load"))
        self.image_settings_label.setText(_translate("Form", "Image"))
        self.spectrum_settings_label.setText(_translate("Form", "Spectrum config"))
        self.spectrometer_name_label.setText(_translate("Form", "Spectrometer name"))
        self.detector_settings_label.setText(_translate("Form", "Detector"))
        self.save_acquisition_settings_button.setText(_translate("Form", "Save"))
        self.apply_acquisition_settings_button.setText(_translate("Form", "Apply settings"))
        self.live_button.setText(_translate("Form", "Live"))
        self.spectrum_rotation_global_input.setText(_translate("Form", "0"))
        self.spectrum_rotation_spectrum_input.setText(_translate("Form", "0"))
        self.spectrum_start_x_input.setText(_translate("Form", "750"))
        self.spectrum_stop_x_input.setText(_translate("Form", "1230"))
        self.spectrum_line_input.setText(_translate("Form", "500"))
        self.spectrum_lines_input.setText(_translate("Form", "5"))
        self.detector_width_input.setText(_translate("Form", "1280"))
        self.detector_integration_time_label.setText(_translate("Form", "Integration time (ms):"))
        self.detector_gain_label.setText(_translate("Form", "Gain (0-100):"))
        self.detector_averages_label.setText(_translate("Form", "Averages:"))
        self.detector_gain_input.setText(_translate("Form", "20"))
        self.detector_averages_input.setText(_translate("Form", "5"))
        self.detector_height_input.setText(_translate("Form", "1024"))
        self.detector_resolution_label.setText(_translate("Form", "Resolution (WxH):"))
        self.detector_integration_time_input.setText(_translate("Form", "20"))
        self.detector_resolution_x_label.setText(_translate("Form", "x"))
        self.spectrum_rotation_global_label.setText(_translate("Form", "Rotation global:"))
        self.spectrum_rotation_spectrum_label.setText(_translate("Form", "Rotation spectrum:"))
        self.spectrum_start_x_label.setText(_translate("Form", "Start (x-val):"))
        self.spectrum_stop_x_label.setText(_translate("Form", "Stop (x-val):"))
        self.spectrum_line_label.setText(_translate("Form", "Line (y-val):"))
        self.spectrum_lines_label.setText(_translate("Form", "No of lines:"))
        self.image_scale_cropped_label.setText(_translate("Form", "Scale cropped (%):"))
        self.image_crop_label.setText(_translate("Form", "Crop to spectrum:"))
        self.image_scale_overview_label.setText(_translate("Form", "Scale overview (%):"))
        self.image_camera_no_label.setText(_translate("Form", "Camera #:"))
        self.image_scale_overview_input.setText(_translate("Form", "40"))
        self.image_scale_cropped_input.setText(_translate("Form", "150"))
        self.image_camera_no_input.setText(_translate("Form", "0"))
        self.clear_experiment_button_2.setText(_translate("Form", "Clear"))
        self.export_experiment_button_2.setText(_translate("Form", "Export experiment"))
        self.experiment_menu_transmission_button_2.setText(_translate("Form", "Wavelength"))
        self.experiment_menu_emission_button_2.setText(_translate("Form", "Spectral sensitivity"))
        self.main_menu_tab.setTabText(self.main_menu_tab.indexOf(self.main_menu_calibration_tab), _translate("Form", "Page"))
        self.clear_experiment_button.setText(_translate("Form", "Clear"))
        self.export_experiment_button.setText(_translate("Form", "Export experiment"))
        self.experiment_menu_emission_button.setText(_translate("Form", "Emission"))
        self.experiment_menu_transmission_button.setText(_translate("Form", "Transmission"))
        self.experiment_no_1_label.setText(_translate("Form", "1."))
        self.experiment_no_2_label.setText(_translate("Form", "2."))
        self.experiment_no_3_label.setText(_translate("Form", "3."))
        self.acquire_dark_spectrum_button.setText(_translate("Form", "Dark spectrum"))
        self.acquire_emission_spectrum_button.setText(_translate("Form", "Emission spectrum"))
        self.acquire_reference_spectrum_button.setText(_translate("Form", "Reference spectrum"))
        self.acquire_transmission_spectrum_button.setText(_translate("Form", "Transmission spectrum"))
        self.calc_plot_3_label.setText(_translate("Form", "Transmission"))
        self.calc_plot_3_lambda_label.setText(_translate("Form", "λ (nm)"))
        self.calc_plot_3_i_label.setText(_translate("Form", "I"))
        self.save_calc_plot_1_txt_button.setText(_translate("Form", ".txt"))
        self.save_calc_plot_1_png_button.setText(_translate("Form", ".png"))
        self.save_calc_plot_3_png_button.setText(_translate("Form", ".png"))
        self.save_calc_plot_3_txt_button.setText(_translate("Form", ".txt"))
        self.save_calc_plot_2_txt_button.setText(_translate("Form", ".txt"))
        self.save_calc_plot_2_png_button.setText(_translate("Form", ".png"))
        self.calc_plot_2_combo_label.setText(_translate("Form", "Reference"))
        self.calc_plot_2_combo_i_label.setText(_translate("Form", "I"))
        self.calc_plot_1_combo_label.setText(_translate("Form", "Dark"))
        self.calc_plot_1_combo_i_label.setText(_translate("Form", "I"))
        self.calc_plot_1_combo_lambda_label.setText(_translate("Form", "λ (nm)"))
        self.calc_plot_2_combo_lambda_label.setText(_translate("Form", "λ (nm)"))
        self.calc_plot_1_i_label.setText(_translate("Form", "I"))
        self.calc_plot_1_label.setText(_translate("Form", "Dark"))
        self.calc_plot_1_lambda_label.setText(_translate("Form", "λ (nm)"))
        self.calc_plot_2_i_label.setText(_translate("Form", "I"))
        self.calc_plot_2_label.setText(_translate("Form", "Reference"))
        self.calc_plot_2_lambda_label.setText(_translate("Form", "λ (nm)"))
        self.calibration_button.setText(_translate("Form", "Calibration"))
        self.spec_streamer_label.setText(_translate("Form", "spec-streamer"))
        self.acquisition_button.setText(_translate("Form", "Acquisition"))
        self.raw_plot_i_label.setText(_translate("Form", "I"))
        self.raw_plot_label.setText(_translate("Form", "Raw spectrum"))
        self.raw_plot_lambda_label.setText(_translate("Form", "λ (nm)"))
        self.spec_streamer_v_label.setText(_translate("Form", "v1.0"))
        self.spec_tools_label.setText(_translate("Form", "by spec-tools"))
        self.experiment_button.setText(_translate("Form", "Experiment"))
        self.save_raw_plot_txt_button.setText(_translate("Form", ".txt"))
        self.save_raw_plot_png_button.setText(_translate("Form", ".png"))


from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
