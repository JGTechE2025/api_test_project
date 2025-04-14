import pytest


def run_tests(test_path):
    # 直接在程式內執行 pytest 測試
    pytest.main([test_path])


if __name__ == "__main__":
    # run_tests("tests/test_user.py")  # 執行特定測試檔案
    run_tests("tests")  # 執行所有測試
