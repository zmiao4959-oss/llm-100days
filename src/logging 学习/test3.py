import logging

# 输出格式和添加一些公共信息
logging.basicConfig(
    format="%(asctime)s\n%(levelname)s\n%(filename)s:%(lineno)s\n%(message)s\n",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG,
)

logging.debug("debug message")
name = "李白"
age = 56
logging.debug("姓名 %s 年龄 %d", name, age)
logging.critical("姓名 %s 年龄 %d", name, age)
