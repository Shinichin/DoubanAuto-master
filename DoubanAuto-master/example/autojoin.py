# -*- coding: utf-8 -*-
from group import join
from util import doubanutil
# 账号登录
if __name__ == "__main__":
    doubanutil.init_func()
    user_id = "193497089"
    join.auto_join_group(join.get_join_group_url("704882"))
