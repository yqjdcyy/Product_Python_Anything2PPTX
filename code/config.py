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

# 服务配置


class Setting:
    def __init__(self):
        # Java.Launcher
        self.jar = "../bin/java/PDFBox.jar"
        # CSharp.Launcher
        self.exe = "../bin/csharp/AnythingToPPTX.exe"
        # Template
        self.template = "../bin/csharp/Template/template.pptx"
        # 日志配置
        self.logConfig = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'standard': {
                    'format': '%(asctime)s %(levelname)10s %(message)s'
                },
            },
            'handlers': {
                'default': {
                    'level': logging.INFO,
                    'formatter': 'standard',
                    'class': 'logging.StreamHandler',
                },
                'stdFile': {
                    'level': logging.DEBUG,
                    'formatter': 'standard',
                    'class': 'logging.FileHandler',
                    'filename': '../log/anythind-to-pptx.log'
                },
            },
            'loggers': {
                '': {
                    'handlers': ['default'],
                    'level': logging.INFO,
                    'propagate': False
                },
                'appuser': {
                    'handlers': ['stdFile'],
                    'level': logging.DEBUG,
                    'propagate': True
                },
            }
        }


# 全局参数
config = Config()
setting = Setting()
