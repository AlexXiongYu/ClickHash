# ClickHash ⚡

[English](#english) | [简体中文](#简体中文)

---

<h2 id="english">English</h2>

An ultra-lightweight, lightning-fast file hash calculator for Windows. Say goodbye to tedious command lines, **just click and calculate**!

### ✨ Core Features

- **Extremely Lightweight:** Abandons bloated third-party UI libraries, directly calls native Windows C APIs. The program opens instantly with a tiny packaged size.
- **Batch Processing:** Supports selecting multiple files via marquee or keyboard shortcuts, automatically queuing them for batch validation.
- **Lightning-Fast Reading:** Employs "streamed block reading" and "synchronous memory multi-calculation" technologies. Large files only need to be read from the disk once, minimizing IO bottlenecks.
- **Zero Memory Bloat:** Whether the file is 1MB or 100GB, memory usage remains constant (around a dozen MBs).
- **Real-time Progress:** Features a native, stutter-free dynamic progress bar, clearly displaying percentage and read capacity.
- **All-Around Coverage:** Outputs MD5, SHA-1, SHA-256, and SHA-512 in one go.

### 🚀 Quick Start

#### Method 1: Run from Source (For Developers)

1. Ensure you have [Python 3.x](https://www.python.org/) installed.
2. Clone or download the `ClickHash.py` file from this repository.
3. Double-click to run, or execute in the terminal:
```bash
python ClickHash.py
```

#### Method 2: Package as Standalone .exe (No Python Required)

If you want to share it with friends who don't have Python installed, use PyInstaller to package it:

1. Install the packaging tool:
```bash
pip install pyinstaller
```
2. Execute the single-file packaging command:
```bash
pyinstaller -F ClickHash.py
```
3. Find `ClickHash.exe` in the generated `dist` folder. Anyone can double-click to use it!

### 💡 Screenshots

*(Paste your program's running screenshot here. GitHub will automatically convert it into an image link.)*

### 📄 License

This project is licensed under the MIT License. Feel free to use and modify it.

---

<h2 id="简体中文">简体中文</h2>

一个极其轻量、极速的 Windows 文件哈希校验工具。告别繁琐的命令行，**点选即算**！

### ✨ 核心特性

- **极致轻量：** 摒弃臃肿的第三方 UI 库，底层直接调用 Windows 原生 C API，程序秒开，打包体积小。
- **批量处理：** 支持框选/键盘连选多个文件，自动排队批量校验。
- **极速读取：** 采用“流式分块读取”与“内存同步多算”技术，大文件只需读取一遍硬盘，IO 瓶颈降至最低。
- **不爆内存：** 无论文件是 1MB 还是 100GB，内存占用始终保持在常量级别 (约十几兆)。
- **实时进度：** 自带原生防卡顿动态进度条，清晰显示百分比和读取容量。
- **全能覆盖：** 一次性输出 MD5、SHA-1、SHA-256、SHA-512 四大主流校验值。

### 🚀 快速使用

#### 方式一：直接运行源码 (适合开发者)

1. 确保电脑已安装 [Python 3.x](https://www.python.org/)。
2. 克隆或下载本仓库中的 `ClickHash.py` 文件。
3. 双击运行，或在终端中执行：
```bash
python ClickHash.py
```

#### 方式二：打包成独立 .exe 程序 (无需 Python 环境)

如果你想发给没有安装 Python 的朋友使用，可以使用 PyInstaller 进行打包：

1. 安装打包工具：
```bash
pip install pyinstaller
```
2. 执行单文件打包命令：
```bash
pyinstaller -F ClickHash.py
```
3. 在生成的 `dist` 文件夹中找到 `ClickHash.exe`，发给任何人双击即可使用！

### 💡 使用截图

*(在此处粘贴你的程序运行截图，GitHub 会自动将其转换为图片链接)*

### 📄 协议

本项目基于 MIT 协议开源，欢迎自由使用和修改。
