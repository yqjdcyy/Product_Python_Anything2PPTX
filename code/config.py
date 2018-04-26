from enum import Enum
import logging
import logging.config

# 请求类型


class ReqType(Enum):
    CONFIG = 0
    PDF2PPTX = 1
    IMAGES2PPTX = 2
    PDF2IMAGES = 3


# 请求参数配置
class Config:

    def __init__(self, type=ReqType.PDF2PPTX, src="", dest="", dpi=96, ext="jpeg", open=True):
        self.type = type
        self.src = src
        self.dest = dest
        self.dpi = dpi
        self.ext = ext
        self.open = open

    def __str__(self):
        return "{{\"type\": {},\"src\": {},\"dest\": {},\"dpi\": {},\"extension\": {},\"open\": {}}}".format(self.type, self.src,  self.dest,  self.dpi, self.ext, self.open)


# 全局参数
config = Config()
