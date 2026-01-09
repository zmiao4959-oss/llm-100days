import logging

# 默认warning级别
# 使用logging.basicConfig()指定级别
logging.basicConfig(filename="demo.log", filemode="w", level=logging.DEBUG)  # a追加w写入

logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")
