# coding=utf-8
# 本文件实现程序的界面
import tkinter as tk
from tkinter import messagebox
import _tkinter as _tk
from sys_cfg import *
from PIL import Image, ImageTk


class GuiModule:
    def __init__(self):
        """
        初始化接口
        """
        # 初始化一个窗口实例
        self.__root_window = tk.Tk()
        # 登录密码
        self.__passwd_entry = None
        # 搜索输入
        self.__search_entry = None
        self.__search_button = None
        # 应用变量
        # MiniAlphaGo
        self.__mini_pic = None
        self.__mini_name = None

    @classmethod
    def get_instance(cls):
        """
        获取单例
        :return:
        """
        if not hasattr(GuiModule, '_instance'):
            GuiModule._instance = GuiModule()
        return GuiModule._instance

    def init_ui(self):
        """
        初始化界面
        :return:
        """
        # 去除最大最小化按钮
        self.__root_window.attributes("-toolwindow", 2)
        # 设置窗口标题
        self.__root_window.title("超超平台")
        # 设置背景颜色
        self.__root_window.config(background="white")
        # 设置窗口尺寸
        self.__root_window.geometry("300x400")
        # 设置“登录”字体
        title = tk.Label(self.__root_window, text="* 登录平台",
                         fg="black", borderwidth=40,
                         background="white", font=('等线', 16, 'bold'))
        title.pack()
        # 输入密码
        self.__passwd_entry = tk.Entry(self.__root_window, show='*')
        self.__passwd_entry.pack(padx=20, pady=30)
        # 登录按钮
        login_button = tk.Button(self.__root_window, text='登 录',
                                 background='Gray', padx=53, pady=2,
                                 command=self.__login_callback)
        login_button.pack(padx=5, pady=30)
        # 底部字体
        foot = tk.Label(self.__root_window, text=version,
                        fg="black", borderwidth=60,
                        background="white", font=('等线', 12, 'bold'))
        foot.pack()
        # 窗口循环
        self.__root_window.mainloop()

    def __login_callback(self):
        """
        登录回调函数
        :return:
        """
        passwd = self.__passwd_entry.get()
        if passwd == '':
            messagebox.showinfo(title='温馨提示', message='密码为空！')
        elif passwd == '123456789':
            print(passwd)
            self.__main_ui()
        else:
            messagebox.showinfo(title='温馨提示', message='密码错误！')

    def __main_ui(self):
        """
        主页面
        :return:
        """
        # 销毁界面，重启界面
        self.__root_window.destroy()
        self.__root_window = tk.Tk()
        # 设置icon图标
        self.__root_window.iconbitmap(icon_path)
        # 标题为空
        self.__root_window.title('PLAT')
        # 设置窗口尺寸
        self.__root_window.geometry("900x600")
        # 左侧导航
        self.__main_left_menu()
        # 创建界面控件
        self.__create_component()
        # 循环显示窗口
        self.__root_window.mainloop()

    def __main_left_menu(self):
        """
        主页面左侧菜单
        :return:
        """
        # logo
        menu_logo = self.__create_menu('#303030', 'white', 'ZC',
                                       ('宋体', 15, 'bold', 'underline'))
        menu_logo.place(x=0, y=0, height=50, width=50)
        # 菜单顶端
        menu_top = self.__create_menu('#303030')
        menu_top.place(x=0, y=50, height=50, width=50)
        # 应用菜单项
        memu_app = self.__create_menu('#303030', 'white', '应用',
                                      ('宋体', 10), self.__app_callback)
        memu_app.place(x=0, y=100, height=40, width=50)
        # 系统配置菜单项
        menu_cfg = self.__create_menu('#303030', 'white', '配置',
                                      ('宋体', 10), self.__cfg_callback)
        menu_cfg.place(x=0, y=140, height=40, width=50)
        # 设置菜单项
        menu_set = self.__create_menu('#303030', 'white', '设置',
                                      ('宋体', 10), self.__set_callback)
        menu_set.place(x=0, y=180, height=40, width=50)
        # 菜单底部
        menu_foot = self.__create_menu('#303030')
        menu_foot.place(x=0, y=220, height=340, width=50)
        sys_version = self.__create_menu('#303030', 'white',
                                         version, ('宋体', 10))
        sys_version.place(x=0, y=560, height=40, width=50)

    def __create_menu(self, color, fg=None, text=None, font=None,
                      callback=None):
        """
        创建按钮
        :param color: 背景颜色
        :param fg: 字体颜色
        :param text: 文字
        :param font: 字体格式
        :param callback: 选项回调函数
        :return: 菜单控件
        """
        menu = tk.Label(self.__root_window, background=color,
                        fg=fg, text=text, font=font)
        if callback is not None:
            menu.bind('<Button-1>', callback)
        return menu

    def __create_component(self):
        """
        创建控件
        :return:
        """
        # 创建app控件
        self.__create_app()

    def __app_callback(self, event):
        """
        应用菜单回调函数
        :param event:
        :return:
        """
        # 应用列表
        self.__place_app()

    def __cfg_callback(self, event):
        """
        配置菜单回调函数
        :param event:
        :return:
        """
        self.__forget_app()

    def __set_callback(self, event):
        """
        配置菜单回调函数
        :param event:
        :return:
        """
        self.__forget_app()

    def __search_func(self):
        """
        搜索函数
        :return:
        """
        tmp = self.__search_entry.get()
        print(tmp)

    def __create_search(self):
        """
        创建搜索框
        :return:
        """
        # 搜索框
        self.__search_entry = tk.Entry(self.__root_window,
                                       background="#D3D3D3")
        # 搜索按钮
        self.__search_button = tk.Button(self.__root_window, text='+',
                                         background='#D3D3D3', font=('宋体', 15),
                                         activebackground="#D3D3D3",
                                         command=self.__search_func)

    def __create_app(self):
        """
        创建app列表
        :return:
        """
        # 显示搜索框
        self.__create_search()
        # Mini Alpha Go
        # 图标
        if os.path.exists(mini_path):
            try:
                mini_open = Image.open(mini_path)
                global mini_photo
                mini_photo = ImageTk.PhotoImage(mini_open)
                self.__mini_pic = tk.Label(self.__root_window, image=mini_photo)
            except _tk.TclError:
                pass
        # app名称
        self.__mini_name = tk.Label(self.__root_window, background="#F5F5F5",
                                    fg='black', text='Mini Alpha Go', font=('宋体', 12))
        self.__mini_name.bind('<Button-1>', self.__mini_alpha_go)

    def __forget_app(self):
        """
        隐藏应用选项
        :return:
        """
        # 隐藏搜索框
        self.__search_entry.place_forget()
        self.__search_button.place_forget()
        self.__mini_pic.place_forget()
        self.__mini_name.place_forget()

    def __place_app(self):
        """
        恢复应用选项
        :return:
        """
        self.__search_entry.place(x=65, y=15, height=25, width=140)
        self.__search_button.place(x=215, y=15, height=25, width=25)
        self.__mini_pic.place(x=60, y=50, height=40, width=40)
        self.__mini_name.place(x=100, y=50, height=40, width=150)

    def __mini_alpha_go(self, event):
        """
        MiniAlphaGo
        :param event:
        :return:
        """
        print('MiniAlphaGo')
