# 钉钉 Windows 客户端 RPA 自动化

基于 Robocorp RPA 框架的钉钉客户端自动化项目，实现日期参数查询和 Excel 导出功能。

## 功能说明

- ✅ 自动启动/激活钉钉 Windows 客户端
- ✅ 自动填写开始和结束日期参数
- ✅ 点击查询按钮获取数据
- ✅ 导出查询结果为 Excel 文件

## 项目结构

```
RPA_Robocorp_TEST_20260114/
├── tasks.py              # RPA 任务主脚本
├── robot.yaml            # Robocorch 配置文件
├── conda.yaml            # Python 依赖环境配置
├── resources/
│   └── config.yaml       # 项目配置文件
├── output/               # 导出文件的目录
└── README.md             # 项目说明
```

## 环境要求

- Windows 11 操作系统
- Python 3.9+
- 钉钉 Windows 客户端（已安装）
- Robocorp RPA Framework

## 安装步骤

### 1. 安装 Robocorp CLI

```bash
pip install rpaframework
```

### 2. 创建并激活 Python 虚拟环境

```bash
# 使用 conda
conda env create -f conda.yaml
conda activate rpa-env

# 或使用 venv
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt  # 如果创建 requirements.txt
```

### 3. 安装依赖

```bash
pip install rpaframework==22.5.0
pip install rpaframework-windows==5.1.0
```

## 使用方法

### 方式 1: 直接运行 Python 脚本

```bash
python tasks.py
```

### 方式 2: 使用 Robocorch CLI

```bash
# 运行默认任务
robocorp run query_and_export

# 带参数运行（需要修改代码支持命令行参数）
robocorp run query_and_export --param start_date=2024-01-01 --param end_date=2024-01-31
```

### 方式 3: 在 Python 中调用

```python
from tasks import query_and_export

# 执行查询和导出
result = query_and_export(
    start_date="2024-01-01",
    end_date="2024-01-31",
    filename="my_export.xlsx"
)
```

## 配置说明

编辑 `resources/config.yaml` 文件来自定义配置：

```yaml
date_params:
  default_start_date: "2024-01-01"
  default_end_date: "2024-01-31"

dingtalk:
  window_title: "DingTalk"
  controls:
    start_date_field: "开始日期"
    end_date_field: "结束日期"
    query_button: "查询"
    save_button: "保存"
```

## 重要提示

### 🔍 获取控件选择器

由于不同版本的钉钉界面可能不同，需要获取准确的控件选择器：

1. **下载 UI 检查工具**:
   - Windows SDK 中的 `inspect.exe`
   - 或使用 `Accessibility Insights for Windows`

2. **获取控件信息**:
   - 打开钉钉和 UI 检查工具
   - 将鼠标悬停在目标控件上（日期输入框、按钮等）
   - 记录控件的 `Name`、`AutomationId`、`ClassName` 等属性

3. **更新代码中的选择器**:
   ```python
   # 修改 tasks.py 中的控件选择器
   self.windows.set_focus("实际的控件名称")
   ```

### 调试技巧

1. **打印日志**: 代码中已添加 print 语句，方便调试
2. **手动测试**: 先手动执行一遍流程，记录每个步骤
3. **截图验证**: 可以在每个步骤后添加截图功能
4. **延迟调整**: 根据实际网络和系统响应速度调整等待时间

## 常见问题

### Q: 找不到钉钉窗口？

**A**: 检查 `config.yaml` 中的 `window_title` 是否与实际窗口标题匹配。

### Q: 无法输入日期？

**A**: 确保使用正确的控件选择器，可能需要先点击输入框激活焦点。

### Q: 查询按钮点击无效？

**A**: 尝试以下方法：
- 使用控件名称点击
- 使用快捷键（如 Tab 键切换 + Enter）
- 使用图像识别定位按钮

### Q: 导出的 Excel 文件不在 output 目录？

**A**: 钉钉可能将文件保存到浏览器默认下载目录，需要：
1. 检查 `C:\Users\{你的用户名}\Downloads`
2. 在代码中添加文件移动逻辑

## 下一步优化

- [ ] 添加命令行参数支持
- [ ] 添加日志记录功能
- [ ] 添加错误重试机制
- [ ] 添加定时任务调度
- [ ] 支持批量日期范围查询
- [ ] 添加数据验证和清洗
- [ ] 生成查询报告

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！
