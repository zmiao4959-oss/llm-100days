# failure_modes

先定义`logging.conf`文件

然后在`translate.py`里面使用logging进行监控调试

if response.status_code == 200:
        #print(response.text)
        result = response.json()
        logger.debug("successfully translated text")
        return ''.join([item[0] for item in result[0]])
    else:
        logger.error("failed to translate")
        return None
