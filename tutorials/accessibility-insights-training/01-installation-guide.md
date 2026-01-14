# 教程 1: 工具安装指南

## 📋 本教程目标

完成本教程后，你将：
- 了解什么是 Accessibility Insights for Windows
- 成功安装工具到你的电脑
- 验证工具可以正常使用

---

## 🎯 什么是 Accessibility Insights for Windows？

### 简介
Accessibility Insights for Windows 是微软开发的**免费工具**，主要用于：
- 🔍 检查 Windows 应用程序的可访问性
- 🌲 查看应用程序的 UI 元素树结构
- 📋 获取控件的详细属性信息
- 🎯 帮助 RPA 开发者定位自动化元素

### 为什么 RPA 开发需要它？
```
问题: 钉钉有上百个按钮和输入框，如何告诉电脑点击哪一个？

解决: Accessibility Insights 可以"透视"钉钉界面，
      显示每个按钮的唯一标识信息

类比: 就像给钉钉的每个按钮都贴上了"姓名标签"
     "发送按钮" → AutomationId: "send_btn"
     "搜索框"   → AutomationId: "search_input"
```

---

## 💻 系统要求

在开始安装前，请确认你的系统满足以下要求：

| 要求项 | 最低配置 | 推荐配置 |
|--------|---------|---------|
| **操作系统** | Windows 10 1809+ | Windows 11 |
| **系统架构** | x64 | x64 |
| **内存** | 4 GB | 8 GB 或更多 |
| **磁盘空间** | 500 MB | 1 GB |
| **权限** | 管理员权限（安装时） | 管理员权限 |

### 检查系统版本
```powershell
# 在 PowerShell 中运行
winver

# 或
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
```

---

## 📥 安装方法

### 方法 1️⃣: Microsoft Store 安装（推荐）

**优点:** 自动更新，安装最简单

#### 步骤：

**第 1 步:** 打开 Microsoft Store
- 按 `Win + S` 搜索 "Microsoft Store"
- 或在开始菜单中找到 "Microsoft Store"

**第 2 步:** 搜索工具
```
在搜索框输入: Accessibility Insights for Windows
```

**第 3 步:** 安装应用
- 点击 "获取" 或 "安装" 按钮
- 等待下载和安装完成（约 2-5 分钟）

**第 4 步:** 启动应用
- 安装完成后点击"打开"
- 或在开始菜单搜索 "Accessibility Insights"

---

### 方法 2️⃣: GitHub 直接下载

**优点:** 可选择特定版本，无需 Microsoft 账户

#### 步骤：

**第 1 步:** 访问发布页面
```
浏览器打开: https://github.com/microsoft/accessibility-insights-windows/releases
```

**第 2 步:** 下载安装包
- 找到最新版本（标记为 "Latest release"）
- 在 "Assets" 部分下载文件：
  - 文件名格式: `AccessibilityInsights.VERSION.msix`
  - 例如: `AccessibilityInsights.1.1.2001.01.msix`

**第 3 步:** 安装应用
```
方法 A: 双击安装
1. 找到下载的 .msix 文件
2. 双击文件
3. 在弹出的窗口中点击"安装"

方法 B: PowerShell 安装
1. 右键点击开始菜单，选择 "Windows PowerShell (管理员)"
2. 运行命令:
   Add-AppxPackage "路径\AccessibilityInsights.VERSION.msix"
   例如:
   Add-AppxPackage "C:\Downloads\AccessibilityInsights.1.1.2001.01.msix"
```

---

### 方法 3️⃣: 使用 winget 命令行工具

**优点:** 最快速，适合开发者

#### 步骤：

**第 1 步:** 打开终端
- 按 `Win + X` 选择 "Windows PowerShell" 或 "终端"
- 或按 `Win + R` 输入 `powershell`

**第 2 步:** 运行安装命令
```powershell
# 搜索应用
winget search "Accessibility Insights"

# 安装应用
winget install Microsoft.AccessibilityInsights.Windows

# 等待安装完成...
```

**第 3 步:** 启动应用
```powershell
# 启动命令
explplorer shell:AppsFolder\Microsoft.AccessibilityInsights.Windows_8wekyb3d8bbwe!App
```

---

## ✅ 验证安装成功

安装完成后，让我们验证工具是否正常工作：

### 验证步骤

**1. 启动应用**
```
方法 1: 开始菜单
- 按 Win 键
- 搜索 "Accessibility Insights"
- 点击打开

方法 2: 命令行
- 按 Win + R
- 输入: AccessibilityInsights.Windows
- 按回车
```

**2. 检查主界面**
启动后，你应该看到：
```
┌─────────────────────────────────────┐
│  Accessibility Insights             │
├─────────────────────────────────────┤
│  [Inspect]  [Test]  [Issues]        │
│                                     │
│  请选择要检查的应用程序...            │
│                                     │
└─────────────────────────────────────┘
```

**3. 测试基本功能**
- 确保 "Inspect" 按钮可以点击
- 确保界面可以正常拖动和缩放
- 确保没有错误提示

---

## 🐛 常见安装问题

### 问题 1: "安装失败，错误代码 0x80070005"

**原因:** 权限不足

**解决方法:**
```powershell
# 以管理员身份运行 PowerShell
# 右键点击开始菜单 → "Windows PowerShell (管理员)"

# 然后重新运行安装命令
```

---

### 问题 2: "此应用无法在你的电脑上运行"

**原因:** Windows 版本过低

**解决方法:**
```
1. 更新 Windows 到最新版本
   - 设置 → 更新和安全 → Windows 更新
   - 点击"检查更新"

2. 最低要求: Windows 10 1809 或更高版本
```

---

### 问题 3: Microsoft Store 无法打开

**原因:** Store 服务未运行

**解决方法:**
```powershell
# 以管理员身份运行 PowerShell
wsreset.exe

# 这会重置 Microsoft Store 缓存
```

---

### 问题 4: 下载速度慢或无法下载

**解决方法:** 使用方法 2（GitHub 下载）或方法 3（winget）

---

## 📝 安装检查清单

完成以下检查，确保安装成功：

- [ ] 工具已成功安装到电脑
- [ ] 可以从开始菜单启动应用
- [ ] 主界面正常显示
- [ ] "Inspect" 按钮可以点击
- [ ] 没有错误弹窗

如果以上所有项都已完成，恭喜你！🎉 工具安装成功！

---

## 🎓 知识检测

在进入下一教程前，请确认你能回答以下问题：

1. **Accessibility Insights 的主要作用是什么？**
   <details>
   <summary>点击查看答案</summary>
   查看和检查 Windows 应用程序的 UI 元素结构和属性，帮助 RPA 开发者定位控件。
   </details>

2. **有哪三种安装方法？**
   <details>
   <summary>点击查看答案</summary>
   1. Microsoft Store 安装
   2. GitHub 下载 .msix 文件
   3. 使用 winget 命令行工具
   </details>

3. **最低系统要求是什么？**
   <details>
   <summary>点击查看答案</summary>
   Windows 10 1809 或更高版本，x64 架构。
   </details>

---

## 🚀 下一步

安装完成后，让我们继续学习[教程 2: 界面介绍](./02-ui-overview.md)，了解工具的各个界面组件！

---

**有问题？** 查看[教程 5: 常见问题与技巧](./05-tips-and-tricks.md)中的"安装问题"部分
