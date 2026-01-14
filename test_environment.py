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
        print("\n请先安装依赖:")
        print("  pip install rpaframework==22.5.0")
        print("  pip install rpaframework-windows==5.1.0")
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

        config_path = Path("resources/config.yaml")
        if not config_path.exists():
            print("✗ 配置文件不存在")
            return False

        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)

        print("✓ 配置文件加载成功")
        print(f"  - 默认开始日期: {config['date_params']['default_start_date']}")
        print(f"  - 默认结束日期: {config['date_params']['default_end_date']}")
        print(f"  - 钉钉窗口标题: {config['dingtalk']['window_title']}")

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
        print("\n下一步:")
        print("  1. 确保钉钉客户端已安装并登录")
        print("  2. 运行手动测试: python test_manual.py")
        print("  3. 运行主任务: python tasks.py")
    else:
        print("\n✗ 部分测试失败，请检查上述错误信息。")

    return all_passed


if __name__ == "__main__":
    main()
