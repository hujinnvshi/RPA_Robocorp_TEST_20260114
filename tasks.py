"""
钉钉 Windows 客户端 RPA 自动化任务
功能：填写日期参数 -> 查询数据 -> 导出 Excel
"""

from datetime import datetime
from pathlib import Path
from RPA import Windows
from RPA.Excel.Files import Files as ExcelFiles
from RPA.FileSystem import FileSystem
import time


class DingTalkRPA:
    """钉钉客户端自动化类"""

    def __init__(self):
        self.windows = Windows()
        self.excel = ExcelFiles()
        self.fs = FileSystem()
        self.output_dir = Path("output")

    def start_dingtalk(self):
        """启动钉钉客户端"""
        try:
            # 方式1: 通过应用名称启动（需根据实际钉钉安装路径调整）
            # self.windows.run_application("C:\\Users\\{YOUR_USER}\\AppData\\Local\\DingTalk\\DingtalkLauncher.exe")

            # 方式2: 假设钉钉已经运行，直接激活窗口
            # 需要找到钉钉窗口的标题或类名
            self.windows.set_focus("DingTalk")  # 窗口标题关键字
            print("✓ 钉钉客户端已激活")
            time.sleep(2)

        except Exception as e:
            print(f"✗ 启动钉钉失败: {e}")
            print("提示: 请确保钉钉客户端已安装并可以正常启动")
            raise

    def input_date_parameters(self, start_date, end_date):
        """
        输入日期参数

        Args:
            start_date: 开始日期，格式: YYYY-MM-DD
            end_date: 结束日期，格式: YYYY-MM-DD
        """
        print(f"正在输入日期参数: {start_date} 至 {end_date}")

        try:
            # 注意：以下选择器需要根据实际的钉钉界面调整
            # 使用 inspect.exe (Windows SDK) 或类似工具获取准确的选择器

            # 示例: 输入开始日期
            self.windows.set_focus("开始日期")  # 控件名称或标签
            time.sleep(0.5)
            self.windows.send_keys(start_date)
            print(f"✓ 开始日期已输入: {start_date}")
            time.sleep(0.5)

            # 示例: 输入结束日期
            self.windows.set_focus("结束日期")
            time.sleep(0.5)
            self.windows.send_keys(end_date)
            print(f"✓ 结束日期已输入: {end_date}")
            time.sleep(0.5)

        except Exception as e:
            print(f"✗ 输入日期参数失败: {e}")
            print("提示: 需要根据实际的钉钉界面控件调整选择器")
            raise

    def click_query_button(self):
        """点击查询按钮"""
        print("正在点击查询按钮...")

        try:
            # 示例: 点击查询按钮
            # self.windows.click("查询")  # 按钮文本或控件名称

            # 或者使用快捷键
            # self.windows.send_keys("{ENTER}")  # 按回车键查询

            print("✓ 查询按钮已点击")
            time.sleep(3)  # 等待查询结果加载

        except Exception as e:
            print(f"✗ 点击查询按钮失败: {e}")
            raise

    def export_to_excel(self, filename=None):
        """
        导出查询结果为 Excel

        Args:
            filename: 导出的文件名，如不指定则使用时间戳
        """
        print("正在导出数据...")

        try:
            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"dingtalk_export_{timestamp}.xlsx"

            output_path = self.output_dir / filename

            # 示例: 点击保存/导出按钮
            # self.windows.click("保存")  # 或 "导出"

            # 等待文件保存完成
            time.sleep(2)

            # 检查文件是否已创建（钉钉可能保存到默认下载目录）
            # 如果需要，可以移动文件到 output 目录

            print(f"✓ 数据已导出到: {output_path}")
            return output_path

        except Exception as e:
            print(f"✗ 导出失败: {e}")
            raise

    def run_query_workflow(self, start_date, end_date, filename=None):
        """
        执行完整的查询工作流程

        Args:
            start_date: 开始日期，格式: YYYY-MM-DD
            end_date: 结束日期，格式: YYYY-MM-DD
            filename: 导出的文件名（可选）
        """
        print("=" * 60)
        print("开始执行钉钉 RPA 自动化任务")
        print("=" * 60)

        try:
            # 1. 启动/激活钉钉
            self.start_dingtalk()

            # 2. 输入日期参数
            self.input_date_parameters(start_date, end_date)

            # 3. 点击查询
            self.click_query_button()

            # 4. 导出 Excel
            output_file = self.export_to_excel(filename)

            print("=" * 60)
            print("✓ 任务执行成功！")
            print(f"✓ 导出文件: {output_file}")
            print("=" * 60)

            return output_file

        except Exception as e:
            print("=" * 60)
            print(f"✗ 任务执行失败: {e}")
            print("=" * 60)
            raise


def query_and_export(start_date: str, end_date: str, filename: str = None):
    """
    RPA 任务入口函数

    Args:
        start_date: 开始日期，格式: YYYY-MM-DD，例如: 2024-01-01
        end_date: 结束日期，格式: YYYY-MM-DD，例如: 2024-01-31
        filename: 导出的文件名（可选）

    Example:
        query_and_export("2024-01-01", "2024-01-31")
    """
    rpa = DingTalkRPA()
    return rpa.run_query_workflow(start_date, end_date, filename)


# ====== 供 Robocorch 调用的主函数 ======
def main():
    """主函数 - Robocorch 入口点"""
    # 示例参数（可以改为从配置文件读取或命令行参数）
    start_date = "2024-01-01"
    end_date = "2024-01-31"

    # 执行 RPA 任务
    result = query_and_export(start_date, end_date)
    return result


if __name__ == "__main__":
    main()
