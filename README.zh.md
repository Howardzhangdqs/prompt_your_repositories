# Prompt Your Repository

<div align="center">

[English](README.md)

</div>

**Prompt Your Repository** 是一个Python脚本，用于递归读取指定目录中的所有文件内容，并将其输出到一个名为`prompt.txt`的文件中，同时添加格式化内容。该脚本允许用户根据指定的模式排除某些文件或目录。

## 功能

- **递归目录遍历**：脚本可以遍历指定目录中的所有文件和子目录。
- **文件排除**：用户可以指定模式来排除某些文件或目录不被处理。
- **格式化输出**：每个文件的内容会写入到一个输出文件中，文件名作为标题被格式化输出。
- **临时忽略文件**：脚本会创建一个临时的忽略文件，用于管理排除模式，脚本运行结束后会自动删除该文件。

## 系统要求

- Python 3.6或更高版本
- `gitignorefile` 模块

可以通过以下命令安装所需模块：

```bash
pip install gitignorefile
```

## 使用方法

可以通过以下命令运行脚本：

```bash
python3 main.py [-d DIRECTORY] [-o OUTPUT] [-i IGNORE [IGNORE ...]]
```

### 参数说明

- `-d, --directory`：指定要递归读取的目录。默认为当前工作目录。
- `-o, --output`：指定输出文件的文件名。默认为`prompt.txt`。
- `-i, --ignore`：指定要排除的文件或目录模式。可以指定多个模式。

### 示例

```bash
python3 main.py -d /path/to/directory -o output.txt -i "*.log" "tmp/*"
```

该命令将读取 `/path/to/directory` 目录中的所有文件，排除匹配 `*.log` 和 `tmp/` 目录下的所有文件，并将内容写入到 `output.txt` 文件中。

## 工作原理

1. 脚本递归遍历指定的目录。
2. 匹配忽略模式的文件将被跳过。
3. 每个文件的内容都会写入到输出文件中，并在文件头部添加文件名作为标题。
4. 临时忽略文件（`.pyrtemp_delete_me_ignore`）用于管理排除模式，执行完毕后会自动删除。

## 许可证

该项目使用MIT许可证。详情请参阅[LICENSE](LICENSE)文件。