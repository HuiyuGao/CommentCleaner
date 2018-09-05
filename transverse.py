# -*- encoding: utf-8 -*-

from config import *

import os

# store the real_path for every file that need to process
real_paths_to_process = []


def transverse(dir):
    '''
    :param dir: must be a directory
    :return:
    '''
    for file in os.listdir(dir):
        real_path = os.path.join(dir, file)

        # <editor-fold desc="filter"
        if os.path.isdir(real_path) and ignore_dir_name.__contains__(file):
            continue
        if os.path.isfile(real_path):
            # 如果是文件，那么扩展名为 ignore_extension 或者名称为 ignore_file_name 都要忽略
            (path, file_name) = os.path.split(real_path)
            if ignore_file_name.__contains__(file_name):
                continue
            (_, extension_name) = os.path.splitext(file_name)
            if not process_file_extension.__contains__(extension_name):
                continue
        # </editor-fold>
        if os.path.isdir(real_path):
            transverse(real_path)
        else:
            real_paths_to_process.append(real_path)