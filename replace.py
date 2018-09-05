# -*- encoding: utf-8 -*-

import re


def replace_by_regex(file_need_to_be_replaced, regex):
    f = open(file_need_to_be_replaced, 'r+')
    s = f.read()
    f.seek(0, 0)
    f.truncate()
    f.write(re.sub(regex, '', s))
    f.close()
