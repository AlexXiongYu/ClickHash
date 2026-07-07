# ClickHash ⚡

一个极其轻量、极速的 Windows 文件哈希校验工具。告别繁琐的命令行，**点选即算**！

## ✨ 核心特性

- **极致轻量：** 摒弃臃肿的第三方 UI 库，底层直接调用 Windows 原生 C API，程序秒开，打包体积小。
- **批量处理：** 支持框选/键盘连选多个文件，自动排队批量校验。
- **极速读取：** 采用“流式分块读取”与“内存同步多算”技术，大文件只需读取一遍硬盘，IO 瓶颈降至最低。
- **不爆内存：** 无论文件是 1MB 还是 100GB，内存占用始终保持在常量级别 (约十几兆)。
- **实时进度：** 自带原生防卡顿动态进度条，清晰显示百分比和读取容量。
- **全能覆盖：** 一次性输出 MD5、SHA-1、SHA-256、SHA-512 四大主流校验值。

## 🚀 快速使用

### 方式一：直接运行源码 (适合开发者)

1. 确保电脑已安装 [Python 3.x](https://www.python.org/)。
2. 克隆或下载本仓库中的 `ClickHash.py` 文件。
3. 双击运行，或在终端中执行：
```bash
python ClickHash.py
```

### 方式二：打包成独立 .exe 程序 (无需 Python 环境)

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

## 💡 使用截图

<img width="1751" height="1048" alt="image" src="https://github.com/user-attachments/assets/0120361b-19ef-4daf-a701-0e824155983e" />


## 📄 协议

本项目基于 MIT 协议开源，欢迎自由使用和修改。
