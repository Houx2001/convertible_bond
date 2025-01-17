# -*- encoding: utf-8 -*-

"""
 日志工具
 
 Author: zsyoung
 
 Date: 2019/01/09 15:00
"""

import os
import time


def log(path, text):
    """
    生成日志

    :param path: 存储路径
    :param text: 日志内容
    :return: None
    """

    __check_path(path)

    localtime = time.asctime(time.localtime(time.time()))
    text = '\n' + localtime + ' ' + text

    with open(path, 'a', encoding='utf-8') as file:
        file.write(text)


def __check_path(path):
    file_name = path.split("/")[-1]
    dir_path = path.replace(file_name, '')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
