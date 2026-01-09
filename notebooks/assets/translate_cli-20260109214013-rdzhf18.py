import os
import sys

# 获取当前脚本的目录
# print(os.path.abspath(__file__))
script_dir = os.path.dirname(os.path.abspath(__file__))
# print(script_dir)
# 获取项目根目录，即scripts的父目录
project_root = os.path.dirname(script_dir)
# print(project_root)
# 将项目根目录添加到sys.path，不然识别不到包的信息
sys.path.insert(0, project_root)
from src.llm_bootstrap import translate_google

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "item", help="put something here to translate to chinese", type=str
    )
    args = parser.parse_args()
    result = translate_google(args.item)
    print(result)
