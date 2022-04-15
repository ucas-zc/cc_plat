# coding=utf-8
# 进程管理模块
from GuiModule import GuiModule


class Process:
    def __init__(self):
        """
        初始化接口
        """
        pass

    @classmethod
    def get_instance(cls):
        """
        获取单例
        :return: 单例
        """
        if not hasattr(Process, '_instance'):
            Process._instance = Process()
        return Process._instance

    def init(self):
        """
        进程初始化接口
        :return:
        """
        pass

    def start(self):
        """
        启动程序
        :return:
        """
        # 启动初始化界面
        GuiModule.get_instance().init_ui()
