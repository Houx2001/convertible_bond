# -*- encoding: utf-8 -*-

"""
 Http 网络请求工具
 
 Author: zsyoung
 
 Date: 2019/01/09 15:00
"""
import random

import requests
from retrying import retry

from constants.Constant import USER_AGENTS
from util import LogUtils


@retry(wait_fixed=3000, stop_max_attempt_number=9)
def get_html(url):
    """
    获取Html源码

    :param url: 链接地址
    :return: html源码
    """
    try:
        response = requests.get(url, headers=__gen_headers())
        response.encoding = response.apparent_encoding
        if response.status_code == 200:
            return response.text
        else:
            print("网络访问出错，非200")
    except:
        LogUtils.log('./error.log', url)
        raise Exception('网络异常')


@retry(wait_fixed=3000, stop_max_attempt_number=9)
def get_bytes(url):
    """
    获取File字节流

    :param url: File地址
    :return: response.content
    """

    try:
        response = requests.get(url, headers=__gen_headers())
        if response.status_code == 200:
            return response.content
        else:
            print("网络访问出错，非200")
    except:
        LogUtils.log('./error.log', url)
        raise Exception('网络异常')


@retry(wait_fixed=3000, stop_max_attempt_number=9)
def get_data(url, params):
    """
    获取File字节流

    :param params:
    :param url: File地址
    :return: response.content
    """

    try:
        response = requests.post(url, data=params, headers=__gen_headers())
        if response.status_code == 200:
            return response.content.decode("utf-8")
        else:
            print("网络访问出错，非200")
    except:
        LogUtils.log('./error.log', url)
        raise Exception('网络异常')


@retry(wait_fixed=3000, stop_max_attempt_number=9)
def get_data_by_session(login_url, data_url, login_params, data_params):
    """
    根据session获取数据

    :param login_url:
    :param data_url:
    :param login_params:
    :param data_params:
    :return:
    """

    try:
        session = requests.Session()
        headers = __gen_headers()
        # 在session中发送登录请求，此后这个session里就存储了cookie
        # 可以用print(session.cookies.get_dict())查看
        session.post(login_url, data=login_params, headers=headers)
    except:
        LogUtils.log('./error.log', login_url)
        raise Exception('网络异常')

    try:
        # 发送访问请求
        response = session.post(data_url, data=data_params, headers=headers)
        if response.status_code == 200:
            return response.content.decode("utf-8")
        else:
            print("网络访问出错，非200")
    except:
        LogUtils.log('./error.log', data_url)
        raise Exception('网络异常')


def __gen_headers():
    headers = {
        "User-Agent": USER_AGENTS[random.randint(0, len(USER_AGENTS) - 1)],
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    return headers
