#!/usr/bin/env python3

import os
import argparse
from typing import List
import gitignorefile


TEMP_IGNORE = ".pyrtemp_delete_me_ignore"
IGNORE_NAMES = [TEMP_IGNORE, '.gitignore']

file_list: List[str] = []


def process_directory(folder_path: str, check: callable, callback: callable):
    # 遍历文件夹中的所有文件和文件夹
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        if check(item_path):
            continue

        # 如果是文件且check返回True
        if os.path.isfile(item_path):
            callback(item_path)

        # 如果是文件夹
        elif os.path.isdir(item_path):
            # 递归调用自身
            process_directory(item_path, check, callback)


def write_to_prompt_file(file_list: List[str], directory: str, output_file: str):
    with open(output_file, 'w', encoding='utf-8') as f:
        for file in file_list:
            relative_file_path = os.path.relpath(file, directory)
            print(f"读取文件：{relative_file_path}")
            f.write(f"///** filename: {relative_file_path} **///\n\n")
            with open(file, 'r', encoding='utf-8') as file:
                f.write(file.read())
            f.write("\n\n")
        
        # 返回文件内字符数
        file_size = f.tell()

    return file_size



def main():
    parser = argparse.ArgumentParser(
        description='递归读取指定目录下的所有文件内容，并输出到prompt.txt文件中')
    parser.add_argument('-d', '--directory', type=str, default=os.getcwd(),
                        help='指定要递归读取的目录（默认使用当前运行目录）')
    parser.add_argument('-o', '--output', type=str, default='prompt.txt',
                        help='指定输出文件的文件名（默认输出到prompt.txt）')
    parser.add_argument('-i', '--ignore', type=str, nargs='*', default=[],
                        help='指定需要排除的文件或目录模式，可以指定多个')

    args = parser.parse_args()

    ignore_patterns: List[str] = args.ignore
    ignore_patterns.append(TEMP_IGNORE)

    if len(ignore_patterns) > 0:
        with open(os.path.join(args.directory, TEMP_IGNORE), 'w', encoding='utf-8') as f:
            for pattern in ignore_patterns:
                f.write(pattern + '\n')

    # 如果args.output不是绝对路径，则join(directory, output)
    if not os.path.isabs(args.output):
        output_file_path = os.path.join(os.getcwd(), args.output)

    # 将output_file_path的filename加入ignore列表
    ignore_patterns.append(os.path.basename(output_file_path))

    process_directory(
        args.directory,
        lambda x: gitignorefile.ignored(x, ignore_names=IGNORE_NAMES),
        file_list.append
    )
    
    print(f"共计 {os.path.relpath(file_list[0], args.directory)} 等 {len(file_list)} 个文件")
    file_size = write_to_prompt_file(file_list, args.directory, output_file_path)
    print(f"{file_size} 字符的内容已成功写入到 {output_file_path}")

    # 删除临时ignore文件
    if os.path.isfile(os.path.join(args.directory, TEMP_IGNORE)):
        os.remove(os.path.join(args.directory, TEMP_IGNORE))


if __name__ == "__main__":
    main()
