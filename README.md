---

# autounrar - 自动解压 RAR 压缩包的 Python 库  
# autounrar - Automatically Unrar RAR Archives in Python

---

## 简介 / Introduction  
`autounrar` 是一个 Python 库，旨在简化 RAR 压缩包的处理。它会自动下载 `unrar.exe`，并使用它来解压 RAR 压缩包或列出压缩包中的文件列表。无需手动安装或配置 `unrar.exe`，所有操作均可通过 Python 脚本完成。

`autounrar` is a Python library designed to simplify handling RAR archives. It automatically downloads `unrar.exe` and uses it to extract RAR archives or list their contents. No need to manually install or configure `unrar.exe`; all operations can be done via Python scripts.

---

## 安装 / Installation  
通过 pip 安装 `autounrar`：  
Install `autounrar` via pip:  

```bash
pip install autounrar
```

---

## 使用示例 / Usage Example  

```python
from autounrar import unrar

# 列出RAR压缩包中的文件 / List files in the RAR archive  
file_list = unrar.list('example.rar')  
print("Files in the archive:", file_list)  

# 解压RAR压缩包到指定目录 / Extract RAR archive to a specific directory  
unrar.extract('example.rar', 'output_directory')  

# 解压RAR压缩包到当前目录 / Extract RAR archive to the current directory  
unrar.extract('example.rar')  
```

---

## 功能 / Features  
- 自动下载 `unrar.exe`：无需手动安装，直接通过库完成下载。  
  - **Automatically download `unrar.exe`**: No need for manual installation; directly handled by the library.  
- 列出压缩包内容：快速查看 RAR 压缩包中的文件列表。  
  - **List archive contents**: Quickly view the file list in a RAR archive.  
- 解压文件：将 RAR 压缩包解压到指定目录。  
  - **Extract files**: Extract RAR archives to a specified directory.  

---

## 依赖 / Dependencies  
- Python 3.6 或更高版本。  
  - **Python 3.6 or higher**  
- `subprocess` 库  
  - `subprocess` library  
- `requests` 库  
  - `requests` library  
- `appdirs` 库  
  - `appdirs` library  
- `os` 库  
  - `os` library  
- 需要网络连接以下载 `unrar.exe`。  
  - **Internet connection required to download `unrar.exe`**  

---

## 许可证 / License  
本项目基于 MIT 许可证发布，请查看 [LICENSE](LICENSE) 文件获取更多信息。  
This project is released under the MIT License. See the [LICENSE](LICENSE) file for more details.  

---

## 贡献 / Contribution  
欢迎提交 Pull Request 或 Issue 来改进本库！  
We welcome Pull Requests or Issues to improve this library!  

---

## 支持 / Support  
如有问题或建议，请在 [Issues](https://github.com/Jeffrey131313/unrar/issues) 中反馈。  
If you have any issues or suggestions, please report them in the [Issues](https://github.com/Jeffrey131313/unrar/issues) section.

---

> **Note:** 本项目仅为学习目的，请勿用于非法用途。  
> **Note:** This project is for educational purposes only. Do not use it for illegal purposes.

---
