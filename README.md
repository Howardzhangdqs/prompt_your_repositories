# Prompt Your Repository

将你的仓库转换为提示词。

## Usage

```
usage: main.py [-h] [-d DIRECTORY] [-o OUTPUT]
               [-i [IGNORE ...]]

递归读取指定目录下的所有文件内容，并输出到prompt.txt文件中

options:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        指定要递归读取的目录（默认使用当前运行目录）
  -o OUTPUT, --output OUTPUT
                        指定输出文件的文件名（默认输出到prompt.txt）
  -i [IGNORE ...], --ignore [IGNORE ...]
```

## Example

```shell
python main.py -d . -o prompt.txt -i ".git" ".idea" "node_modules"
```