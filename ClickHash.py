import hashlib
import os
import time
import ctypes
from ctypes import wintypes

# ==========================================
# 利用 ctypes 调用 Windows 原生 API 构建文件选择框
# ==========================================
class OPENFILENAME(ctypes.Structure):
    _fields_ = [
        ("lStructSize", wintypes.DWORD),
        ("hwndOwner", wintypes.HWND),
        ("hInstance", wintypes.HINSTANCE),
        ("lpstrFilter", wintypes.LPCWSTR),
        ("lpstrCustomFilter", wintypes.LPWSTR),
        ("nMaxCustFilter", wintypes.DWORD),
        ("nFilterIndex", wintypes.DWORD),
        ("lpstrFile", wintypes.LPWSTR),
        ("nMaxFile", wintypes.DWORD),
        ("lpstrFileTitle", wintypes.LPWSTR),
        ("nMaxFileTitle", wintypes.DWORD),
        ("lpstrInitialDir", wintypes.LPCWSTR),
        ("lpstrTitle", wintypes.LPCWSTR),
        ("Flags", wintypes.DWORD),
        ("nFileOffset", wintypes.WORD),
        ("nFileExtension", wintypes.WORD),
        ("lpstrDefExt", wintypes.LPCWSTR),
        ("lCustData", wintypes.LPARAM),
        ("lpfnHook", ctypes.c_void_p),
        ("lpTemplateName", wintypes.LPCWSTR),
        ("pvReserved", ctypes.c_void_p),
        ("dwReserved", wintypes.DWORD),
        ("FlagsEx", wintypes.DWORD)
    ]

def ask_open_filenames():
    ofn = OPENFILENAME()
    ofn.lStructSize = ctypes.sizeof(OPENFILENAME)
    ofn.lpstrTitle = "ClickHash - 请选择要校验的文件 (可框选/按Ctrl多选)"
    
    # 创建 32768 字符的超大缓冲区 (Windows 对话框最大支持容量)
    buffer = ctypes.create_unicode_buffer(32768)
    ofn.lpstrFile = ctypes.cast(buffer, wintypes.LPWSTR)
    ofn.nMaxFile = 32768
    
    # 核心修改：增加了 0x00000200 (OFN_ALLOWMULTISELECT) 允许多选
    # 0x00080000 (OFN_EXPLORER) | 0x00001000 (OFN_FILEMUSTEXIST) | 0x00000008 (OFN_NOCHANGEDIR)
    ofn.Flags = 0x00080000 | 0x00001000 | 0x00000008 | 0x00000200
    
    user32 = ctypes.windll.user32
    ofn.hwndOwner = user32.GetForegroundWindow()

    if ctypes.windll.comdlg32.GetOpenFileNameW(ctypes.byref(ofn)):
        # 将整个 buffer 转换为字符串
        raw_str = buffer[:]
        
        # 寻找双空字符 \0\0，这是系统标记多文件列表结束的地方
        end_idx = raw_str.find('\0\0')
        if end_idx != -1:
            valid_str = raw_str[:end_idx]
        else:
            valid_str = raw_str.strip('\0')
            
        # 根据 \0 分割字符串
        parts = valid_str.split('\0')
        
        # 解析逻辑
        if len(parts) == 1 and parts[0]:
            # 数组只有1个元素，说明用户只选了 1 个文件，直接返回绝对路径
            return [parts[0]]
        elif len(parts) > 1:
            # 选了多文件：第 0 个元素是文件夹路径，后面的全是文件名
            dir_path = parts[0]
            # 把文件夹路径和文件名拼接起来，组合成完整的绝对路径列表返回
            return [os.path.join(dir_path, f) for f in parts[1:]]
    return []

# ==========================================
# 核心哈希计算逻辑
# ==========================================
def calculate_hashes(file_path):
    hash_funcs = {
        "MD5": hashlib.md5(),
        "SHA-1": hashlib.sha1(),
        "SHA-256": hashlib.sha256(),
        "SHA-512": hashlib.sha512()
    }
    
    total_size = os.path.getsize(file_path)
    processed_size = 0
    start_time = time.time()
    
    if total_size == 0:
        return {name: func.hexdigest().upper() for name, func in hash_funcs.items()}, 0

    print(f"正在读取: {os.path.basename(file_path)}")
    
    try:
        last_percent = -1
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(65536), b""):
                for algo in hash_funcs.values():
                    algo.update(byte_block)
                
                processed_size += len(byte_block)
                percent = int((processed_size / total_size) * 100)
                
                if percent > last_percent:
                    bar_length = 30
                    filled_length = int(bar_length * percent // 100)
                    bar = '█' * filled_length + '-' * (bar_length - filled_length)
                    proc_mb = processed_size / (1024 * 1024)
                    tot_mb = total_size / (1024 * 1024)
                    
                    print(f'\r进度: [{bar}] {percent}% ({proc_mb:.1f}M / {tot_mb:.1f}M)', end='', flush=True)
                    last_percent = percent
                    
        print() 
        results = {name: func.hexdigest().upper() for name, func in hash_funcs.items()}
        cost_time = time.time() - start_time
        return results, cost_time
        
    except Exception as e:
        return None, f"\n读取文件出错: {e}"

# ==========================================
# 主程序
# ==========================================
def main():
    print("正在呼出文件选择窗口，请稍候...")
    
    # 获取返回的文件路径列表 (可能是一个，也可能是多个)
    file_paths = ask_open_filenames()

    if file_paths:
        os.system('cls' if os.name == 'nt' else 'clear') 
        
        total_files = len(file_paths)
        print(f"✅ 成功选择 {total_files} 个文件，开始批量处理...\n")
        
        # 遍历选中的每一个文件进行计算
        for index, file_path in enumerate(file_paths, 1):
            print(f"▶ [{index}/{total_files}] " + "="*50)
            
            results, time_or_err = calculate_hashes(file_path)
            
            if isinstance(results, dict):
                file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
                print(f"文件大小: {file_size_mb:.2f} MB")
                print(f"计算耗时: {time_or_err:.2f} 秒")
                print("-" * 60)
                
                for algo_name, hash_value in results.items():
                    print(f"{algo_name:<8}: {hash_value}")
            else:
                print(time_or_err)
                
            print("="*60 + "\n")
            
        print("🎉 所有文件处理完毕！")
    else:
        print("已取消选择。")

    input("\n按回车键退出...")

if __name__ == "__main__":
    main()
