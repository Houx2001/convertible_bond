# -*- encoding: utf-8 -*-

"""
 登录工具

 Author: zsyoung

 Date: 2021/07/24 23:13
"""
import io
import sys

import requests

from kzz.Config import global_config


def jsl_login():
    # 改变标准输出的默认编码
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

    # 登录时需要POST的数据
    data = {
        'return_url': 'https://www.jisilu.cn/',
        'user_name': 'e8e96acdbda31f93a8469aa666221499',
        'password': 'bc2f47a84214030125d3811a3cd81be0',
        'net_auto_login': 1,
        '_post_type': 'ajax',
        'aes': 1
    }

    # 设置请求头
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

    # 登录时表单提交到的地址（用开发者工具可以看到）
    login_url = global_config.get('config', 'jsl_login_url')

    # 构造Session
    session = requests.Session()

    # 在session中发送登录请求，此后这个session里就存储了cookie
    # 可以用print(session.cookies.get_dict())查看

    resp = session.post(login_url, data)
    print(session.cookies.get_dict())

    # 登录后才能访问的网页
    url = global_config.get('config', 'jsl_url')

    # 发送访问请求
    resp = session.get(url)

    print(resp.content.decode('utf-8'))
