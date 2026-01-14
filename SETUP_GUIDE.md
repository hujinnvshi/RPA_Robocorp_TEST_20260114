# Windows 11 环境准备指南 - 钉钉 RPA 自动化测试

本文档详细介绍在 Windows 11 上配置 Robocorp RPA 开发和测试环境的完整步骤。

## 目录

- [系统要求](#系统要求)
- [第一步：安装 Python](#第一步安装-python)
- [第二步：安装 Git（可选）](#第二步安装-git可选)
- [第三步：安装钉钉客户端](#第三步安装钉钉客户端)
- [第四步：安装 Robocorp RPA Framework](#第四步安装-robocorp-rpa-framework)
- [第五步：安装 UI 检查工具](#第五步安装-ui-检查工具)
- [第六步：配置项目环境](#第六步配置项目环境)
- [第七步：验证环境](#第七步验证环境)
- [第八步：运行测试](#第八步运行测试)
- [常见问题排查](#常见问题排查)
- [附录：PowerShell 自动化脚本](#附录powershell-自动化脚本)

---

## 系统要求

- **操作系统**: Windows 11 (64-bit)
- **内存**: 至少 8GB RAM (推荐 16GB)
- **磁盘空间**: 至少 5GB 可用空间
- **权限**: 管理员权限（用于安装软件）

### 检查系统信息

```powershell
# 查看 Windows 版本
winver

# 查看系统信息
systeminfo

# 查看是否为 64 位系统
$env:PROCESSOR_ARCHITECTURE
```

---

## 第一步：安装 Python

### 方式 1：从官网安装（推荐）

1. **下载 Python**
   - 访问：https://www.python.org/downloads/
   - 下载 Python 3.9.x 或 3.10.x Windows installer (64-bit)

2. **安装 Python**
   ```
   重要：安装时务必勾选 ☑️ Add Python to PATH
   ```

   - 选择 "Install Now" 或 "Customize installation"
   - 确保勾选 "Add Python to PATH"

3. **验证安装**

   打开 PowerShell 或命令提示符：

   ```powershell
   # 检查 Python 版本
   python --version
   # 或
   python3 --version

   # 检查 pip 版本
   pip --version

   # 升级 pip
   python -m pip install --upgrade pip
   ```

### 方式 2：使用 Windows Store

```powershell
# 打开 Windows Store，搜索 Python 3.9 或 3.10
# 或直接使用命令
winget install Python.Python.3.9
```

### 方式 3：使用 Anaconda（适合数据科学场景）

1. 下载 Anaconda：https://www.anaconda.com/download
2. 安装后使用 Anaconda Prompt

```powershell
# 创建专门的环境
conda create -n rpa-dingtalk python=3.9
conda activate rpa-dingtalk
```

---

## 第二步：安装 Git（可选）

如果使用 Git 进行版本控制：

### 方式 1：官网下载

1. 下载 Git：https://git-scm.com/download/win
2. 安装时选择默认配置即可
3. 验证安装：

```powershell
git --version
```

### 方式 2：使用 winget

```powershell
winget install Git.Git
```

### 克隆项目（如果已有远程仓库）

```powershell
git clone <your-repository-url>
cd RPA_Robocorp_TEST_20260114
```

---

## 第三步：安装钉钉客户端

### 1. 下载钉钉

- 访问：https://www.dingtalk.com/
- 下载 Windows 版本

### 2. 安装并登录

```powershell
# 默认安装路径
C:\Users\{YOUR_USERNAME}\AppData\Local\DingTalk\DingtalkLauncher.exe
```

### 3. 测试钉钉

- 手动启动钉钉
- 登录账号
- 找到你要操作的功能模块（考勤、审批、报表等）
- 手动测试一遍完整流程
- 记录每个步骤的操作

### 4. 记录关键信息

在记事本中记录以下信息：

```
钉钉窗口标题：_________________________
功能模块路径：_________________________
开始日期控件：_________________________
结束日期控件：_________________________
查询按钮：_________________________
保存按钮：_________________________
导出文件默认位置：_________________________
```

---

## 第四步：安装 Robocorp RPA Framework

### 1. 创建项目目录

```powershell
# 如果还没有项目文件
mkdir C:\RPA_Projects
cd C:\RPA_Projects

# 复制项目文件到此目录
```

### 2. 创建虚拟环境（推荐）

```powershell
# 进入项目目录
cd C:\RPA_Projects\RPA_Robocorp_TEST_20260114

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
.\venv\Scripts\Activate.ps1

# 如果提示执行策略错误，先运行：
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. 安装 RPA Framework

```powershell
# 激活虚拟环境后
pip install --upgrade pip

# 安装核心框架
pip install rpaframework==22.5.0

# 安装 Windows 自动化库
pip install rpaframework-windows==5.1.0

# 安装其他依赖
pip install PyYAML robocorp-log
```

### 4. 验证安装

```powershell
# 检查已安装的包
pip list | Select-String rpaframework

# 应该看到类似输出：
# rpaframework               22.5.0
# rpaframework-windows       5.1.0
```

### 5. 安装 Robocorp CLI（可选）

```powershell
# 使用 pip 安装
pip install rcc

# 验证安装
rcc --version

# 如果提示无法识别，检查 PATH
# 或使用完整路径
python -m rcc --version
```

---

## 第五步：安装 UI 检查工具

这是**最关键**的一步！用于获取钉钉界面控件的信息。

### 方式 1：使用 Accessibility Insights for Windows（推荐）

1. **下载安装**
   - 访问：https://accessibilityinsights.io/downloads/
   - 下载 "Accessibility Insights for Windows"
   - 安装后打开应用

2. **使用方法**
   ```
   1. 打开 Accessibility Insights for Windows
   2. 打开钉钉客户端
   3. 在 Accessibility Insights 中选择 "Inspect" 模式
   4. 将鼠标悬停在钉钉的目标控件上
   5. 记录以下信息：
      - Name（控件名称）
      - AutomationId（自动化 ID）
      - ClassName（类名）
      - ControlType（控件类型）
   ```

3. **示例输出**
   ```
   Name: "开始日期"
   AutomationId: "startDateInput"
   ClassName: "EditControl"
   ControlType: "Edit"
   ```

### 方式 2：使用 Windows SDK 的 inspect.exe

1. **安装 Windows SDK**
   ```powershell
   # 使用 winget
   winget install Microsoft.WindowsSDK

   # 或访问
   # https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/
   ```

2. **找到并运行 inspect.exe**
   ```
   默认路径：
   C:\Program Files (x86)\Windows Kits\10\bin\<版本号>\x64\inspect.exe
   ```

3. **使用方法**
   - 打开 inspect.exe
   - 打开钉钉
   - 点击控件查看属性

### 方式 3：使用 UIAutomation 模块（Python 脚本）

创建一个辅助脚本：

```python
# 文件名：inspect_ui.py
from RPA import Windows
import time

def inspect_ui_elements():
    """简单的 UI 元素检查脚本"""
    windows = Windows()

    print("请在接下来的 5 秒内打开钉钉并定位到目标界面...")
    time.sleep(5)

    try:
        # 获取当前窗口的元素
        elements = windows.get_elements()

        print("\n找到的元素：")
        for i, elem in enumerate(elements):
            print(f"{i}: {elem}")

    except Exception as e:
        print(f"检查失败: {e}")

if __name__ == "__main__":
    inspect_ui_elements()
```

运行：

```powershell
python inspect_ui.py
```

### 方式 4：使用 pywinauto（备选方案）

```powershell
pip install pywinauto
```

创建检查脚本：

```python
# 文件名：inspect_pywinauto.py
from pywinauto import Application
import time

def inspect_with_pywinauto():
    """使用 pywinauto 检查控件"""
    print("请在 5 秒内打开钉钉...")
    time.sleep(5)

    try:
        # 连接到钉钉
        app = Application(backend="uia").connect(title="钉钉")
        dlg = app.window(title="钉钉")

        # 打印控件树
        dlg.print_control_identifiers()

    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    inspect_with_pywinauto()
```

---

## 第六步：配置项目环境

### 1. 编辑配置文件

使用记事本或 VS Code 打开：

```
notepad resources\config.yaml
```

根据第五步获取的控件信息，更新配置：

```yaml
dingtalk:
  window_title: "钉钉"  # 修改为实际的窗口标题
  controls:
    start_date_field: "实际的控件名称"  # 例如：startDateInput
    end_date_field: "实际的控件名称"    # 例如：endDateInput
    query_button: "查询"              # 或实际的按钮文本
    save_button: "保存"               # 或 "导出"
```

### 2. 更新 tasks.py

编辑 `tasks.py`，找到控件操作部分（约第 67 行），更新选择器：

```python
# 示例：根据实际情况修改
self.windows.set_focus("开始日期")  # 修改为实际控件名

# 或使用 AutomationId
# self.windows.set_focus(selector={"AutomationId": "startDateInput"})
```

### 3. 创建测试配置

创建 `test_config.py`：

```python
# 测试用的临时配置
TEST_START_DATE = "2024-01-01"
TEST_END_DATE = "2024-01-31"

# 如果你知道默认导出路径
DEFAULT_DOWNLOAD_DIR = r"C:\Users\YOUR_USERNAME\Downloads"
```

---

## 第七步：验证环境

### 1. 创建测试脚本

创建文件 `test_environment.py`：

```python
"""
环境测试脚本 - 验证所有组件是否正常工作
"""

def test_python_imports():
    """测试 Python 包导入"""
    print("=" * 60)
    print("测试 1: Python 包导入")
    print("=" * 60)

    try:
        from RPA import Windows
        print("✓ RPA.Windows 导入成功")

        from RPA.Excel.Files import Files as ExcelFiles
        print("✓ RPA.Excel.Files 导入成功")

        from RPA.FileSystem import FileSystem
        print("✓ RPA.FileSystem 导入成功")

        import yaml
        print("✓ PyYAML 导入成功")

        return True
    except ImportError as e:
        print(f"✗ 导入失败: {e}")
        return False


def test_project_files():
    """测试项目文件是否存在"""
    print("\n" + "=" * 60)
    print("测试 2: 项目文件检查")
    print("=" * 60)

    import os
    from pathlib import Path

    required_files = [
        "tasks.py",
        "robot.yaml",
        "conda.yaml",
        "resources/config.yaml"
    ]

    all_exist = True
    for file in required_files:
        exists = Path(file).exists()
        status = "✓" if exists else "✗"
        print(f"{status} {file}")
        if not exists:
            all_exist = False

    return all_exist


def test_directories():
    """测试目录结构"""
    print("\n" + "=" * 60)
    print("测试 3: 目录结构检查")
    print("=" * 60)

    from pathlib import Path

    dirs = ["output", "resources"]
    all_exist = True

    for dir_name in dirs:
        path = Path(dir_name)
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            print(f"✓ 已创建目录: {dir_name}")
        else:
            print(f"✓ 目录已存在: {dir_name}")

    return True


def test_config_loading():
    """测试配置文件加载"""
    print("\n" + "=" * 60)
    print("测试 4: 配置文件加载")
    print("=" * 60)

    try:
        import yaml
        from pathlib import Path

        with open("resources/config.yaml", "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)

        print("✓ 配置文件加载成功")
        print(f"  - 默认开始日期: {config['date_params']['default_start_date']}")
        print(f"  - 默认结束日期: {config['date_params']['default_end_date']}")

        return True
    except Exception as e:
        print(f"✗ 配置文件加载失败: {e}")
        return False


def main():
    """运行所有测试"""
    print("\n🔍 开始环境检查...\n")

    results = {
        "Python 包导入": test_python_imports(),
        "项目文件": test_project_files(),
        "目录结构": test_directories(),
        "配置加载": test_config_loading()
    }

    print("\n" + "=" * 60)
    print("测试总结")
    print("=" * 60)

    for test_name, passed in results.items():
        status = "✓ 通过" if passed else "✗ 失败"
        print(f"{test_name}: {status}")

    all_passed = all(results.values())

    if all_passed:
        print("\n✓ 所有测试通过！环境配置成功。")
        print("\n下一步：运行手动测试")
        print("  python test_manual.py")
    else:
        print("\n✗ 部分测试失败，请检查上述错误信息。")

    return all_passed


if __name__ == "__main__":
    main()
```

运行测试：

```powershell
python test_environment.py
```

---

## 第八步：运行测试

### 1. 创建手动测试脚本

创建文件 `test_manual.py`：

```python
"""
手动测试脚本 - 逐步验证每个功能
"""

from RPA import Windows
import time

def manual_test():
    """手动测试流程"""
    windows = Windows()

    print("=" * 60)
    print("钉钉 RPA 手动测试")
    print("=" * 60)

    # 测试 1: 激活窗口
    print("\n[测试 1] 尝试激活钉钉窗口...")
    print("请确保钉钉已打开并登录")
    input("按 Enter 继续...")

    try:
        windows.set_focus("钉钉")
        print("✓ 钉钉窗口已激活")
        time.sleep(2)
    except Exception as e:
        print(f"✗ 激活失败: {e}")
        print("提示: 请检查窗口标题是否正确")
        return

    # 测试 2: 测试开始日期输入
    print("\n[测试 2] 测试开始日期输入...")
    print("将鼠标放在开始日期输入框上")
    input("按 Enter 继续测试输入...")

    try:
        # 这里需要根据实际情况修改
        windows.send_keys("2024-01-01")
        print("✓ 已输入: 2024-01-01")
        time.sleep(1)
    except Exception as e:
        print(f"✗ 输入失败: {e}")

    # 测试 3: 测试 Tab 切换
    print("\n[测试 3] 测试 Tab 切换到结束日期...")
    input("按 Enter 继续...")

    try:
        windows.send_keys("{TAB}")
        time.sleep(0.5)
        windows.send_keys("2024-01-31")
        print("✓ 已输入结束日期: 2024-01-31")
        time.sleep(1)
    except Exception as e:
        print(f"✗ 输入失败: {e}")

    # 测试 4: 测试查询按钮
    print("\n[测试 4] 测试点击查询按钮...")
    input("按 Enter 继续...")

    try:
        # 可以尝试快捷键
        windows.send_keys("{ENTER}")
        print("✓ 已按回车键（假设触发查询）")
        print("请检查钉钉是否有反应...")
        time.sleep(3)
    except Exception as e:
        print(f"✗ 操作失败: {e}")

    print("\n" + "=" * 60)
    print("手动测试完成")
    print("=" * 60)
    print("\n请根据实际结果调整 tasks.py 中的参数")


if __name__ == "__main__":
    manual_test()
```

### 2. 运行手动测试

```powershell
# 确保虚拟环境已激活
.\venv\Scripts\Activate.ps1

# 运行手动测试
python test_manual.py
```

### 3. 运行完整任务

```powershell
# 运行主任务
python tasks.py
```

### 4. 使用 Robocorp CLI（如果已安装）

```powershell
# 初始化 Robocorp 项目
rcc cloud new

# 运行任务
rcc run --task query_and_export

# 或直接运行
robocorp run
```

---

## 常见问题排查

### 问题 1: PowerShell 执行策略错误

**错误信息**：
```
无法加载文件，因为在此系统上禁止运行脚本
```

**解决方案**：
```powershell
# 以管理员身份运行 PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 或临时绕过
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### 问题 2: Python 不在 PATH 中

**错误信息**：
```
'python' 不是内部或外部命令
```

**解决方案**：

方式 1 - 重新安装 Python 并勾选 "Add to PATH"

方式 2 - 手动添加到 PATH
```powershell
# 查看当前 PATH
$env:PATH

# 添加 Python 到 PATH（临时）
$env:PATH += ";C:\Users\YOUR_USERNAME\AppData\Local\Programs\Python\Python39"

# 永久添加（需要管理员权限）
[Environment]::SetEnvironmentVariable("Path", $env:PATH + ";C:\Python39", "User")
```

### 问题 3: 找不到钉钉窗口

**解决方案**：

1. 检查钉钉是否真的在运行
```powershell
# 查看进程
tasklist | findstr "DingTalk"
```

2. 检查窗口标题
```powershell
# 使用 Python 脚本列出所有窗口
python -c "from RPA import Windows; w = Windows(); print(w.get_window_titles())"
```

3. 更新 config.yaml 中的 `window_title`

### 问题 4: 无法识别控件

**解决方案**：

1. 使用 Accessibility Insights 获取准确信息
2. 尝试不同的选择器方式：
   - 控件名称 (Name)
   - AutomationId
   - ClassName
   - 控件索引

3. 使用键盘快捷键代替鼠标点击
```python
# Tab 切换 + Enter
windows.send_keys("{TAB}{TAB}{ENTER}")
```

### 问题 5: 权限不足

**解决方案**：

```powershell
# 以管理员身份运行 PowerShell
# 右键点击 PowerShell -> 以管理员身份运行

# 或在代码中添加 UAC 提示
```

### 问题 6: 依赖包冲突

**解决方案**：

```powershell
# 完全重新创建虚拟环境
deactivate  # 退出当前环境
Remove-Item -Recurse -Force venv  # 删除旧环境

python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt  # 或重新安装依赖
```

---

## 附录：PowerShell 自动化脚本

保存为 `setup.ps1`，可以自动化大部分安装步骤：

```powershell
# Windows 11 RPA 环境自动配置脚本
# 需要以管理员身份运行

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "钉钉 RPA 环境自动配置脚本" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# 检查管理员权限
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "错误: 请以管理员身份运行此脚本" -ForegroundColor Red
    exit 1
}

# 1. 安装 Python
Write-Host "`n[1/6] 检查 Python..." -ForegroundColor Yellow
$pythonVersion = python --version 2>$null
if ($pythonVersion) {
    Write-Host "✓ Python 已安装: $pythonVersion" -ForegroundColor Green
} else {
    Write-Host "正在安装 Python..." -ForegroundColor Yellow
    winget install Python.Python.3.9
}

# 2. 安装 Git
Write-Host "`n[2/6] 检查 Git..." -ForegroundColor Yellow
$gitVersion = git --version 2>$null
if ($gitVersion) {
    Write-Host "✓ Git 已安装: $gitVersion" -ForegroundColor Green
} else {
    Write-Host "正在安装 Git..." -ForegroundColor Yellow
    winget install Git.Git
}

# 3. 设置 PowerShell 执行策略
Write-Host "`n[3/6] 配置 PowerShell..." -ForegroundColor Yellow
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
Write-Host "✓ 执行策略已设置" -ForegroundColor Green

# 4. 创建虚拟环境（如果不存在）
Write-Host "`n[4/6] 配置 Python 虚拟环境..." -ForegroundColor Yellow
if (-not (Test-Path "venv")) {
    Write-Host "创建虚拟环境..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "✓ 虚拟环境已创建" -ForegroundColor Green
} else {
    Write-Host "✓ 虚拟环境已存在" -ForegroundColor Green
}

# 5. 安装 Python 依赖
Write-Host "`n[5/6] 安装 Python 依赖包..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install rpaframework==22.5.0
pip install rpaframework-windows==5.1.0
pip install PyYAML
pip install robocorp-log
Write-Host "✓ 依赖包安装完成" -ForegroundColor Green

# 6. 创建必要目录
Write-Host "`n[6/6] 创建项目目录..." -ForegroundColor Yellow
$directories = @("output", "resources", "logs")
foreach ($dir in $directories) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force
        Write-Host "✓ 已创建目录: $dir" -ForegroundColor Green
    }
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "✓ 环境配置完成！" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "`n下一步操作:" -ForegroundColor Yellow
Write-Host "1. 激活虚拟环境: .\venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host "2. 安装钉钉客户端（如未安装）" -ForegroundColor White
Write-Host "3. 运行环境测试: python test_environment.py" -ForegroundColor White
Write-Host "4. 运行手动测试: python test_manual.py" -ForegroundColor White
```

运行方式：
```powershell
# 右键点击 PowerShell -> 以管理员身份运行
cd C:\RPA_Projects\RPA_Robocorp_TEST_20260114
.\setup.ps1
```

---

## 快速参考卡

### 常用命令

```powershell
# 激活虚拟环境
.\venv\Scripts\Activate.ps1

# 退出虚拟环境
deactivate

# 运行测试
python test_environment.py

# 运行手动测试
python test_manual.py

# 运行主任务
python tasks.py

# 查看已安装的包
pip list

# 升级 pip
python -m pip install --upgrade pip
```

### 文件清单

```
必需文件:
✓ tasks.py              # 主任务脚本
✓ robot.yaml            # Robocorch 配置
✓ conda.yaml            # Conda 环境配置
✓ resources/config.yaml # 项目配置
✓ .gitignore           # Git 忽略文件
✓ README.md            # 项目说明
✓ SETUP_GUIDE.md       # 本文档

测试文件:
✓ test_environment.py  # 环境测试脚本
✓ test_manual.py       # 手动测试脚本
✓ inspect_ui.py        # UI 检查脚本（可选）

配置脚本:
✓ setup.ps1            # 自动配置脚本（可选）
```

---

## 需要帮助？

- Robocorp 文档: https://robocorp.com/docs
- RPA Framework 文档: https://rpaframework.org/
- Windows 自动化: https://rpaframework.org/libraries/windows/

---

**文档版本**: 1.0
**最后更新**: 2024-01-14
**适用系统**: Windows 11 (64-bit)
**Python 版本**: 3.9.x
