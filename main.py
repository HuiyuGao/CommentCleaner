# -*- encoding: utf-8 -*-

import re
import time
import sys

from replace import replace_by_regex
from transverse import transverse, real_paths_to_process

# get the dir path
dir_path = sys.argv[1]

single_line = r'(?<!:)\/\/.*'

multi_line = r'\/\*{1,2}[\s\S]*?\*\/'

pragma_mark = r'#pragma .*'

final_regex_list = [single_line, multi_line, pragma_mark]

final_regex = str.join('|', final_regex_list)

# 开始时间
start_time = time.time()
print("start: ", time.asctime(time.localtime(start_time)))

# 得到所有 paths
transverse(dir_path)

for file in real_paths_to_process:
    print("正在处理: ", file)
    replace_by_regex(file, final_regex)

print('よかった SUCCESS!')
# 结束时间
end_time = time.time()
print("end: ", time.asctime(time.localtime(end_time)))
print("用时: ", end_time - start_time)
