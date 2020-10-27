# -*- coding: utf-8 -*-
import random
import time
import requests
from lxml import etree
from group import comment
from config import doubanurl
from util import doubanutil
from baiconfig import headers

if __name__ == "__main__":
    group_id = "699571"
    group_url = "https://www.douban.com/group/"+group_id+"/"
    r = requests.get(group_url, cookies=doubanutil.get_cookies(), headers=headers)
    group_topics_html = etree.HTML(r.text)
    group_topics = group_topics_html.xpath("//table[@class='olt']/tr[@class='']/td[@class='title']/a/@href")
    group_topics = group_topics[3:]
    print(group_topics)
    # print (r.text)
    for topic_url in group_topics:
        comment_topic_url = topic_url + "/add_comment"
        list_data = []
        list_data2 = []
        with open("D:\\douban\\DoubanAuto-master\\DoubanAuto-master\\data\\reponse.txt", "r", encoding="utf-8") as fr:
            list_data = fr.readlines()
            for i in list_data:
                temp_line = i.strip()  # 去除每行的\n
                list_data2.append(temp_line)
        print(list_data2)
        random_index = random.randint(0, len(list_data2) - 1)
        print(random_index)
        print(list_data2[random_index])

        comment_str = list_data2[random_index]
        print("顶帖:"+topic_url)
        comment_dict = comment.make_comment_dict(topic_url, comment_str)
        comment.comment_topic(comment_topic_url, comment_dict)
        random_sleep = random.randint(10, 50)
        time.sleep(random_sleep)