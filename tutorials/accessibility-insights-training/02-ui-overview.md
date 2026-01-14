# 教程 2: 界面介绍

## 📋 本教程目标

完成本教程后，你将：
- 熟悉 Accessibility Insights 的主界面布局
- 理解各个功能区域的作用
- 掌握基本术语和概念
- 学会使用快捷键提高效率

---

## 🎨 主界面布局

启动 Accessibility Insights 后，你会看到以下界面：

```
┌─────────────────────────────────────────────────────────────────┐
│  Accessibility Insights for Windows                    [_][□][X]│
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  模式选择区域                                             │    │
│  │  [Inspect]  [Test]  [Issues]  [Events]                   │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌──────────────────────┐  ┌─────────────────────────────────┐ │
│  │                      │  │                                 │ │
│  │   元素树区域          │  │   属性面板区域                  │ │
│  │   (Element Tree)     │  │   (Properties Panel)           │ │
│  │                      │  │                                 │ │
│  │  ┌─────────────┐    │  │  Name: ...                      │ │
│  │  │ 窗口        │    │  │  AutomationId: ...              │ │
│  │  │ ├─ 按钮     │    │  │  ClassName: ...                 │ │
│  │  │ └─ 输入框   │    │  │  ControlType: ...               │ │
│  │  │             │    │  │                                 │ │
│  │  └─────────────┘    │  │                                 │ │
│  │                      │  │                                 │ │
│  └──────────────────────┘  └─────────────────────────────────┘ │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  快速选择按钮: [Target] [Refresh] [Toggle Highlight]    │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📦 界面区域详解

### 1️⃣ 模式选择区域

这是工具的核心功能区，提供 4 种主要模式：

#### **Inspect（检查模式）** ⭐ RPA 最常用
```
作用: 实时查看应用程序的 UI 元素
使用场景:
  - 查找按钮、输入框等控件
  - 获取控件的属性信息
  - 理解 UI 元素的层级结构

快捷键: Ctrl + I
```

#### **Test（测试模式）**
```
作用: 运行可访问性自动化测试
使用场景:
  - 检查应用是否符合可访问性标准
  - 发现潜在的 UI 问题

注: RPA 开发较少使用
```

#### **Issues（问题模式）**
```
作用: 查看已发现的可访问性问题
使用场景:
  - 审查应用的 UI 问题
  - 生成可访问性报告

注: RPA 开发较少使用
```

#### **Events（事件模式）**
```
作用: 监控 UI 元素的事件
使用场景:
  - 调试复杂交互
  - 了解元素事件触发时机

注: 高级功能，初级阶段不需要
```

---

### 2️⃣ 元素树区域 (Element Tree)

这是左侧的树形结构视图，显示所有 UI 元素的层级关系。

#### 树形结构示例
```
📁 DingTalk (钉钉主窗口)
  ├─ 📁 TitleBar (标题栏)
  │   ├─ 🔴 Button (最小化)
  │   ├─ 🔴 Button (最大化)
  │   └─ 🔴 Button (关闭)
  ├─ 📁 MenuBar (菜单栏)
  │   └─ 🔴 MenuItem (设置)
  ├─ 📁 SearchPanel (搜索面板)
  │   └─ ⚪ Edit (搜索框)         ← 这是我们想要的
  └─ 📁 ChatList (聊天列表)
      └─ 🔴 ListItem (张三)
```

#### 图标说明
| 图标 | 含义 | 示例 |
|------|------|------|
| 📁 | 容器类元素 | Window, Pane, Group |
| 🔴 | 可交互元素 | Button, CheckBox |
| ⚪ | 输入/显示元素 | Edit, Text, Document |
| 🔷 | 特殊控件 | List, Table, Menu |

#### 操作方式
```
展开节点: 点击 ▶ 或双击元素名
折叠节点: 点击 ▼ 或双击元素名
选择元素: 单击元素
查看属性: 选中元素后看右侧面板
```

---

### 3️⃣ 属性面板区域 (Properties Panel)

右侧面板显示当前选中元素的详细属性。

#### 核心属性（RPA 必知）

##### **1. Name（名称）**
```
定义: 控件的显示名称，用户看到的文字
示例: "发送"、"搜索"、"张三"
重要性: ⭐⭐⭐⭐⭐ (最常用的定位方式)
稳定性: 中等（可能因语言设置变化）

RPA 使用示例:
library.click('name:"发送"')
```

##### **2. AutomationId（自动化ID）**
```
定义: 开发者设置的自动化唯一标识符
示例: "send_btn", "search_input", "chat_item_1"
重要性: ⭐⭐⭐⭐⭐ (最稳定的定位方式)
稳定性: 高（除非代码重构）

RPA 使用示例:
library.click('automationid:"send_btn"')
```

##### **3. ClassName（类名）**
```
定义: .NET 控件类名
示例: "Button", "Edit", "TextBox", "ListBox"
重要性: ⭐⭐⭐ (辅助定位)
稳定性: 高

RPA 使用示例:
library.click('classname:"Button"')
```

##### **4. ControlType（控件类型）**
```
定义: UI Automation 标准控件类型
示例: "Button", "Edit", "Text", "Window"
重要性: ⭐⭐⭐⭐ (常用作过滤条件)
稳定性: 高

RPA 使用示例:
library.click('controltype:"Button" AND name:"发送"')
```

##### **5. FrameworkId（框架类型）**
```
定义: 应用使用的 UI 框架
常见值:
  - "Win32"  → 传统 Windows 应用
  - "WinForm" → .NET Windows Forms
  - "WPF"    → Windows Presentation Foundation
  - "WinRT"  → UWP 应用

重要性: ⭐⭐ (了解即可，不常用于定位)
```

#### 其他有用属性

| 属性 | 说明 | RPA 用途 |
|------|------|---------|
| **IsEnabled** | 是否可用 | 判断按钮是否可点击 |
| **IsOffscreen** | 是否在屏幕外 | 过滤不可见元素 |
| **BoundingRectangle** | 屏幕坐标 | 用于截图验证 |
| **HelpText** | 帮助文本 | 辅助理解控件用途 |
| **LocalizedControlType** | 本地化类型 | 与 ControlType 相同 |

---

### 4️⃣ 快速操作按钮区域

底部的快捷按钮，提高操作效率：

#### **Target（目标选择）** 🎯
```
图标: 靶心图标
作用: 点击后在应用中直接选择元素
使用方法:
  1. 点击 Target 按钮
  2. 鼠标变成十字准星
  3. 在目标应用中点击元素
  4. 自动跳转到对应元素树节点

快捷键: Ctrl + Shift + T
```

#### **Refresh（刷新）** 🔄
```
图标: 刷新图标
作用: 重新加载元素树（当界面更新时）
使用场景:
  - 应用界面发生变化
  - 动态加载的内容
  - 找不到元素时

快捷键: F5
```

#### **Toggle Highlight（切换高亮）** 💡
```
图标: 灯泡/高亮图标
作用: 高亮显示当前选中的元素
使用场景:
  - 确认选中了正确的元素
  - 查看元素在屏幕上的位置

快捷键: Ctrl + H
```

---

## ⌨️ 常用快捷键

掌握快捷键可以大幅提高效率：

| 快捷键 | 功能 | 说明 |
|--------|------|------|
| `F5` | 刷新元素树 | 界面更新后使用 |
| `Ctrl + I` | 切换 Inspect 模式 | 快速进入检查模式 |
| `Ctrl + T` | 快速选择元素 | 启动 Target 模式 |
| `Ctrl + H` | 切换高亮 | 高亮当前元素 |
| `Ctrl + F` | 搜索元素 | 在元素树中搜索 |
| `Ctrl + C` | 复制元素信息 | 复制选中元素的属性 |
| `ESC` | 取消当前操作 | 退出 Target 模式 |

---

## 🎯 重要概念

### 概念 1: 元素层级（Element Hierarchy）

UI 元素是树形结构，类似文件系统：

```
文件系统类比:
C:\Users\Documents\RPA\file.txt

UI 元素树类比:
Window → Pane → Group → Button
         ↑      ↑       ↑      ↑
       根节点  容器   容器   目标元素
```

**RPA 影响:**
```python
# 方式 1: 直接定位（简单但可能不精确）
library.click('name:"发送"')

# 方式 2: 通过层级定位（更精确）
window = library.windows_window('钉钉')
chat_panel = window.find_element('name:"聊天面板"')
send_button = chat_panel.find_element('name:"发送"')
send_button.click()
```

---

### 概念 2: 元素焦点（Focus）

元素树中当前被选中的元素称为"有焦点"的元素。

```
属性面板显示的信息 = 当前有焦点元素的信息

改变焦点:
  - 点击元素树中的节点
  - 使用 Target 功能选择元素
  - 使用快捷键 Ctrl + T
```

---

### 概念 3: 可见性（Visibility）

不是所有元素都在屏幕上可见：

| 属性 | 说明 | RPA 策略 |
|------|------|---------|
| **IsOffscreen = false** | 元素可见 | 可以直接操作 |
| **IsOffscreen = true** | 元素在屏幕外 | 需要滚动或调整窗口 |
| **IsEnabled = false** | 元素禁用 | 不能操作（灰色按钮） |

```python
# RPA 代码中检查可见性
if element.is_offscreen:
    # 需要滚动到元素位置
    library.scroll_to_element(element)
```

---

## 📚 实践练习

### 练习 1: 熟悉界面

**目标:** 打开工具并找到所有界面元素

**步骤:**
```
1. 启动 Accessibility Insights
2. 点击 "Inspect" 按钮
3. 打开 Windows 记事本 (Notepad)
4. 在工具中选择记事本窗口
5. 尝试以下操作:
   □ 展开/折叠元素树节点
   □ 点击不同元素查看属性变化
   □ 使用 Target 按钮选择记事本的输入框
   □ 按 F5 刷新元素树
   □ 使用 Ctrl + F 搜索 "Edit"
```

**预期结果:**
- ✅ 能看到记事本的元素树
- ✅ 能找到标题栏、菜单栏、输入框等元素
- ✅ 属性面板显示选中元素的信息

---

### 练习 2: 识别属性

**目标:** 理解各个属性的含义

**步骤:**
```
1. 选择记事本的输入框元素
2. 记录以下属性:
   □ Name: _________________
   □ AutomationId: _________________
   □ ClassName: _________________
   □ ControlType: _________________

3. 选择记事本的菜单 "文件" (File)
4. 记录属性:
   □ Name: _________________
   □ ControlType: _________________

5. 对比两个元素的属性差异
```

**思考问题:**
- 哪些属性是相同的？为什么？
- 哪些属性能唯一标识一个元素？
- 哪个属性最适合用于 RPA 定位？

---

### 练习 3: 使用快捷键

**目标:** 提高操作效率

**任务:**
```
□ 用 F5 刷新元素树 3 次
□ 用 Ctrl + T 启动 Target 模式
□ 用 Ctrl + H 切换高亮显示
□ 用 Ctrl + F 搜索 "Button"
□ 用 ESC 取消 Target 模式
```

---

## 🎓 知识检测

在进入下一教程前，请确认你能回答以下问题：

1. **RPA 开发最常用哪个模式？**
   <details>
   <summary>点击查看答案</summary>
   Inspect（检查模式）
   </details>

2. **最稳定的元素定位属性是？**
   <details>
   <summary>点击查看答案</summary>
   AutomationId（自动化ID）
   </details>

3. **如何刷新元素树？**
   <details>
   <summary>点击查看答案</summary>
   按 F5 或点击 Refresh 按钮
   </details>

4. **ControlType 和 ClassName 有什么区别？**
   <details>
   <summary>点击查看答案</summary>
   ControlType 是 UI Automation 标准类型（如 Button），ClassName 是具体的 .NET 类名（如 System.Windows.Forms.Button）
   </details>

---

## 📝 学习笔记

```
在本教程中，我学到了:

1. Accessibility Insights 有 4 个模式:
   - Inspect (检查) ← RPA 最重要
   - Test (测试)
   - Issues (问题)
   - Events (事件)

2. RPA 核心属性:
   - Name: 显示名称
   - AutomationId: 最稳定的标识
   - ClassName: .NET 类名
   - ControlType: 标准控件类型

3. 常用快捷键:
   - F5: 刷新
   - Ctrl + T: 快速选择
   - Ctrl + H: 切换高亮

4. 重要概念:
   - 元素树层级结构
   - 元素焦点
   - 元素可见性
```

---

## 🚀 下一步

现在你已经熟悉了界面，让我们继续学习[教程 3: 基础操作练习](./03-basic-operations.md)，开始实际操作吧！

---

**💡 小贴士:** 在继续学习前，建议多次打开工具，熟悉界面和快捷键，形成肌肉记忆！
