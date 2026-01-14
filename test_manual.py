"""
手动测试脚本 - 逐步验证每个功能

这个脚本会引导你逐步测试钉钉的各个功能，
帮助你找到正确的控件选择器。
"""

from RPA import Windows
from datetime import datetime
import time


class ManualTester:
    """手动测试类"""

    def __init__(self):
        self.windows = Windows()

    def test_window_activation(self):
        """测试窗口激活"""
        print("\n" + "=" * 60)
        print("测试 1: 激活钉钉窗口")
        print("=" * 60)

        print("\n准备工作:")
        print("  1. 确保钉钉客户端已打开")
        print("  2. 确保已登录")
        print("  3. 导航到你要操作的页面（如考勤、审批等）")

        input("\n按 Enter 键继续...")

        # 尝试不同的窗口标题
        titles_to_try = [
            "钉钉",
            "DingTalk",
            "钉钉面板",
            "DingTalk Launcher"
        ]

        for title in titles_to_try:
            try:
                print(f"\n尝试使用标题激活: '{title}'")
                self.windows.set_focus(title)
                print(f"✓ 成功！使用标题: '{title}'")
                time.sleep(2)
                return title
            except Exception as e:
                print(f"✗ 失败: {e}")

        print("\n所有预设标题都失败了。")
        print("请手动查看钉钉窗口的完整标题，并更新 config.yaml")

        custom_title = input("\n请输入钉钉窗口的确切标题（留空跳过）: ").strip()
        if custom_title:
            try:
                self.windows.set_focus(custom_title)
                print(f"✓ 成功！使用自定义标题: '{custom_title}'")
                return custom_title
            except Exception as e:
                print(f"✗ 仍然失败: {e}")

        return None

    def test_date_input(self):
        """测试日期输入"""
        print("\n" + "=" * 60)
        print("测试 2: 日期输入测试")
        print("=" * 60)

        print("\n这个测试会尝试不同的方式输入日期:")
        print("  1. 直接发送按键")
        print("  2. Tab 键切换 + 按键")
        print("  3. 鼠标点击 + 按键")

        test_date = "2024-01-15"

        print(f"\n测试日期: {test_date}")

        # 方式 1: 直接发送按键
        print("\n[方式 1] 直接发送按键（假设焦点已在输入框）")
        print("请手动点击开始日期输入框，然后按 Enter...")
        input("按 Enter 继续...")

        try:
            self.windows.send_keys(test_date)
            print(f"✓ 已发送: {test_date}")
            time.sleep(1)
        except Exception as e:
            print(f"✗ 失败: {e}")

        # 方式 2: Tab 键
        print("\n[方式 2] 使用 Tab 键切换焦点")
        input("请确保焦点在日期输入框前的某个位置，然后按 Enter...")

        try:
            # 尝试多次 Tab
            tabs = int(input("需要按几次 Tab 才能到达开始日期？(输入数字，通常 1-5): "))
            for i in range(tabs):
                self.windows.send_keys("{TAB}")
                time.sleep(0.3)

            self.windows.send_keys(test_date)
            print(f"✓ 已输入: {test_date}")
            time.sleep(1)
        except Exception as e:
            print(f"✗ 失败: {e}")

        # 方式 3: 清除并重新输入
        print("\n[方式 3] 清除现有内容 + 输入新内容")
        input("如果输入框有内容，将光标放在输入框中，按 Enter...")

        try:
            # 全选 (Ctrl+A)
            self.windows.send_keys("^a")
            time.sleep(0.3)
            # 删除
            self.windows.send_keys("{DELETE}")
            time.sleep(0.3)
            # 输入新内容
            self.windows.send_keys(test_date)
            print(f"✓ 已输入: {test_date}")
            time.sleep(1)
        except Exception as e:
            print(f"✗ 失败: {e}")

        print("\n记录你的发现:")
        print("  - 哪种方式有效？")
        print("  - 需要按几次 Tab 键？")

    def test_query_button(self):
        """测试查询按钮点击"""
        print("\n" + "=" * 60)
        print("测试 3: 查询按钮测试")
        print("=" * 60)

        print("\n这个测试会尝试不同的方式触发查询:")
        print("  1. 按 Enter 键")
        print("  2. Tab 键切换到按钮 + Enter")
        print("  3. 快捷键（如 Ctrl+Enter）")

        # 方式 1: Enter
        print("\n[方式 1] 直接按 Enter 键")
        input("确保日期已输入，按 Enter 测试...")

        try:
            self.windows.send_keys("{ENTER}")
            print("✓ 已按 Enter 键")
            print("请检查钉钉是否触发了查询...")
            time.sleep(3)
        except Exception as e:
            print(f"✗ 失败: {e}")

        # 方式 2: Tab + Enter
        print("\n[方式 2] Tab 键切换到按钮 + Enter")
        tabs = int(input("需要按几次 Tab 才能到达查询按钮？(通常 1-3): "))

        try:
            for i in range(tabs):
                self.windows.send_keys("{TAB}")
                time.sleep(0.3)

            self.windows.send_keys("{ENTER}")
            print("✓ 已点击按钮")
            print("请检查钉钉是否触发了查询...")
            time.sleep(3)
        except Exception as e:
            print(f"✗ 失败: {e}")

        # 方式 3: 快捷键
        print("\n[方式 3] 尝试快捷键")
        print("常见快捷键:")
        print("  - Ctrl+Enter")
        print("  - Alt+Q")
        print("  - F5")

        choice = input("是否尝试自定义快捷键？(输入快捷键组合，如 'ctrl+enter'，留空跳过): ").strip()

        if choice:
            try:
                # 解析快捷键
                keys = choice.lower()
                if "ctrl" in keys and "enter" in keys:
                    self.windows.send_keys("^{{ENTER}}")
                elif "alt" in keys and "q" in keys:
                    self.windows.send_keys("%q")
                elif keys == "f5":
                    self.windows.send_keys("{F5}")
                else:
                    print(f"未识别的快捷键: {choice}")
                    return

                print(f"✓ 已按下: {choice}")
                print("请检查钉钉是否触发了查询...")
                time.sleep(3)
            except Exception as e:
                print(f"✗ 失败: {e}")

    def test_export_function(self):
        """测试导出功能"""
        print("\n" + "=" * 60)
        print("测试 4: 导出功能测试")
        print("=" * 60)

        print("\n导出方式可能包括:")
        print("  1. 点击'保存'按钮")
        print("  2. 点击'导出'按钮")
        print("  3. 快捷键（如 Ctrl+S）")
        print("  4. 右键菜单")

        print("\n请先在钉钉中完成一次查询，然后:")
        input("按 Enter 测试导出...")

        # 方式 1: 快捷键 Ctrl+S
        print("\n[方式 1] 尝试 Ctrl+S")
        try:
            self.windows.send_keys("^s")
            print("✓ 已按 Ctrl+S")
            print("如果弹出保存对话框，请记录保存路径...")

            time.sleep(2)
            print("\n可能需要以下操作:")
            print("  1. 选择保存位置")
            print("  2. 确认文件名")
            print("  3. 按 Enter 确认保存")

            input("\n按 Enter 继续...")
        except Exception as e:
            print(f"✗ 失败: {e}")

        # 方式 2: Tab 到导出按钮
        print("\n[方式 2] Tab 键切换到导出/保存按钮")
        tabs = int(input("需要按几次 Tab 才能到达导出按钮？(通常 5-10): "))

        try:
            for i in range(tabs):
                self.windows.send_keys("{TAB}")
                time.sleep(0.3)

            self.windows.send_keys("{ENTER}")
            print("✓ 已点击按钮")
            time.sleep(2)
        except Exception as e:
            print(f"✗ 失败: {e}")

    def generate_report(self):
        """生成测试报告"""
        print("\n" + "=" * 60)
        print("测试总结报告")
        print("=" * 60)

        print("\n请根据你的测试结果，更新以下配置:")
        print("\n1. 窗口标题:")
        print("   config.yaml -> dingtalk.window_title")

        print("\n2. 日期输入方式:")
        print("   - 需要几次 Tab 键？")
        print("   - 是否需要先清除内容？")

        print("\n3. 查询触发方式:")
        print("   - Enter 键有效吗？")
        print("   - 需要按几次 Tab？")

        print("\n4. 导出方式:")
        print("   - Ctrl+S 有效吗？")
        print("   - 还是点击特定按钮？")
        print("   - 默认保存路径是什么？")

        print("\n5. 建议的配置:")
        print("""
# resources/config.yaml

dingtalk:
  window_title: "实际窗口标题"

  controls:
    # 如果使用 Tab 键
    tabs_to_start_date: 2
    tabs_to_end_date: 1
    tabs_to_query_button: 3

    # 如果使用控件名称
    start_date_field: "控件名称"
    end_date_field: "控件名称"
    query_button: "查询"

export:
  default_path: "C:\\\\Users\\\\YOUR_USERNAME\\\\Downloads"
        """)

    def run_all_tests(self):
        """运行所有测试"""
        print("=" * 60)
        print("钉钉 RPA 手动测试工具")
        print("=" * 60)
        print("\n这个工具会帮助你:")
        print("  1. 找到正确的窗口标题")
        print("  2. 测试日期输入方式")
        print("  3. 测试查询触发方式")
        print("  4. 测试导出功能")
        print("  5. 生成配置建议")

        input("\n按 Enter 开始测试...")

        # 依次运行测试
        # self.test_window_activation()
        # self.test_date_input()
        # self.test_query_button()
        # self.test_export_function()
        # self.generate_report()

        # 让用户选择测试项目
        while True:
            print("\n" + "=" * 60)
            print("选择测试项目:")
            print("  1. 窗口激活测试")
            print("  2. 日期输入测试")
            print("  3. 查询按钮测试")
            print("  4. 导出功能测试")
            print("  5. 生成测试报告")
            print("  0. 退出")

            choice = input("\n请选择 (0-5): ").strip()

            if choice == "1":
                self.test_window_activation()
            elif choice == "2":
                self.test_date_input()
            elif choice == "3":
                self.test_query_button()
            elif choice == "4":
                self.test_export_function()
            elif choice == "5":
                self.generate_report()
            elif choice == "0":
                print("\n测试结束。")
                break
            else:
                print("无效选择，请重试。")


def main():
    """主函数"""
    tester = ManualTester()
    tester.run_all_tests()


if __name__ == "__main__":
    main()
