# -*- encoding: utf-8 -*-

"""
 常量设置

 Author: zsyoung

 Date: 2019/01/09 15:00
"""

# User-Agent
USER_AGENTS = [
    'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
    'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
    'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;',
    'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
    'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
    'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)',
    'Mozilla/5.0(Linux;U;Android2.3.7;en-us;NexusOneBuild/FRF91)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1',
    'Mozilla/5.0(iPad;U;CPUOS4_3_3likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8J2Safari/6533.18.5',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
]

# 请求时间间隔
SLEEP_TIME = 2

# 线程数
THREAD_COUNT = 2

# 存储路径
DIR_NAME = './三要素转债'

# excel文件头1
HEADER_1 = ["排名", "评分", "代码", "转债名称", "评级", "剩余年限", "剩余规模", "现价", "现价评分", "溢价率", "溢价率评分", "到期税前收益", "到期税前收益评分"]

# excel文件头2
HEADER_2 = ["排名", "评分", "代码", "转债名称", "评级", "剩余年限", "剩余规模", "现价", "溢价率", "到期税前收益"]

# excel文件头3
HEADER_3 = ["排名", "评分", "代码", "转债名称", "评级", "剩余年限", "剩余规模", "PB", "正股代码", "正股名称", "双低", "现价", "溢价率", "到期税前收益"]
