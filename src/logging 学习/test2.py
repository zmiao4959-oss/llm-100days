import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("debug message")
name = "李白"
age = 56
logging.debug("姓名 %s 年龄 %d", name, age)  # debug的三个参数输入，因此与print结果不同
print("姓名 %s 年龄 %d", name, age)
logging.debug("姓名 %s 年龄 %d" % (name, age))
print("姓名 %s 年龄 %d" % (name, age))
