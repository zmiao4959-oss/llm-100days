import logging

# 编程方式写高级用法
# 记录器
logger = logging.getLogger("applog")
# logger.setLevel(logging.DEBUG)
# print(logger)
# print(type(logger))

# 处理器handler    level先经过lpgger筛选，再经过handler筛选，因此取二者的交集
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

# 不指定级别，默认logger级别
fileHandler = logging.FileHandler("applog.log")

# formatter格式 8占8位置，-左对齐
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)-8s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# 给处理器设置格式
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

# 给记录器设置处理器
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

# 定义一个过滤器，只选择特定格式文件
flt = logging.FileHandler("applog.")

# 关联过滤器
logger.addFilter(flt)
# fileHandler.addFilter(flt)

# 打印日志代码
logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")
