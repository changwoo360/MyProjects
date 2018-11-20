import sys
import io
from scheduler import Scheduler


def main():
	# 入口文件，运行调度器
    try:
        # 改变标准输出的默认编码
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
        Scheduler().run()
    except Exception as result:
        print("The <main> program got an exception：\"{}\"".format(result))
        
