
import logging
import logging.config
import os

from config import setting

# Auto Close Office Logger


class ACOLogger:

    def __init__(self, config=setting.logConfig):

        self.initFolder(config)
        logging.config.dictConfig(config)
        self.logger = logging.getLogger("appuser")

    # 切换日志记录器
    def setLogger(self, name=None):
        self.logger = logging.getLogger(name)

    # 完成推流
    def flush(self):
        for idx in range(len(self.logger.handlers)):
            try:
                self.logger.handlers[idx].flush()
            except:
                self.logger.error("flush->fail to flush handlers[%d]", idx)

    # 日志文件初始化
    def initFolder(self, config):

        FILE_NAME = "filename"
        CURRENT_PATH = os.getcwd()

        handlers = config["handlers"]
        for key in handlers:
            handler = handlers[key]
            if FILE_NAME in handler:
                filepath = os.path.dirname(os.path.join(
                    CURRENT_PATH, handler[FILE_NAME]))
                if False == os.path.isdir(filepath):
                    os.makedirs(filepath)
                    print("create foloder[", filepath, "]")
