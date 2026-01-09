import logging
import logging.config

# 配置文件
logging.config.fileConfig("logging.conf")
logger_root = logging.getLogger("root")
logger_root.debug("debug message for root logger")
logger = logging.getLogger("applog")
logger.debug("debug message for app logger")

x = "hello world"
try:
    int(x)
except Exception as e:
    # logger.error(e)
    logger.exception(e)
