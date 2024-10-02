from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QSizePolicy

from videotrans.component.controlobj import TextGetdir
from videotrans.configure import config
from videotrans.recognition import RECOGN_NAME_LIST
from videotrans.tts import TTS_NAME_LIST

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)


        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.splitter.setLineWidth(1)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.splitter.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.splitter.setMaximumWidth(700)
        self.splitter.setMinimumWidth(380)

        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 3, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.btn_get_video = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_get_video.setMinimumSize(QtCore.QSize(120, 30))
        self.btn_get_video.setObjectName("btn_get_video")

        self.source_mp4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.source_mp4.setMinimumSize(QtCore.QSize(0, 30))
        self.source_mp4.setText("Select the video to be processed" if config.defaulelang != 'zh' else '选择要处理的视频')
        self.source_mp4.setReadOnly(False)
        self.source_mp4.setDisabled(True)
        self.source_mp4.setObjectName("source_mp4")

        self.select_file_type = QtWidgets.QCheckBox()
        self.select_file_type.setText('文件夹' if config.defaulelang == 'zh' else 'Folder')
        self.select_file_type.setToolTip('默认可选择多个文件，选中该框则可选择文件夹' if config.defaulelang == 'zh' else 'Multiple files can be selected by default, check the box to select folders')

        self.horizontalLayout_6.addWidget(self.btn_get_video)
        self.horizontalLayout_6.addWidget(self.select_file_type)
        self.horizontalLayout_6.addWidget(self.source_mp4)
        self.horizontalLayout_6.addStretch()

        self.btn_save_dir = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_save_dir.setMinimumSize(QtCore.QSize(120, 30))
        self.btn_save_dir.setObjectName("btn_save_dir")
        self.horizontalLayout_6.addWidget(self.btn_save_dir)

        self.only_video = QtWidgets.QCheckBox(self.layoutWidget)
        self.only_video.setMinimumSize(QtCore.QSize(0, 30))
        self.only_video.setObjectName("only_video")
        self.only_video.setText(config.uilanglist['onlyvideo'])
        self.only_video.setToolTip(config.uilanglist['onlyvideo_tips'])

        self.horizontalLayout_6.addWidget(self.only_video)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        
        
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.layout_translate_type = QtWidgets.QFormLayout()
        self.layout_translate_type.setObjectName("layoutconfig.uilanglist.get_type")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)

        self.label_9.setMinimumSize(QtCore.QSize(0, 30))
        self.label_9.setObjectName("label_9")
        
        self.translate_type = QtWidgets.QComboBox(self.layoutWidget)
        self.translate_type.setMinimumSize(QtCore.QSize(160, 30))
        self.translate_type.setObjectName("translate_type")

        self.horizontalLayout_5.addWidget(self.label_9)
        self.horizontalLayout_5.addWidget(self.translate_type)

        # 原始语言 目标语言 start       
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setObjectName("label_2")
        
        self.source_language = QtWidgets.QComboBox(self.layoutWidget)

        self.source_language.setMinimumSize(QtCore.QSize(145, 30))
        self.source_language.setObjectName("source_language")

        self.label_3 = QtWidgets.QLabel(self.layoutWidget)

        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.label_3.setObjectName("label_3")
        self.target_language = QtWidgets.QComboBox(self.layoutWidget)

        self.target_language.setMinimumSize(QtCore.QSize(145, 30))
        self.target_language.setObjectName("target_language")

        self.horizontalLayout_5.addWidget(self.label_2)
        self.horizontalLayout_5.addWidget(self.source_language)
        self.horizontalLayout_5.addWidget(self.label_3)
        self.horizontalLayout_5.addWidget(self.target_language)

        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setObjectName("label")

        self.proxy = QtWidgets.QLineEdit(self.layoutWidget)

        self.proxy.setMinimumSize(QtCore.QSize(120, 30))
        self.proxy.setObjectName("proxy")

        self.horizontalLayout_5.addWidget(self.label)
        self.horizontalLayout_5.addWidget(self.proxy)

        self.listen_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.listen_btn.setEnabled(False)
        self.listen_btn.setFixedWidth(80)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        # 配音渠道行
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tts_text = QtWidgets.QLabel(self.layoutWidget)
        self.tts_text.setObjectName("tts_text")
        self.tts_type = QtWidgets.QComboBox(self.layoutWidget)
        self.tts_type.setMinimumSize(QtCore.QSize(160, 30))
        self.tts_type.setObjectName("tts_type")
        self.tts_type.addItems(TTS_NAME_LIST)
        self.horizontalLayout.addWidget(self.tts_text)
        self.horizontalLayout.addWidget(self.tts_type)

        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 30))
        self.label_4.setObjectName("label_4")
        self.voice_role = QtWidgets.QComboBox(self.layoutWidget)
        self.voice_role.setMinimumSize(QtCore.QSize(160, 30))
        self.voice_role.setObjectName("voice_role")

        self.horizontalLayout.addWidget(self.label_4)
        self.horizontalLayout.addWidget(self.voice_role)
        self.horizontalLayout.addWidget(self.listen_btn)
        self.horizontalLayout.addStretch()

        self.volume_label = QtWidgets.QLabel(self.layoutWidget)
        self.volume_label.setText("音量+" if config.defaulelang == 'zh' else "Volume+")
        self.volume_rate = QtWidgets.QSpinBox(self.layoutWidget)
        self.volume_rate.setMinimum(-95)
        self.volume_rate.setMaximum(100)
        self.volume_rate.setObjectName("volume_rate")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volume_rate.sizePolicy().hasHeightForWidth())
        self.volume_rate.setSizePolicy(sizePolicy)

        self.pitch_label = QtWidgets.QLabel(self.layoutWidget)
        self.pitch_label.setText("音调+" if config.defaulelang == 'zh' else "Pitch+")
        self.pitch_rate = QtWidgets.QSpinBox(self.layoutWidget)
        self.pitch_rate.setMinimum(-100)
        self.pitch_rate.setMaximum(100)
        self.pitch_rate.setObjectName("pitch_rate")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pitch_rate.sizePolicy().hasHeightForWidth())
        self.pitch_rate.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.volume_label)
        self.horizontalLayout.addWidget(self.volume_rate)
        self.horizontalLayout.addWidget(self.pitch_label)
        self.horizontalLayout.addWidget(self.pitch_rate)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        # 语音识别
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.reglabel=QtWidgets.QLabel(self.layoutWidget)
        self.reglabel.setText('语音识别' if config.defaulelang=='zh' else 'Speech Recognition')
        self.recogn_type = QtWidgets.QComboBox(self.layoutWidget)
        self.recogn_type.setMinimumSize(QtCore.QSize(160, 30))
        self.recogn_type.setObjectName("label_5")
        self.recogn_type.addItems(RECOGN_NAME_LIST)
        self.recogn_type.setToolTip(config.uilanglist['model_type_tips'])
        
        self.model_name_help=QtWidgets.QPushButton(self.layoutWidget)
        self.model_name_help.setStyleSheet("""background-color:transparent""")
        self.model_name_help.setText('!选择模型' if config.defaulelang=='zh' else '!Model')
        self.model_name_help.setToolTip('点击查看模型选择说明' if config.defaulelang=='zh' else 'Click for model description')
        self.model_name_help.setMaximumSize(QtCore.QSize(60, 20))

        self.model_name = QtWidgets.QComboBox(self.layoutWidget)
        self.model_name.setMinimumSize(QtCore.QSize(160, 30))
        self.model_name.setObjectName("model_name")

        
        self.split_type = QtWidgets.QComboBox(self.layoutWidget)
        self.split_type.setMinimumSize(QtCore.QSize(80, 30))
        self.split_type.setObjectName("split_type")


        self.horizontalLayout_4.addWidget(self.reglabel)
        self.horizontalLayout_4.addWidget(self.recogn_type)
        self.horizontalLayout_4.addWidget(self.model_name_help)
        self.horizontalLayout_4.addWidget(self.model_name)
        self.horizontalLayout_4.addWidget(self.split_type)

        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.subtitle_type = QtWidgets.QComboBox(self.layoutWidget)
        self.subtitle_type.setMinimumSize(QtCore.QSize(0, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subtitle_type.sizePolicy().hasHeightForWidth())
        self.subtitle_type.setSizePolicy(sizePolicy)
        self.subtitle_type.setObjectName("subtitle_type")
        self.horizontalLayout_4.addWidget(self.subtitle_type)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.gaoji_layout_inner2 = QtWidgets.QHBoxLayout()
        self.gaoji_layout_inner2.setObjectName("gaoji_layout_inner2")
        self.addbackbtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addbackbtn.sizePolicy().hasHeightForWidth())
        self.addbackbtn.setSizePolicy(sizePolicy)
        self.addbackbtn.setMinimumSize(QtCore.QSize(100, 30))
        self.addbackbtn.setObjectName("addbackbtn")
        self.gaoji_layout_inner2.addWidget(self.addbackbtn)

        self.back_audio = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_audio.sizePolicy().hasHeightForWidth())
        self.back_audio.setSizePolicy(sizePolicy)
        self.back_audio.setMinimumSize(QtCore.QSize(0, 30))
        self.back_audio.setObjectName("back_audio")
        self.gaoji_layout_inner2.addWidget(self.back_audio)

        self.gaoji_layout_inner = QtWidgets.QHBoxLayout()
        self.gaoji_layout_inner.setObjectName("gaoji_layout_inner")
        self.layout_voice_rate = QtWidgets.QFormLayout()
        self.layout_voice_rate.setFormAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.layout_voice_rate.setObjectName("layout_voice_rate")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(0, 30))
        self.label_6.setObjectName("label_6")

        self.layout_voice_rate.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)

        self.voice_rate = QtWidgets.QSpinBox(self.layoutWidget)
        self.voice_rate.setMinimum(-50)
        self.voice_rate.setMaximum(50)
        self.voice_rate.setObjectName("voice_rate")

        self.layout_voice_rate.setAlignment(Qt.AlignVCenter)
        self.layout_voice_rate.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.voice_rate)
        self.gaoji_layout_inner.addLayout(self.layout_voice_rate)

        self.append_video = QtWidgets.QCheckBox(self.layoutWidget)
        self.append_video.setObjectName("append_video")

        self.voice_autorate = QtWidgets.QCheckBox(self.layoutWidget)
        self.voice_autorate.setObjectName("voice_autorate")

        self.video_autorate = QtWidgets.QCheckBox(self.layoutWidget)
        self.video_autorate.setObjectName("videoe_autorate")

        self.gaoji_layout_inner.addWidget(self.append_video)
        self.gaoji_layout_inner.addWidget(self.voice_autorate)
        self.gaoji_layout_inner.addWidget(self.video_autorate)

        self.is_separate = QtWidgets.QCheckBox(self.layoutWidget)
        self.is_separate.setMinimumSize(QtCore.QSize(0, 30))
        self.is_separate.setObjectName("is_separate")
        self.gaoji_layout_inner.addWidget(self.is_separate)

        self.enable_cuda = QtWidgets.QCheckBox(self.layoutWidget)
        self.enable_cuda.setMinimumSize(QtCore.QSize(0, 30))
        self.enable_cuda.setObjectName("enable_cuda")
        self.enable_cuda.setToolTip(config.transobj['cudatips'])
        self.gaoji_layout_inner.addWidget(self.enable_cuda)

        self.gaoji_layout_inner.setAlignment(Qt.AlignVCenter)
        self.verticalLayout_2.addLayout(self.gaoji_layout_inner)
        self.verticalLayout_2.addLayout(self.gaoji_layout_inner2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.show_tips = QtWidgets.QPushButton(self.layoutWidget)
        self.show_tips.setStyleSheet("""background-color:transparent;border-color:transparent;color:#aaaaaa""")
        self.show_tips.setObjectName("show_tips")
        self.verticalLayout_3.addWidget(self.show_tips)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.addStretch(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.clear_cache = QtWidgets.QCheckBox(self.layoutWidget)
        self.clear_cache.setMinimumSize(QtCore.QSize(50, 20))
        self.clear_cache.setObjectName("clear_cache")
        self.clear_cache.setToolTip(
            '清理上次执行时已处理好的文件，比如已识别或翻译的字幕文件' if config.defaulelang == 'zh' else 'Cleaning up files that have been processed in previous executions, such as recognized or translated subtitle files')
        self.clear_cache.setText('清理已生成' if config.defaulelang == 'zh' else 'Del Generated')
        self.clear_cache.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.shutdown = QtWidgets.QCheckBox(self.layoutWidget)
        self.shutdown.setMinimumSize(QtCore.QSize(50, 20))
        self.shutdown.setObjectName("shutdown")
        self.shutdown.setToolTip(
            '完成全部任务后自动关机' if config.defaulelang == 'zh' else 'Automatic shutdown after completing all tasks')
        self.shutdown.setText('完成后关机' if config.defaulelang == 'zh' else 'Automatic shutdown')
        self.shutdown.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.startbtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startbtn.sizePolicy().hasHeightForWidth())
        self.startbtn.setSizePolicy(sizePolicy)
        self.startbtn.setMinimumSize(QtCore.QSize(160, 40))
        self.startbtn.setObjectName("startbtn")

        vhlayout = QtWidgets.QVBoxLayout()
        vhlayout.setAlignment(Qt.AlignVCenter)
        vhlayout.addWidget(self.clear_cache)
        vhlayout.addWidget(self.shutdown)

        self.horizontalLayout_3.addLayout(vhlayout)
        self.horizontalLayout_3.addWidget(self.startbtn)

        self.continue_compos = QtWidgets.QPushButton(self.layoutWidget)
        self.continue_compos.setEnabled(True)
        self.continue_compos.setMinimumSize(QtCore.QSize(240, 40))

        self.continue_compos.setObjectName("continue_compos")
        self.continue_compos.setVisible(False)
        self.horizontalLayout_3.addWidget(self.continue_compos)
        self.stop_djs = QtWidgets.QPushButton(self.layoutWidget)
        self.stop_djs.setEnabled(True)
        self.stop_djs.setVisible(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_djs.sizePolicy().hasHeightForWidth())
        self.stop_djs.setSizePolicy(sizePolicy)
        self.stop_djs.setMinimumSize(QtCore.QSize(130, 30))
        self.stop_djs.setObjectName("stop_djs")
        self.horizontalLayout_3.addWidget(self.stop_djs)
        self.horizontalLayout_3.addStretch(1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.timeout_tips = QtWidgets.QLabel()
        self.timeout_tips.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # 设置 QLabel 水平拉伸（扩展）
        self.timeout_tips.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.verticalLayout_3.addWidget(self.timeout_tips)

        self.scroll_area = QtWidgets.QScrollArea(self.layoutWidget)
        self.scroll_area.setStyleSheet("border-color:#32414B")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()

        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.scroll_area.setWidgetResizable(True)
        viewport = QtWidgets.QWidget(self.scroll_area)
        self.scroll_area.setWidget(viewport)
        self.processlayout = QtWidgets.QVBoxLayout(viewport)
        self.processlayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.scroll_area)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")


        self.subtitle_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.subtitle_layout.setContentsMargins(3, 0, 0, 0)
        self.subtitle_layout.setObjectName("subtitle_layout")

        self.subtitle_area = TextGetdir(self)
        self.subtitle_area.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.subtitle_area.setPlaceholderText(
            f"{config.transobj['zimubianjitishi']}\n\n{config.transobj['subtitle_tips']}\n\n{config.transobj['meitiaozimugeshi']}")
        self.subtitle_layout.addWidget(self.subtitle_area)

        self.layout_sub_bottom = QtWidgets.QHBoxLayout()
        self.layout_sub_bottom.setObjectName("layout_sub_bottom")

        #
        self.import_sub = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.import_sub.setObjectName("import_sub")
        self.layout_sub_bottom.addWidget(self.import_sub)
        #
        self.export_sub = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.export_sub.setObjectName("export_sub")
        #
        self.layout_sub_bottom.addWidget(self.export_sub)
        #
        self.set_line_role = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.set_line_role.setObjectName("set_line_role")
        #
        self.layout_sub_bottom.addWidget(self.set_line_role)
        self.subtitle_layout.addLayout(self.layout_sub_bottom)


        self.horizontalLayout_7.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)

        self.menuBar.setObjectName("menuBar")
        self.menu_Key = QtWidgets.QMenu(self.menuBar)
        self.menu_Key.setObjectName("menu_Key")

        self.menu_TTS = QtWidgets.QMenu(self.menuBar)
        self.menu_TTS.setObjectName("menu_TTS")

        self.menu_RECOGN = QtWidgets.QMenu(self.menuBar)
        self.menu_RECOGN.setObjectName("menu_RECOGN")

        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_H = QtWidgets.QMenu(self.menuBar)
        self.menu_H.setObjectName("menu_H")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.toolBar.setMovable(True)
        self.toolBar.setIconSize(QtCore.QSize(100, 40))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionbaidu_key = QtGui.QAction(MainWindow)
        self.actionbaidu_key.setObjectName("actionbaidu_key")
        self.actionchatgpt_key = QtGui.QAction(MainWindow)
        self.actionchatgpt_key.setObjectName("actionchatgpt_key")
        self.actionopenaitts_key = QtGui.QAction(MainWindow)
        self.actionopenaitts_key.setObjectName("actionopenaitts_key")
        self.actionopenairecognapi_key = QtGui.QAction(MainWindow)
        self.actionopenairecognapi_key.setObjectName("actionopenairecognapi_key")
        self.actionai302_key = QtGui.QAction(MainWindow)
        self.actionai302_key.setObjectName("actionai302_key")
        self.actionlocalllm_key = QtGui.QAction(MainWindow)
        self.actionlocalllm_key.setObjectName("actionlocalllm_key")
        self.actionzijiehuoshan_key = QtGui.QAction(MainWindow)
        self.actionzijiehuoshan_key.setObjectName("actionzijiehuoshan_key")
        self.actiondeepL_key = QtGui.QAction(MainWindow)
        self.actiondeepL_key.setObjectName("actiondeepL_key")

        self.actionazure_tts = QtGui.QAction(MainWindow)
        self.actionazure_tts.setObjectName("actionazure_tts")

        self.action_ffmpeg = QtGui.QAction(MainWindow)
        self.action_ffmpeg.setObjectName("action_ffmpeg")
        self.action_git = QtGui.QAction(MainWindow)
        self.action_git.setObjectName("action_git")
        self.action_issue = QtGui.QAction(MainWindow)
        self.action_issue.setObjectName("action_issue")
        self.actiondeepLX_address = QtGui.QAction(MainWindow)
        self.actiondeepLX_address.setObjectName("actiondeepLX_address")
        self.actionott_address = QtGui.QAction(MainWindow)
        self.actionott_address.setObjectName("actionott_address")

        self.actionclone_address = QtGui.QAction(MainWindow)
        self.actionclone_address.setObjectName("actionclone_address")
        self.actionchattts_address = QtGui.QAction(MainWindow)
        self.actionchattts_address.setObjectName("actionchattts_address")
        self.actionai302tts_address = QtGui.QAction(MainWindow)
        self.actionai302tts_address.setObjectName("actionai302tts_address")

        self.actiontts_api = QtGui.QAction(MainWindow)
        self.actiontts_api.setObjectName("actiontts_api")

        self.actiontrans_api = QtGui.QAction(MainWindow)
        self.actiontrans_api.setObjectName("actiontrans_api")
        self.actionzhrecogn_api = QtGui.QAction(MainWindow)
        self.actionzhrecogn_api.setObjectName("actionzhrecogn_api")
        self.actionrecognapi = QtGui.QAction(MainWindow)
        self.actionrecognapi.setObjectName("actionrecognapi")
        self.actionsttapi = QtGui.QAction(MainWindow)
        self.actionsttapi.setObjectName("actionsttapi")

        self.actiondoubao_api = QtGui.QAction(MainWindow)
        self.actiondoubao_api.setObjectName("actiondoubao_api")

        self.actiontts_gptsovits = QtGui.QAction(MainWindow)
        self.actiontts_gptsovits.setObjectName("actiontts_gptsovits")
        self.actiontts_cosyvoice = QtGui.QAction(MainWindow)
        self.actiontts_cosyvoice.setObjectName("actiontts_cosyvoice")
        self.actiontts_fishtts = QtGui.QAction(MainWindow)
        self.actiontts_fishtts.setObjectName("actiontts_fishtts")

        self.action_website = QtGui.QAction(MainWindow)
        self.action_website.setObjectName("action_website")
        self.action_blog = QtGui.QAction(MainWindow)
        self.action_blog.setObjectName("action_blog")
        self.action_discord = QtGui.QAction(MainWindow)
        self.action_discord.setObjectName("action_discord")
        self.action_models = QtGui.QAction(MainWindow)
        self.action_models.setObjectName("action_models")
        self.action_dll = QtGui.QAction(MainWindow)
        self.action_dll.setObjectName("action_dll")
        self.action_gtrans = QtGui.QAction(MainWindow)
        self.action_gtrans.setObjectName("action_gtrans")
        self.action_cuda = QtGui.QAction(MainWindow)
        self.action_cuda.setObjectName("action_cuda")

        self.action_online = QtGui.QAction(MainWindow)
        self.action_online.setObjectName("action_online")

        self.actiontencent_key = QtGui.QAction(MainWindow)
        self.actiontencent_key.setObjectName("actiontencent_key")
        self.action_about = QtGui.QAction(MainWindow)
        self.action_about.setObjectName("action_about")

        self.action_biaozhun = QtGui.QAction(MainWindow)
        self.action_biaozhun.setCheckable(True)
        self.action_biaozhun.setChecked(True)
        self.action_biaozhun.setObjectName("action_biaozhun")

        self.action_xinshoujandan = QtGui.QAction(MainWindow)
        self.action_xinshoujandan.setCheckable(True)
        self.action_xinshoujandan.setChecked(False)
        self.action_xinshoujandan.setObjectName("action_xinshoujandan")

        self.action_yuyinshibie = QtGui.QAction(MainWindow)

        self.action_yuyinshibie.setObjectName("action_yuyinshibie")
        self.action_yuyinhecheng = QtGui.QAction(MainWindow)

        self.action_yuyinhecheng.setObjectName("action_yuyinhecheng")
        self.action_tiquzimu = QtGui.QAction(MainWindow)
        self.action_tiquzimu.setCheckable(True)


        self.action_tiquzimu.setObjectName("action_tiquzimu")

        self.action_yingyinhebing = QtGui.QAction(MainWindow)
        self.action_yingyinhebing.setObjectName("action_yingyinhebing")

        self.action_subtitleediter = QtGui.QAction(MainWindow)
        self.action_subtitleediter.setObjectName("action_subtitleediter")

        self.action_hun = QtGui.QAction(MainWindow)
        self.action_hun.setObjectName("action_hun")

        self.action_fanyi = QtGui.QAction(MainWindow)
        self.action_fanyi.setObjectName("action_fanyi")
        self.action_hebingsrt = QtGui.QAction(MainWindow)
        self.action_hebingsrt.setObjectName("action_hebingsrt")

        self.action_clearcache = QtGui.QAction(MainWindow)
        self.action_clearcache.setObjectName("action_clearcache")

        self.actionazure_key = QtGui.QAction(MainWindow)
        self.actionazure_key.setObjectName("actionazure_key")
        self.actiongemini_key = QtGui.QAction(MainWindow)
        self.actiongemini_key.setObjectName("actiongemini_key")
        self.actionElevenlabs_key = QtGui.QAction(MainWindow)
        self.actionElevenlabs_key.setObjectName("actionElevenlabs_key")
        self.actionyoutube = QtGui.QAction(MainWindow)
        self.actionyoutube.setObjectName("actionyoutube")
        self.actionwatermark = QtGui.QAction(MainWindow)
        self.actionwatermark.setObjectName("actionwatermark")
        self.actionsepar = QtGui.QAction(MainWindow)
        self.actionsepar.setObjectName("actionsepar")
        self.actionsetini = QtGui.QAction(MainWindow)
        self.actionsetini.setObjectName("setini")
        self.actionvideoandaudio = QtGui.QAction(MainWindow)
        self.actionvideoandaudio.setObjectName("videoandaudio")
        self.actionvideoandaudio = QtGui.QAction(MainWindow)
        self.actionvideoandaudio.setObjectName("videoandaudio")
        self.actionvideoandsrt = QtGui.QAction(MainWindow)
        self.actionvideoandsrt.setObjectName("videoandsrt")
        self.actionformatcover = QtGui.QAction(MainWindow)
        self.actionformatcover.setObjectName("formatcover")
        self.actionsubtitlescover = QtGui.QAction(MainWindow)
        self.actionsubtitlescover.setObjectName("subtitlescover")

        self.action_yinshipinfenli = QtGui.QAction(MainWindow)
        self.action_yinshipinfenli.setObjectName("action_yinshipinfenli")

        self.menu_Key.addAction(self.actionbaidu_key)
        self.menu_Key.addSeparator()
        self.menu_Key.addAction(self.actiontencent_key)
        self.menu_Key.addSeparator()
        self.menu_Key.addAction(self.actionai302_key)
        self.menu_Key.addSeparator()
        self.menu_Key.addAction(self.actionchatgpt_key)
        self.menu_Key.addSeparator()
        self.menu_Key.addAction(self.actionlocalllm_key)
        self.menu_Key.addSeparator()
        self.menu_Key.addAction(self.actionzijiehuoshan_key)
        self.menu_Key.addSeparator()
        self.menu_Key.addAction(self.actionazure_key)
        self.menu_Key.addSeparator()
        self.menu_Key.addAction(self.actiongemini_key)
        self.menu_Key.addSeparator()
        self.menu_Key.addAction(self.actiondeepL_key)
        self.menu_Key.addSeparator()
        self.menu_Key.addAction(self.actiondeepLX_address)
        self.menu_Key.addSeparator()
        self.menu_Key.addAction(self.actionott_address)
        self.menu_Key.addSeparator()
        self.menu_Key.addAction(self.actiontrans_api)

        self.menu_Key.addSeparator()

        self.menu_TTS.addAction(self.actionclone_address)
        self.menu_TTS.addSeparator()
        self.menu_TTS.addAction(self.actionchattts_address)
        self.menu_TTS.addSeparator()
        self.menu_TTS.addAction(self.actionai302tts_address)
        self.menu_TTS.addSeparator()
        self.menu_TTS.addAction(self.actiontts_gptsovits)
        self.menu_TTS.addSeparator()
        self.menu_TTS.addAction(self.actiontts_cosyvoice)
        self.menu_TTS.addSeparator()
        self.menu_TTS.addAction(self.actiontts_fishtts)
        self.menu_TTS.addSeparator()
        self.menu_TTS.addAction(self.actionElevenlabs_key)
        self.menu_TTS.addSeparator()
        self.menu_TTS.addAction(self.actionazure_tts)
        self.menu_TTS.addSeparator()
        self.menu_TTS.addAction(self.actionopenaitts_key)
        self.menu_TTS.addSeparator()
        self.menu_TTS.addAction(self.actiontts_api)
        self.menu_TTS.addSeparator()

        self.menu_RECOGN.addAction(self.actiondoubao_api)
        self.menu_RECOGN.addSeparator()
        self.menu_RECOGN.addAction(self.actionzhrecogn_api)
        self.menu_RECOGN.addSeparator()
        self.menu_RECOGN.addAction(self.actionopenairecognapi_key)
        self.menu_RECOGN.addSeparator()
        self.menu_RECOGN.addAction(self.actionrecognapi)
        self.menu_RECOGN.addSeparator()
        self.menu_RECOGN.addAction(self.actionsttapi)

        self.menu.addAction(self.actionsetini)
        self.menu.addSeparator()
        self.menu.addAction(self.actionwatermark)
        self.menu.addSeparator()
        self.menu.addAction(self.actionvideoandaudio)
        self.menu.addSeparator()
        self.menu.addAction(self.actionvideoandsrt)
        self.menu.addSeparator()
        self.menu.addAction(self.actionformatcover)
        self.menu.addSeparator()
        self.menu.addAction(self.actionsubtitlescover)
        self.menu.addSeparator()
        self.menu.addAction(self.action_yinshipinfenli)
        self.menu.addSeparator()
        self.menu.addAction(self.action_hun)
        self.menu.addSeparator()
        self.menu.addAction(self.action_hebingsrt)
        self.menu.addSeparator()
        self.menu.addAction(self.actionyoutube)
        self.menu.addSeparator()
        self.menu.addAction(self.actionsepar)
        self.menu.addSeparator()
        self.menu.addAction(self.action_clearcache)
        self.menu.addSeparator()

        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_website)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_blog)
        self.menu_H.addSeparator()

        self.menu_H.addAction(self.action_models)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_gtrans)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_dll)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_cuda)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_discord)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_git)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_issue)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_ffmpeg)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_about)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_online)
        self.menu_H.addSeparator()

        self.menuBar.addAction(self.menu_Key.menuAction())
        self.menuBar.addAction(self.menu_TTS.menuAction())
        self.menuBar.addAction(self.menu_RECOGN.menuAction())
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_H.menuAction())

        self.toolBar.addAction(self.action_xinshoujandan)
        self.toolBar.addAction(self.action_biaozhun)
        self.toolBar.addAction(self.action_tiquzimu)

        self.toolBar.addAction(self.action_yuyinshibie)
        self.toolBar.addAction(self.action_fanyi)
        self.toolBar.addAction(self.action_yuyinhecheng)
        self.toolBar.addAction(self.actionvideoandaudio)
        self.toolBar.addAction(self.actionvideoandsrt)
        self.toolBar.addAction(self.actionsubtitlescover)
        self.toolBar.addAction(self.actionformatcover)
        self.toolBar.addAction(self.action_yingyinhebing)
        self.toolBar.addAction(self.action_subtitleediter)
        # 200ms后渲染文字
        QTimer.singleShot(50, self.retranslateUi)

    def retranslateUi(self):
        self.btn_get_video.setToolTip(
            config.uilanglist.get("Multiple MP4 videos can be selected and automatically queued for processing"))
        self.btn_get_video.setText('选择要处理的视频' if config.defaulelang=='zh' else 'Select the video')
        self.btn_save_dir.setToolTip( config.uilanglist.get("Select where to save the processed output resources"))
        self.btn_save_dir.setText(config.uilanglist.get("Save to.."))

        self.label_9.setText(config.uilanglist.get("Translate channel"))
        self.translate_type.setToolTip('翻译字幕文字时使用的翻译渠道' if config.defaulelang=='zh' else 'Translation channels used in translating subtitle text')
        self.label.setText('网络代理'  if config.defaulelang=='zh' else  'Proxy')
        self.proxy.setPlaceholderText(config.uilanglist.get("proxy address"))
        self.listen_btn.setToolTip(config.uilanglist.get("shuoming01"))
        self.listen_btn.setText(config.uilanglist.get("Trial dubbing"))
        self.label_2.setText(config.uilanglist.get("Source lang"))
        self.source_language.setToolTip(config.uilanglist.get("The language used for the original video pronunciation"))
        self.label_3.setText(config.uilanglist.get("Target lang"))
        self.target_language.setToolTip(config.uilanglist.get("What language do you want to translate into"))
        self.tts_text.setText("配音渠道" if config.defaulelang == 'zh' else "Dubbing channel")
        self.label_4.setText(config.uilanglist.get("Dubbing role"))
        self.voice_role.setToolTip(config.uilanglist.get("No is not dubbing"))

        self.model_name.setToolTip(config.uilanglist.get(
            "From base to large v3, the effect is getting better and better, but the speed is also getting slower and slower"))
        self.split_type.setToolTip(config.uilanglist.get(
            "Overall recognition is suitable for videos with or without background music and noticeable silence"))
        self.label_8.setText(config.uilanglist.get("Embed subtitles"))
        self.subtitle_type.setToolTip(config.uilanglist.get("shuoming02"))

        self.label_6.setText(config.uilanglist.get("Dubbing speed"))
        self.voice_rate.setToolTip(config.uilanglist.get("Overall acceleration or deceleration of voice over playback"))
        self.voice_autorate.setToolTip(config.uilanglist.get("shuoming03"))
        self.voice_autorate.setText(config.uilanglist.get("Voice acceleration?"))
        self.video_autorate.setToolTip('视频自动慢速' if config.defaulelang == 'zh' else 'Video Auto Slow')
        self.video_autorate.setText('视频自动慢速' if config.defaulelang == 'zh' else 'Video Auto Slow')
        self.append_video.setToolTip(
            '如果配音时长大于视频时，是否视频末尾延长' if config.defaulelang == 'zh' else 'If the dubbing time is longer than the video time, is the end of the video extended?')
        self.append_video.setText('视频末尾延长?' if config.defaulelang == 'zh' else 'Extension video?')

        self.enable_cuda.setText(config.uilanglist.get("Enable CUDA?"))
        self.is_separate.setText(config.uilanglist.get("Preserve background music"))
        self.is_separate.setToolTip(
            config.uilanglist.get("If retained, the required time may be longer, please be patient and wait"))
        self.startbtn.setText(config.uilanglist.get("Start"))
        self.addbackbtn.setText(config.uilanglist.get("addbackbtn"))
        self.back_audio.setPlaceholderText(config.uilanglist.get("back_audio_place"))
        self.back_audio.setToolTip(config.uilanglist.get("back_audio_place"))
        self.stop_djs.setText(config.uilanglist.get("Pause"))
        self.import_sub.setText(config.uilanglist.get("Import srt"))

        self.set_line_role.setText(config.uilanglist.get("Set role by line"))
        self.menu_Key.setTitle(config.uilanglist.get("&Setting"))
        self.menu_TTS.setTitle(config.uilanglist.get("&TTSsetting"))
        self.menu_RECOGN.setTitle(config.uilanglist.get("&RECOGNsetting"))
        self.menu.setTitle(config.uilanglist.get("&Tools"))
        self.menu_H.setTitle(config.uilanglist.get("&Help"))
        self.toolBar.setWindowTitle("toolBar")
        self.actionbaidu_key.setText("百度翻译设置" if config.defaulelang == 'zh' else "Baidu Key")
        self.actionchatgpt_key.setText("OpenAI ChatGPT及兼容API" if config.defaulelang == 'zh' else "OpenAI ChatGPT API")
        self.actionopenaitts_key.setText("OpenAI TTS")
        self.actionopenairecognapi_key.setText(
            "OpenAI语音识别API" if config.defaulelang == 'zh' else 'OpenAI Speech to Text API')
        self.actionai302_key.setText("302.AI接入翻译" if config.defaulelang == 'zh' else "302.AI for translation")
        self.actionlocalllm_key.setText("本地兼容openAI大模型翻译" if config.defaulelang == 'zh' else "Local LLM  API")
        self.actionzijiehuoshan_key.setText("字节火山引擎模型翻译" if config.defaulelang == 'zh' else 'ByteDance Ark')
        self.actiondeepL_key.setText("DeepL Key")

        self.action_ffmpeg.setText("FFmpeg")
        self.action_ffmpeg.setToolTip(config.uilanglist.get("Go FFmpeg website"))
        self.action_git.setText("Github Repository")
        self.action_issue.setText(config.uilanglist.get("Post issue"))
        self.actiondeepLX_address.setText("DeepLX Api")
        self.actionott_address.setText("OTT离线翻译Api" if config.defaulelang == 'zh' else "OTT Api")
        self.actionclone_address.setText("原音色克隆TTS" if config.defaulelang == 'zh' else "Clone-Voice TTS")
        self.actionchattts_address.setText("ChatTTS")
        self.actionai302tts_address.setText("302.AI 接入配音" if config.defaulelang == 'zh' else '302.AI TTS')
        self.actiontts_api.setText("自定义TTS API" if config.defaulelang == 'zh' else "TTS API")
        self.actiontrans_api.setText("自定义翻译API" if config.defaulelang == 'zh' else "Transate API")
        self.actionzhrecogn_api.setText("zh_recogn中文语音识别" if config.defaulelang == 'zh' else "zh_recogn only Chinese")
        self.actionrecognapi.setText("自定义语音识别API" if config.defaulelang == 'zh' else "Custom Speech Recognition API")
        self.actionsttapi.setText("stt语音识别API" if config.defaulelang == 'zh' else "stt Speech Recognition API")
        self.actiondoubao_api.setText("豆包模型语音识别" if config.defaulelang == 'zh' else "Doubao")
        self.actiontts_gptsovits.setText("GPT-SoVITS TTS")
        self.actiontts_cosyvoice.setText("CosyVoice TTS")
        self.actiontts_fishtts.setText("Fish TTS")
        self.action_website.setText(config.uilanglist.get("Documents"))
        self.action_discord.setText("Discord")
        self.action_blog.setText("在线体验" if config.defaulelang == 'zh' else 'Online Experience')
        self.action_models.setText(config.uilanglist["Download Models"])
        self.action_dll.setText(config.uilanglist["Download cuBLASxx.dll"])
        self.action_gtrans.setText(config.transobj["miandailigoogle"])
        self.action_cuda.setText('CUDA & cuDNN')
        self.action_online.setText('免责声明' if config.defaulelang == 'zh' else 'Disclaimer')
        self.actiontencent_key.setText("腾讯翻译设置" if config.defaulelang == 'zh' else "Tencent Key")
        self.action_about.setText(config.uilanglist.get("Donating developers"))

        self.action_biaozhun.setText(config.uilanglist.get("Standard Function Mode"))
        self.action_biaozhun.setToolTip(
            '批量进行视频翻译，并可按照需求自定义所有配置选项' if config.defaulelang == 'zh' else 'Batch video translation with all configuration options customizable on demand')

        self.action_xinshoujandan.setText(config.uilanglist.get("action_xinshoujandan"))
        self.action_xinshoujandan.setToolTip(
            '按照默认设置，一键将视频从一种语言翻译为另一种语言并嵌入字幕和配音' if config.defaulelang == 'zh' else 'Translate videos from one language to another and embed subtitles and voiceovers in one click.')

        self.action_yuyinshibie.setText(config.uilanglist.get("Speech Recognition Text"))
        self.action_yuyinshibie.setToolTip(
            '批量将音频或视频中的语音识别为srt字幕' if config.defaulelang == 'zh' else 'Batch recognize speech in audio or video as srt subtitles')

        self.action_yuyinhecheng.setText(config.uilanglist.get("From  Text  Into  Speech"))
        self.action_yuyinhecheng.setToolTip(
            '根据srt字幕文件批量进行配音' if config.defaulelang == 'zh' else 'Batch dubbing based on srt subtitle files')

        self.action_tiquzimu.setText(config.uilanglist.get("Extract Srt And Translate"))
        self.action_tiquzimu.setToolTip(
            '批量将视频中的语音识别为字幕，并可选择是否同时翻译字幕' if config.defaulelang == 'zh' else 'Batch recognize speech in video as srt subtitles')

        self.action_yinshipinfenli.setText(config.uilanglist.get("Separate Video to audio"))
        self.action_yinshipinfenli.setToolTip(config.uilanglist.get("Separate audio and silent videos from videos"))

        self.action_yingyinhebing.setText(config.uilanglist.get("Video Subtitles Merging"))
        self.action_yingyinhebing.setToolTip(config.uilanglist.get("Merge audio, video, and subtitles into one file"))

        self.action_subtitleediter.setText('导入字幕并编辑' if config.defaulelang == 'zh' else 'Import Subtitle Editing')
        self.action_subtitleediter.setToolTip(
            '导入字幕并修改后导出' if config.defaulelang == 'zh' else 'Importing subtitles and exporting them after modifying them')

        self.action_hun.setText(config.uilanglist.get("Mixing 2 Audio Streams"))
        self.action_hun.setToolTip(config.uilanglist.get("Mix two audio files into one audio file"))

        self.action_fanyi.setText(config.uilanglist.get("Text  Or Srt  Translation"))
        self.action_fanyi.setToolTip(
            '将多个srt字幕文件批量进行翻译' if config.defaulelang == 'zh' else 'Batch translation of multiple srt subtitle files')

        self.action_hebingsrt.setText('合并两个字幕' if config.defaulelang == 'zh' else 'Combine Two Subtitles')
        self.action_hebingsrt.setToolTip(
            '将2个字幕文件合并为一个，组成双语字幕' if config.defaulelang == 'zh' else 'Combine 2 subtitle files into one to form bilingual subtitles')

        self.action_clearcache.setText("Clear Cache" if config.defaulelang != 'zh' else '清理缓存和配置')

        self.actionazure_key.setText("AzureGPT 翻译 " if config.defaulelang == 'zh' else 'AzureOpenAI Translation')
        self.actionazure_tts.setText("AzureAI 配音" if config.defaulelang == 'zh' else 'AzureAI TTS')
        self.actiongemini_key.setText("Gemini Pro")
        self.actionElevenlabs_key.setText("ElevenLabs.io TTS")
        self.actionyoutube.setText(config.uilanglist.get("Download from Youtube"))

        self.actionwatermark.setText('批量视频添加水印' if config.defaulelang == 'zh' else 'Add watermark to video')
        self.actionsepar.setText('人声/背景音分离' if config.defaulelang == 'zh' else 'Vocal & instrument Separate')
        self.actionsetini.setText('高级选项' if config.defaulelang == 'zh' else 'Options')

        self.actionvideoandaudio.setText('视频与音频合并' if config.defaulelang == 'zh' else 'Batch video/audio merger')
        self.actionvideoandaudio.setToolTip(
            '批量将视频和音频一一对应合并' if config.defaulelang == 'zh' else 'Batch merge video and audio one-to-one')

        self.actionvideoandsrt.setText('视频与字幕合并' if config.defaulelang == 'zh' else 'Batch Video Srt merger')
        self.actionvideoandsrt.setToolTip(
            '批量将视频和srt字幕一一对应合并' if config.defaulelang == 'zh' else 'Batch merge video and srt subtitles one by one.')

        self.actionformatcover.setText('音视频格式转换' if config.defaulelang == 'zh' else 'Batch Audio/Video conver')
        self.actionformatcover.setToolTip(
            '批量将音频和视频转换格式' if config.defaulelang == 'zh' else 'Batch convert audio and video formats')

        self.actionsubtitlescover.setText('字幕多格式转换' if config.defaulelang == 'zh' else 'Batch Subtitle Conversion')
        self.actionsubtitlescover.setToolTip(
            '批量将字幕文件进行格式转换(srt/ass/vtt)' if config.defaulelang == 'zh' else 'Batch convert subtitle formats (srt/ass/vtt)')
