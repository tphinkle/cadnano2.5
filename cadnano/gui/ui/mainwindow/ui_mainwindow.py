# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1075, 792)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setStatusTip("")
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.main_splitter = QtWidgets.QSplitter(self.centralwidget)
        self.main_splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_splitter.setFrameShadow(QtWidgets.QFrame.Plain)
        self.main_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.main_splitter.setHandleWidth(0)
        self.main_splitter.setObjectName("main_splitter")
        self.slice_graphics_view = CustomQGraphicsView(self.main_splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slice_graphics_view.sizePolicy().hasHeightForWidth())
        self.slice_graphics_view.setSizePolicy(sizePolicy)
        self.slice_graphics_view.setMinimumSize(QtCore.QSize(0, 0))
        self.slice_graphics_view.setBaseSize(QtCore.QSize(480, 0))
        self.slice_graphics_view.setMouseTracking(True)
        self.slice_graphics_view.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.slice_graphics_view.setStyleSheet("QGraphicsView { background-color: rgb(96.5%, 96.5%, 96.5%); }")
        self.slice_graphics_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.slice_graphics_view.setFrameShadow(QtWidgets.QFrame.Plain)
        self.slice_graphics_view.setLineWidth(0)
        self.slice_graphics_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.slice_graphics_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.slice_graphics_view.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.TextAntialiasing)
        self.slice_graphics_view.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.slice_graphics_view.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.slice_graphics_view.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.slice_graphics_view.setObjectName("slice_graphics_view")
        self.path_graphics_view = CustomQGraphicsView(self.main_splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_graphics_view.sizePolicy().hasHeightForWidth())
        self.path_graphics_view.setSizePolicy(sizePolicy)
        self.path_graphics_view.setMinimumSize(QtCore.QSize(0, 0))
        self.path_graphics_view.setMouseTracking(True)
        self.path_graphics_view.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.path_graphics_view.setStyleSheet("QGraphicsView { background-color: rgb(96.5%, 96.5%, 96.5%); }")
        self.path_graphics_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.path_graphics_view.setFrameShadow(QtWidgets.QFrame.Plain)
        self.path_graphics_view.setLineWidth(0)
        self.path_graphics_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.path_graphics_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.path_graphics_view.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.TextAntialiasing)
        self.path_graphics_view.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.path_graphics_view.setObjectName("path_graphics_view")
        self.outliner_property_splitter = QtWidgets.QSplitter(self.main_splitter)
        self.outliner_property_splitter.setBaseSize(QtCore.QSize(0, 0))
        self.outliner_property_splitter.setOrientation(QtCore.Qt.Vertical)
        self.outliner_property_splitter.setHandleWidth(0)
        self.outliner_property_splitter.setObjectName("outliner_property_splitter")
        self.outliner_widget = OutlinerTreeWidget(self.outliner_property_splitter)
        self.outliner_widget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.outliner_widget.setStyleSheet("OutlinerTreeWidget { background-color: rgb(96.5%, 96.5%, 96.5%); }\n"
"\n"
"")
        self.outliner_widget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.outliner_widget.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.outliner_widget.setDragEnabled(True)
        self.outliner_widget.setObjectName("outliner_widget")
        self.outliner_widget.headerItem().setText(0, "1")
        self.property_widget = PropertyEditorWidget(self.outliner_property_splitter)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.property_widget.setFont(font)
        self.property_widget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.property_widget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.property_widget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.property_widget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.property_widget.setAlternatingRowColors(True)
        self.property_widget.setUniformRowHeights(True)
        self.property_widget.setColumnCount(2)
        self.property_widget.setObjectName("property_widget")
        self.property_widget.headerItem().setText(0, "1")
        self.property_widget.headerItem().setText(1, "2")
        self.property_buttonbox = QtWidgets.QDialogButtonBox(self.outliner_property_splitter)
        self.property_buttonbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.property_buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel)
        self.property_buttonbox.setCenterButtons(True)
        self.property_buttonbox.setObjectName("property_buttonbox")
        self.gridLayout.addWidget(self.main_splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.main_toolbar = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_toolbar.sizePolicy().hasHeightForWidth())
        self.main_toolbar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_toolbar.setFont(font)
        self.main_toolbar.setIconSize(QtCore.QSize(20, 20))
        self.main_toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.main_toolbar.setObjectName("main_toolbar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.main_toolbar)
        self.selection_toolbar = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selection_toolbar.sizePolicy().hasHeightForWidth())
        self.selection_toolbar.setSizePolicy(sizePolicy)
        self.selection_toolbar.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.selection_toolbar.setFont(font)
        self.selection_toolbar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.selection_toolbar.setAutoFillBackground(False)
        self.selection_toolbar.setAllowedAreas(QtCore.Qt.LeftToolBarArea|QtCore.Qt.RightToolBarArea|QtCore.Qt.TopToolBarArea)
        self.selection_toolbar.setIconSize(QtCore.QSize(20, 20))
        self.selection_toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.selection_toolbar.setObjectName("selection_toolbar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.selection_toolbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1075, 22))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_edit = QtWidgets.QMenu(self.menubar)
        self.menu_edit.setObjectName("menu_edit")
        MainWindow.setMenuBar(self.menubar)
        self.action_new = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/filetools/new"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_new.setIcon(icon)
        self.action_new.setObjectName("action_new")
        self.action_open = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/filetools/open"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open.setIcon(icon1)
        self.action_open.setObjectName("action_open")
        self.action_close = QtWidgets.QAction(MainWindow)
        self.action_close.setObjectName("action_close")
        self.action_save = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/filetools/save"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save.setIcon(icon2)
        self.action_save.setObjectName("action_save")
        self.action_save_as = QtWidgets.QAction(MainWindow)
        self.action_save_as.setIcon(icon2)
        self.action_save_as.setObjectName("action_save_as")
        self.action_save_a_copy = QtWidgets.QAction(MainWindow)
        self.action_save_a_copy.setObjectName("action_save_a_copy")
        self.action_print = QtWidgets.QAction(MainWindow)
        self.action_print.setObjectName("action_print")
        self.action_SVG = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/filetools/svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_SVG.setIcon(icon3)
        self.action_SVG.setObjectName("action_SVG")
        self.action_X3D = QtWidgets.QAction(MainWindow)
        self.action_X3D.setObjectName("action_X3D")
        self.action_cut = QtWidgets.QAction(MainWindow)
        self.action_cut.setObjectName("action_cut")
        self.action_copy = QtWidgets.QAction(MainWindow)
        self.action_copy.setObjectName("action_copy")
        self.action_paste = QtWidgets.QAction(MainWindow)
        self.action_paste.setObjectName("action_paste")
        self.action_select_all = QtWidgets.QAction(MainWindow)
        self.action_select_all.setObjectName("action_select_all")
        self.action_new_honeycomb_part = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/parttools/new-honeycomb"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_new_honeycomb_part.setIcon(icon4)
        self.action_new_honeycomb_part.setObjectName("action_new_honeycomb_part")
        self.action_path_nick = QtWidgets.QAction(MainWindow)
        self.action_path_nick.setCheckable(True)
        self.action_path_nick.setChecked(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/pathtools/nick"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_path_nick.setIcon(icon5)
        self.action_path_nick.setObjectName("action_path_nick")
        self.action_path_select = QtWidgets.QAction(MainWindow)
        self.action_path_select.setCheckable(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/pathtools/select"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_path_select.setIcon(icon6)
        self.action_path_select.setObjectName("action_path_select")
        self.action_path_pencil = QtWidgets.QAction(MainWindow)
        self.action_path_pencil.setCheckable(True)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/pathtools/force"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_path_pencil.setIcon(icon7)
        self.action_path_pencil.setObjectName("action_path_pencil")
        self.action_path_insertion = QtWidgets.QAction(MainWindow)
        self.action_path_insertion.setCheckable(True)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/pathtools/insert"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_path_insertion.setIcon(icon8)
        self.action_path_insertion.setObjectName("action_path_insertion")
        self.action_new_square_part = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/parttools/new-square"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_new_square_part.setIcon(icon9)
        self.action_new_square_part.setObjectName("action_new_square_part")
        self.action_path_skip = QtWidgets.QAction(MainWindow)
        self.action_path_skip.setCheckable(True)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/pathtools/skip"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_path_skip.setIcon(icon10)
        self.action_path_skip.setObjectName("action_path_skip")
        self.action_path_paint = QtWidgets.QAction(MainWindow)
        self.action_path_paint.setCheckable(True)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/pathtools/paint"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_path_paint.setIcon(icon11)
        self.action_path_paint.setObjectName("action_path_paint")
        self.action_path_add_seq = QtWidgets.QAction(MainWindow)
        self.action_path_add_seq.setCheckable(True)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/pathtools/addseq"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_path_add_seq.setIcon(icon12)
        self.action_path_add_seq.setObjectName("action_path_add_seq")
        self.action_export_staples = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/filetools/export"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_export_staples.setIcon(icon13)
        self.action_export_staples.setObjectName("action_export_staples")
        self.action_preferences = QtWidgets.QAction(MainWindow)
        self.action_preferences.setObjectName("action_preferences")
        self.action_cadnano_website = QtWidgets.QAction(MainWindow)
        self.action_cadnano_website.setObjectName("action_cadnano_website")
        self.action_feedback = QtWidgets.QAction(MainWindow)
        self.action_feedback.setObjectName("action_feedback")
        self.action_filter_part = QtWidgets.QAction(MainWindow)
        self.action_filter_part.setCheckable(True)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/parttools/filter-part"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_filter_part.setIcon(icon14)
        self.action_filter_part.setObjectName("action_filter_part")
        self.action_filter_endpoint = QtWidgets.QAction(MainWindow)
        self.action_filter_endpoint.setCheckable(True)
        self.action_filter_endpoint.setChecked(True)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/parttools/filter-endpoint"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_filter_endpoint.setIcon(icon15)
        self.action_filter_endpoint.setObjectName("action_filter_endpoint")
        self.action_filter_xover = QtWidgets.QAction(MainWindow)
        self.action_filter_xover.setCheckable(True)
        self.action_filter_xover.setChecked(True)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/parttools/filter-xover"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_filter_xover.setIcon(icon16)
        self.action_filter_xover.setText("")
        self.action_filter_xover.setObjectName("action_filter_xover")
        self.action_filters_label = QtWidgets.QAction(MainWindow)
        self.action_filters_label.setEnabled(False)
        self.action_filters_label.setObjectName("action_filters_label")
        self.action_filter_strand = QtWidgets.QAction(MainWindow)
        self.action_filter_strand.setCheckable(True)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/parttools/filter-strand"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_filter_strand.setIcon(icon17)
        self.action_filter_strand.setObjectName("action_filter_strand")
        self.action_filter_handle = QtWidgets.QAction(MainWindow)
        self.action_filter_handle.setCheckable(True)
        self.action_filter_handle.setChecked(False)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/parttools/filter-handle"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_filter_handle.setIcon(icon18)
        self.action_filter_handle.setObjectName("action_filter_handle")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_path_mods = QtWidgets.QAction(MainWindow)
        self.action_path_mods.setCheckable(True)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/pathtools/mod"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_path_mods.setIcon(icon19)
        self.action_path_mods.setObjectName("action_path_mods")
        self.action_new_dnapart = QtWidgets.QAction(MainWindow)
        self.action_new_dnapart.setIcon(icon4)
        self.action_new_dnapart.setObjectName("action_new_dnapart")
        self.action_outliner = QtWidgets.QAction(MainWindow)
        self.action_outliner.setCheckable(True)
        self.action_outliner.setChecked(True)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/parttools/outliner"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_outliner.setIcon(icon20)
        self.action_outliner.setObjectName("action_outliner")
        self.action_new_part = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/parttools/new-origami"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_new_part.setIcon(icon21)
        self.action_new_part.setObjectName("action_new_part")
        self.action_new_plasmidpart = QtWidgets.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/parttools/new-dna"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_new_plasmidpart.setIcon(icon22)
        self.action_new_plasmidpart.setObjectName("action_new_plasmidpart")
        self.action_new_squarednapart = QtWidgets.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/parttools/sqpro"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_new_squarednapart.setIcon(icon23)
        self.action_new_squarednapart.setObjectName("action_new_squarednapart")
        self.action_filter_pre_axover = QtWidgets.QAction(MainWindow)
        self.action_filter_pre_axover.setCheckable(True)
        self.action_filter_pre_axover.setChecked(True)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/parttools/filter-pre-axover"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_filter_pre_axover.setIcon(icon24)
        self.action_filter_pre_axover.setObjectName("action_filter_pre_axover")
        self.action_filter_pre_pxover = QtWidgets.QAction(MainWindow)
        self.action_filter_pre_pxover.setCheckable(True)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/parttools/filter-pre-pxover"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_filter_pre_pxover.setIcon(icon25)
        self.action_filter_pre_pxover.setObjectName("action_filter_pre_pxover")
        self.action_filter_even = QtWidgets.QAction(MainWindow)
        self.action_filter_even.setCheckable(True)
        self.action_filter_even.setChecked(True)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/parttools/filter-even"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_filter_even.setIcon(icon26)
        self.action_filter_even.setObjectName("action_filter_even")
        self.action_filter_odd = QtWidgets.QAction(MainWindow)
        self.action_filter_odd.setCheckable(True)
        self.action_filter_odd.setChecked(True)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(":/parttools/filter-odd"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_filter_odd.setIcon(icon27)
        self.action_filter_odd.setObjectName("action_filter_odd")
        self.action_vhelix_create = QtWidgets.QAction(MainWindow)
        self.action_vhelix_create.setCheckable(True)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(":/slicetools/create-helix"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_vhelix_create.setIcon(icon28)
        self.action_vhelix_create.setObjectName("action_vhelix_create")
        self.action_filter_fwd = QtWidgets.QAction(MainWindow)
        self.action_filter_fwd.setCheckable(True)
        self.action_filter_fwd.setChecked(True)
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(":/parttools/filter-fwd"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_filter_fwd.setIcon(icon29)
        self.action_filter_fwd.setObjectName("action_filter_fwd")
        self.action_filter_rev = QtWidgets.QAction(MainWindow)
        self.action_filter_rev.setCheckable(True)
        self.action_filter_rev.setChecked(True)
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(":/parttools/filter-rev"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_filter_rev.setIcon(icon30)
        self.action_filter_rev.setObjectName("action_filter_rev")
        self.action_vhelix_select = QtWidgets.QAction(MainWindow)
        self.action_vhelix_select.setCheckable(True)
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap(":/slicetools/select-helix"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_vhelix_select.setIcon(icon31)
        self.action_vhelix_select.setObjectName("action_vhelix_select")
        self.action_vhelix_snap = QtWidgets.QAction(MainWindow)
        self.action_vhelix_snap.setCheckable(True)
        self.action_vhelix_snap.setChecked(True)
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap(":/slicetools/snap-helix"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_vhelix_snap.setIcon(icon32)
        self.action_vhelix_snap.setObjectName("action_vhelix_snap")
        self.action_vhelix_set_angles = QtWidgets.QAction(MainWindow)
        self.action_vhelix_set_angles.setCheckable(True)
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap(":/slicetools/select-snap-angles"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_vhelix_set_angles.setIcon(icon33)
        self.action_vhelix_set_angles.setObjectName("action_vhelix_set_angles")
        self.actionGridLines = QtWidgets.QAction(MainWindow)
        self.actionGridLines.setCheckable(True)
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap(":/slicetools/grid-lines"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGridLines.setIcon(icon34)
        self.actionGridLines.setObjectName("actionGridLines")
        self.actionGridCircles = QtWidgets.QAction(MainWindow)
        self.actionGridCircles.setCheckable(True)
        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap(":/slicetools/grid-circles"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGridCircles.setIcon(icon35)
        self.actionGridCircles.setObjectName("actionGridCircles")
        self.actionGridPoints = QtWidgets.QAction(MainWindow)
        self.actionGridPoints.setCheckable(True)
        icon36 = QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap(":/slicetools/grid-points"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGridPoints.setIcon(icon36)
        self.actionGridPoints.setObjectName("actionGridPoints")
        self.action_vhelix_move = QtWidgets.QAction(MainWindow)
        self.action_vhelix_move.setCheckable(True)
        icon37 = QtGui.QIcon()
        icon37.addPixmap(QtGui.QPixmap(":/slicetools/move"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_vhelix_move.setIcon(icon37)
        self.action_vhelix_move.setObjectName("action_vhelix_move")
        self.action_global_pencil = QtWidgets.QAction(MainWindow)
        self.action_global_pencil.setCheckable(True)
        self.action_global_pencil.setIcon(icon7)
        self.action_global_pencil.setObjectName("action_global_pencil")
        self.action_global_select = QtWidgets.QAction(MainWindow)
        self.action_global_select.setCheckable(True)
        self.action_global_select.setIcon(icon6)
        self.action_global_select.setObjectName("action_global_select")
        self.main_toolbar.addAction(self.action_new_dnapart)
        self.main_toolbar.addAction(self.action_global_select)
        self.main_toolbar.addAction(self.action_global_pencil)
        self.main_toolbar.addAction(self.action_path_nick)
        self.main_toolbar.addAction(self.action_path_paint)
        self.main_toolbar.addAction(self.action_path_insertion)
        self.main_toolbar.addAction(self.action_path_skip)
        self.main_toolbar.addAction(self.action_path_add_seq)
        self.main_toolbar.addAction(self.action_path_mods)
        self.main_toolbar.addSeparator()
        self.main_toolbar.addAction(self.action_export_staples)
        self.main_toolbar.addAction(self.action_SVG)
        self.main_toolbar.addSeparator()
        self.main_toolbar.addAction(self.action_outliner)
        self.selection_toolbar.addAction(self.action_filter_handle)
        self.selection_toolbar.addAction(self.action_filter_fwd)
        self.selection_toolbar.addAction(self.action_filter_rev)
        self.selection_toolbar.addAction(self.action_filter_endpoint)
        self.selection_toolbar.addAction(self.action_filter_xover)
        self.menu_file.addAction(self.action_about)
        self.menu_file.addAction(self.action_preferences)
        self.menu_file.addAction(self.action_new)
        self.menu_file.addAction(self.action_open)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_close)
        self.menu_file.addAction(self.action_save)
        self.menu_file.addAction(self.action_save_as)
        self.menu_edit.addAction(self.action_copy)
        self.menu_edit.addAction(self.action_paste)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())

        self.retranslateUi(MainWindow)
        self.action_close.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "cadnano"))
        self.main_toolbar.setWindowTitle(_translate("MainWindow", "Main Toolbar"))
        self.selection_toolbar.setWindowTitle(_translate("MainWindow", "Path Tools"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.menu_edit.setTitle(_translate("MainWindow", "Edit"))
        self.action_new.setText(_translate("MainWindow", "New..."))
        self.action_new.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_open.setText(_translate("MainWindow", "Open..."))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_close.setText(_translate("MainWindow", "Close"))
        self.action_close.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.action_save.setText(_translate("MainWindow", "Save"))
        self.action_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_save_as.setText(_translate("MainWindow", "Save As..."))
        self.action_save_as.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.action_save_a_copy.setText(_translate("MainWindow", "Save a Copy..."))
        self.action_print.setText(_translate("MainWindow", "Print..."))
        self.action_SVG.setText(_translate("MainWindow", "SVG"))
        self.action_X3D.setText(_translate("MainWindow", "X3D"))
        self.action_cut.setText(_translate("MainWindow", "Cut"))
        self.action_cut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.action_copy.setText(_translate("MainWindow", "Copy Part"))
        self.action_copy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.action_paste.setText(_translate("MainWindow", "Paste"))
        self.action_paste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.action_select_all.setText(_translate("MainWindow", "Select All"))
        self.action_select_all.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.action_new_honeycomb_part.setText(_translate("MainWindow", "Hc"))
        self.action_new_honeycomb_part.setToolTip(_translate("MainWindow", "Click to add new part with honeycomb lattice"))
        self.action_path_nick.setText(_translate("MainWindow", "Nick"))
        self.action_path_nick.setIconText(_translate("MainWindow", "Break"))
        self.action_path_nick.setToolTip(_translate("MainWindow", "(B)reak Tool"))
        self.action_path_nick.setShortcut(_translate("MainWindow", "B"))
        self.action_path_select.setText(_translate("MainWindow", "Select"))
        self.action_path_select.setIconText(_translate("MainWindow", "Select"))
        self.action_path_select.setToolTip(_translate("MainWindow", "Select Tool (v)"))
        self.action_path_pencil.setText(_translate("MainWindow", "Pencil"))
        self.action_path_pencil.setToolTip(_translate("MainWindow", "Pe(n)cil Tool"))
        self.action_path_insertion.setText(_translate("MainWindow", "Insert"))
        self.action_path_insertion.setToolTip(_translate("MainWindow", "(I)nsert Tool"))
        self.action_path_insertion.setShortcut(_translate("MainWindow", "I"))
        self.action_new_square_part.setText(_translate("MainWindow", "Sq"))
        self.action_new_square_part.setToolTip(_translate("MainWindow", "Click to add new part with square lattice"))
        self.action_path_skip.setText(_translate("MainWindow", "Skip"))
        self.action_path_skip.setToolTip(_translate("MainWindow", "(S)kip Tool"))
        self.action_path_skip.setShortcut(_translate("MainWindow", "S"))
        self.action_path_paint.setText(_translate("MainWindow", "Paint"))
        self.action_path_paint.setToolTip(_translate("MainWindow", "(P)aint Tool"))
        self.action_path_paint.setShortcut(_translate("MainWindow", "P"))
        self.action_path_add_seq.setText(_translate("MainWindow", "Seq"))
        self.action_path_add_seq.setToolTip(_translate("MainWindow", "(A)dd Sequence Tool"))
        self.action_path_add_seq.setShortcut(_translate("MainWindow", "A"))
        self.action_export_staples.setText(_translate("MainWindow", "Export"))
        self.action_export_staples.setToolTip(_translate("MainWindow", "export oligos as *.CSV"))
        self.action_preferences.setText(_translate("MainWindow", "Preferences"))
        self.action_preferences.setShortcut(_translate("MainWindow", "Ctrl+,"))
        self.action_cadnano_website.setText(_translate("MainWindow", "cadnano Website"))
        self.action_feedback.setText(_translate("MainWindow", "Feedback"))
        self.action_filter_part.setText(_translate("MainWindow", "Parts"))
        self.action_filter_part.setToolTip(_translate("MainWindow", "Part-selection mode"))
        self.action_filter_endpoint.setToolTip(_translate("MainWindow", "(E)ndpoints"))
        self.action_filter_endpoint.setShortcut(_translate("MainWindow", "E"))
        self.action_filter_xover.setToolTip(_translate("MainWindow", "(X)overs"))
        self.action_filter_xover.setShortcut(_translate("MainWindow", "X"))
        self.action_filters_label.setText(_translate("MainWindow", "Selectable:"))
        self.action_filters_label.setToolTip(_translate("MainWindow", "Selection Filters"))
        self.action_filter_strand.setToolTip(_translate("MainWindow", "stran(D)s"))
        self.action_filter_strand.setShortcut(_translate("MainWindow", "D"))
        self.action_filter_handle.setToolTip(_translate("MainWindow", "(H)andles"))
        self.action_filter_handle.setShortcut(_translate("MainWindow", "H"))
        self.action_about.setText(_translate("MainWindow", "About cadnano"))
        self.action_path_mods.setText(_translate("MainWindow", "Mod"))
        self.action_path_mods.setToolTip(_translate("MainWindow", "(M)odifer Tool"))
        self.action_path_mods.setShortcut(_translate("MainWindow", "M"))
        self.action_new_dnapart.setText(_translate("MainWindow", "New"))
        self.action_new_dnapart.setIconText(_translate("MainWindow", "New"))
        self.action_new_dnapart.setToolTip(_translate("MainWindow", "Add DNAPart "))
        self.action_new_dnapart.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.action_outliner.setText(_translate("MainWindow", "inspector"))
        self.action_outliner.setToolTip(_translate("MainWindow", "Toggle Outliner"))
        self.action_new_part.setText(_translate("MainWindow", "New"))
        self.action_new_part.setToolTip(_translate("MainWindow", "Add new part"))
        self.action_new_plasmidpart.setText(_translate("MainWindow", "Plasmid"))
        self.action_new_plasmidpart.setToolTip(_translate("MainWindow", "Plasmid"))
        self.action_new_squarednapart.setText(_translate("MainWindow", "Sq"))
        self.action_new_squarednapart.setIconText(_translate("MainWindow", "Sq"))
        self.action_new_squarednapart.setToolTip(_translate("MainWindow", "Add SquareDNAPart "))
        self.action_filter_pre_axover.setText(_translate("MainWindow", "filter_pre_axover"))
        self.action_filter_pre_axover.setToolTip(_translate("MainWindow", "Antiparallel Xovers ([)"))
        self.action_filter_pre_axover.setShortcut(_translate("MainWindow", "]"))
        self.action_filter_pre_pxover.setText(_translate("MainWindow", "filter-pre-pxover"))
        self.action_filter_pre_pxover.setToolTip(_translate("MainWindow", "Parallel Xovers (\\)"))
        self.action_filter_pre_pxover.setShortcut(_translate("MainWindow", "\\"))
        self.action_filter_even.setText(_translate("MainWindow", "filter-even"))
        self.action_filter_even.setToolTip(_translate("MainWindow", "filter-even"))
        self.action_filter_even.setShortcut(_translate("MainWindow", "0"))
        self.action_filter_odd.setText(_translate("MainWindow", "filter-odd1"))
        self.action_filter_odd.setToolTip(_translate("MainWindow", "filter-odd"))
        self.action_filter_odd.setShortcut(_translate("MainWindow", "1"))
        self.action_vhelix_create.setText(_translate("MainWindow", "create"))
        self.action_vhelix_create.setToolTip(_translate("MainWindow", "Create Helix"))
        self.action_filter_fwd.setText(_translate("MainWindow", "filter-fwd"))
        self.action_filter_fwd.setToolTip(_translate("MainWindow", "(F)wd"))
        self.action_filter_fwd.setShortcut(_translate("MainWindow", "F"))
        self.action_filter_rev.setText(_translate("MainWindow", "filter-rev"))
        self.action_filter_rev.setToolTip(_translate("MainWindow", "(R)ev"))
        self.action_filter_rev.setShortcut(_translate("MainWindow", "R"))
        self.action_vhelix_select.setText(_translate("MainWindow", "select"))
        self.action_vhelix_select.setToolTip(_translate("MainWindow", "Select Helix"))
        self.action_vhelix_snap.setText(_translate("MainWindow", "Snap"))
        self.action_vhelix_snap.setToolTip(_translate("MainWindow", "Snap Helix"))
        self.action_vhelix_set_angles.setText(_translate("MainWindow", "angles"))
        self.action_vhelix_set_angles.setToolTip(_translate("MainWindow", "Helix angle"))
        self.actionGridLines.setText(_translate("MainWindow", "gridLines"))
        self.actionGridCircles.setText(_translate("MainWindow", "gridCircles"))
        self.actionGridPoints.setText(_translate("MainWindow", "gridPoints"))
        self.action_vhelix_move.setText(_translate("MainWindow", "move"))
        self.action_vhelix_move.setShortcut(_translate("MainWindow", "W"))
        self.action_global_pencil.setText(_translate("MainWindow", "Pencil"))
        self.action_global_pencil.setToolTip(_translate("MainWindow", "Pe(n)cil Tool"))
        self.action_global_pencil.setShortcut(_translate("MainWindow", "N"))
        self.action_global_select.setText(_translate("MainWindow", "Select"))
        self.action_global_select.setIconText(_translate("MainWindow", "Select"))
        self.action_global_select.setToolTip(_translate("MainWindow", "Select Tool (v)"))
        self.action_global_select.setShortcut(_translate("MainWindow", "V"))

from cadnano.gui.views.customqgraphicsview import CustomQGraphicsView
from cadnano.gui.views.outlinerview.outlinertreewidget import OutlinerTreeWidget
from cadnano.gui.views.propertyview.propertyeditorwidget import PropertyEditorWidget
import cadnano.gui.ui.mainwindow.icons_rc
