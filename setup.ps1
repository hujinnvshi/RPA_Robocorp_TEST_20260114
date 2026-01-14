# Windows 11 RPA 环境自动配置脚本
# 需要以管理员身份运行

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "钉钉 RPA 环境自动配置脚本" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# 检查管理员权限
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "错误: 请以管理员身份运行此脚本" -ForegroundColor Red
    Write-Host "右键点击 PowerShell -> 以管理员身份运行" -ForegroundColor Yellow
    exit 1
}

# 1. 检查 Python
Write-Host "`n[1/7] 检查 Python..." -ForegroundColor Yellow
$pythonVersion = python --version 2>$null
if ($pythonVersion) {
    Write-Host "✓ Python 已安装: $pythonVersion" -ForegroundColor Green
} else {
    Write-Host "Python 未安装" -ForegroundColor Red
    $install = Read-Host "是否现在安装 Python? (y/n)"
    if ($install -eq "y" -or $install -eq "Y") {
        Write-Host "正在安装 Python 3.9..." -ForegroundColor Yellow
        winget install Python.Python.3.9 --accept-package-agreements --accept-source-agreements
        Write-Host "✓ Python 安装完成，请重新启动终端并再次运行此脚本" -ForegroundColor Green
        exit 0
    } else {
        Write-Host "跳过 Python 安装" -ForegroundColor Yellow
    }
}

# 2. 检查 Git
Write-Host "`n[2/7] 检查 Git..." -ForegroundColor Yellow
$gitVersion = git --version 2>$null
if ($gitVersion) {
    Write-Host "✓ Git 已安装: $gitVersion" -ForegroundColor Green
} else {
    Write-Host "Git 未安装" -ForegroundColor Red
    $install = Read-Host "是否现在安装 Git? (y/n)"
    if ($install -eq "y" -or $install -eq "Y") {
        Write-Host "正在安装 Git..." -ForegroundColor Yellow
        winget install Git.Git --accept-package-agreements --accept-source-agreements
        Write-Host "✓ Git 安装完成" -ForegroundColor Green
    }
}

# 3. 设置 PowerShell 执行策略
Write-Host "`n[3/7] 配置 PowerShell 执行策略..." -ForegroundColor Yellow
try {
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
    Write-Host "✓ 执行策略已设置为 RemoteSigned" -ForegroundColor Green
} catch {
    Write-Host "✗ 设置执行策略失败" -ForegroundColor Red
}

# 4. 创建虚拟环境（如果不存在）
Write-Host "`n[4/7] 配置 Python 虚拟环境..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "✓ 虚拟环境已存在" -ForegroundColor Green
} else {
    Write-Host "创建虚拟环境..." -ForegroundColor Yellow
    python -m venv venv
    if (Test-Path "venv") {
        Write-Host "✓ 虚拟环境已创建" -ForegroundColor Green
    } else {
        Write-Host "✗ 虚拟环境创建失败" -ForegroundColor Red
        exit 1
    }
}

# 5. 安装 Python 依赖
Write-Host "`n[5/7] 安装 Python 依赖包..." -ForegroundColor Yellow
Write-Host "这可能需要几分钟时间..." -ForegroundColor Cyan

try {
    & .\venv\Scripts\Activate.ps1

    # 升级 pip
    Write-Host "升级 pip..." -ForegroundColor Cyan
    python -m pip install --upgrade pip --quiet

    # 安装核心包
    Write-Host "安装 RPA Framework..." -ForegroundColor Cyan
    pip install rpaframework==22.5.0 --quiet
    pip install rpaframework-windows==5.1.0 --quiet
    pip install PyYAML --quiet
    pip install robocorp-log --quiet

    Write-Host "✓ 依赖包安装完成" -ForegroundColor Green

    # 验证安装
    Write-Host "`n已安装的包:" -ForegroundColor Cyan
    pip list | Select-String "rpaframework|PyYAML|robocorp"
} catch {
    Write-Host "✗ 依赖包安装失败: $_" -ForegroundColor Red
    exit 1
}

# 6. 创建必要目录
Write-Host "`n[6/7] 创建项目目录..." -ForegroundColor Yellow
$directories = @("output", "resources", "logs")
foreach ($dir in $directories) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
        Write-Host "✓ 已创建目录: $dir" -ForegroundColor Green
    } else {
        Write-Host "✓ 目录已存在: $dir" -ForegroundColor Green
    }
}

# 7. 检查项目文件
Write-Host "`n[7/7] 检查项目文件..." -ForegroundColor Yellow
$requiredFiles = @(
    "tasks.py",
    "robot.yaml",
    "conda.yaml",
    "resources/config.yaml",
    "README.md",
    "SETUP_GUIDE.md",
    "test_environment.py",
    "test_manual.py"
)

$allFilesExist = $true
foreach ($file in $requiredFiles) {
    if (Test-Path $file) {
        Write-Host "✓ $file" -ForegroundColor Green
    } else {
        Write-Host "✗ $file (缺失)" -ForegroundColor Red
        $allFilesExist = $false
    }
}

# 完成摘要
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "配置完成摘要" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

if ($allFilesExist) {
    Write-Host "✓ 环境配置完成！" -ForegroundColor Green
} else {
    Write-Host "⚠ 部分项目文件缺失，请检查" -ForegroundColor Yellow
}

Write-Host "`n下一步操作:" -ForegroundColor Yellow
Write-Host "  1. 激活虚拟环境:" -ForegroundColor White
Write-Host "     .\venv\Scripts\Activate.ps1" -ForegroundColor Cyan
Write-Host "`n  2. 运行环境测试:" -ForegroundColor White
Write-Host "     python test_environment.py" -ForegroundColor Cyan
Write-Host "`n  3. 运行手动测试:" -ForegroundColor White
Write-Host "     python test_manual.py" -ForegroundColor Cyan
Write-Host "`n  4. 阅读完整指南:" -ForegroundColor White
Write-Host "     README.md" -ForegroundColor Cyan
Write-Host "     SETUP_GUIDE.md" -ForegroundColor Cyan

Write-Host "`n重要提示:" -ForegroundColor Yellow
Write-Host "  - 确保已安装钉钉 Windows 客户端" -ForegroundColor White
Write-Host "  - 运行测试前先登录钉钉" -ForegroundColor White
Write-Host "  - 建议安装 UI 检查工具（Accessibility Insights）" -ForegroundColor White

Write-Host "`n========================================" -ForegroundColor Cyan
