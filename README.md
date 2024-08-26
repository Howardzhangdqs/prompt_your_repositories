# Prompt Your Repository

<div align="center">

[简体中文](README.zh.md)

</div>

**Prompt Your Repository** is designed to recursively read all files in a specified directory and output the content to a single file, `prompt.txt`, with additional formatting. The script allows you to exclude certain files or directories based on user-defined patterns.

## Features

- **Recursive Directory Traversal**: The script navigates through all files and subdirectories within a specified directory.
- **File Exclusion**: Users can specify patterns to exclude certain files or directories from processing.
- **Formatted Output**: Each file's content is written to a single output file, with a formatted header that includes the filename.
- **Temporary Ignore File**: A temporary ignore file is created to manage exclusions and is automatically deleted after the script completes.

## Requirements

- Python 3.6+

Install the required module with:

```bash
pip install gitignorefile
```

## Usage

To run the script, use the following command:

```bash
python3 main.py [-d DIRECTORY] [-o OUTPUT] [-i IGNORE [IGNORE ...]]
```

### Arguments

- `-d, --directory`: Specify the directory to recursively read. Defaults to the current working directory.
- `-o, --output`: Specify the name of the output file. Defaults to `prompt.txt`.
- `-i, --ignore`: Specify patterns to exclude files or directories. Multiple patterns can be specified.

### Example

```bash
python3 main.py -d /path/to/directory -o output.txt -i "*.log" "tmp/*"
```

This command reads all files in `/path/to/directory`, excluding files matching `*.log` and any files in the `tmp/` directory, and writes the content to `output.txt`.

## How It Works

1. The script recursively traverses the specified directory.
2. Files matching the ignore patterns are skipped.
3. Each file's content is written to the output file, with a header containing the filename.
4. A temporary ignore file (`.pyrtemp_delete_me_ignore`) manages exclusion patterns and is automatically removed after execution.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.