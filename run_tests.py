import os
import sys

# 添加项目根目录到 sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    os.system("pytest --alluredir=reports/allure-results")
    os.system("allure generate reports/allure-results -o reports/allure-report --clean")
    os.system("allure open reports/allure-report")