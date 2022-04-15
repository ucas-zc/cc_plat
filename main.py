# coding=utf-8
# 主程序入口
# 2022-4-13
from Process import Process


# main函数
if __name__ == '__main__':
    Process.get_instance().init()
    Process.get_instance().start()
