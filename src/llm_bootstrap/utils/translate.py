import logging
import logging.config
import os

import requests

project_root = os.path.dirname(os.path.abspath(__file__))
file_conf = os.path.join(project_root, "logging.conf")
# 绝对路径杜绝一切麻烦，但是log文件也分开了
logging.config.fileConfig(file_conf)
logger = logging.getLogger("translate_log")


def translate_google(text, src="auto", dest="zh-CN"):
    url = "https://translate.googleapis.com/translate_a/single"
    params = {"client": "gtx", "sl": src, "tl": dest, "dt": "t", "q": text}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        # print(response.text)
        result = response.json()
        logger.debug("successfully translated text")
        return "".join([item[0] for item in result[0]])
    else:
        logger.error("failed to translate")
        return None


if __name__ == "__main__":
    print(translate_google("aurora is splendid"))
