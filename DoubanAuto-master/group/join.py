# -*- coding: utf-8 -*-
import requests

from config import doubanurl
from util import doubanutil
from baiconfig import headers

def auto_join_group(join_group_url):
    # 自动加入小组
    print (join_group_url)
    r = requests.get(join_group_url, cookies=doubanutil.get_cookies(), headers=headers)
    doubanutil.logger.info("in func auto_join_group(), " + str(join_group_url) + ", status_code: " + str(r.status_code))
    return r


def get_join_group_url(group_id):
    # 获取加入小组的链接

    group_url = "https://www.douban.com/group/"+group_id+"/"
    return doubanutil.get_value_from_group_url(group_url, get_bn_join_group)


def get_bn_join_group(text):
    # 通过html提取自动加入小组的链接

    join_group_url_xpath = "//a[@class='bn-join-group ']/@href"
    # print(text)
    return doubanutil.get_value_from_html(text, join_group_url_xpath)
