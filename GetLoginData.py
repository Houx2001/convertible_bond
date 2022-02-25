import json

from Config import global_config
from util import LogUtils, HttpUtils


def get_jsl_data():
    """
    获取集思录数据
    :return:
    """
    jsl_login_url = global_config.get('config', 'jsl_login_url')
    jsl_url = global_config.get('config', 'jsl_url')
    # 登录时需要POST的数据
    login_data = {
        'return_url': 'https://www.jisilu.cn/',
        'user_name': 'e8e96acdbda31f93a8469aa666221499',
        'password': 'bc2f47a84214030125d3811a3cd81be0',
        'net_auto_login': 1,
        '_post_type': 'ajax',
        'aes': 1
    }
    # 不看交换债, 仅看已上市
    params = {'btype': 'C', 'listed': 'Y'}
    try:
        data = HttpUtils.get_data_by_session(jsl_login_url, jsl_url, login_data, params)
        json_data = json.loads(data)
        return json_data
    except:
        LogUtils.log('./error.log', "集思录数据获取异常")
        raise Exception('集思录数据获取异常')
