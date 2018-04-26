import getopt
import sys

from config import config as conf
from config import ReqType


def main():

    # opts
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "ht:s:d:p:e:o",
            ["help", "type=", "src=", "dest=", "dpi=", "ext=", "open"])
    except getopt.GetoptError as err:
        print(str(err))
        help()
        sys.exit(2)

    # analyze
    for key, val in opts:
        if key in ('-h', "--help"):
            help()
            sys.exit()
        elif key in ('-t', "--type"):
            conf.type = ReqType(int(val))
        elif key in ('-s', "--src"):
            conf.src = val
        elif key in ('-d', "--dest"):
            conf.dest = val
        elif key in ('-p', "--dpi"):
            conf.dpi = val
        elif key in ('-e', "--ext"):
            conf.ext = val
        elif key in ('-o', "--open"):
            conf.open = True
        else:
            help()

    # switch
    if conf.type is ReqType.PDF2PPTX:
        print("PDF2PPTX")
    elif conf.type is ReqType.PDF2IMAGES:
        print("PDF2IMAGES")
    elif conf.type is ReqType.IMAGES2PPTX:
        print("IMAGES2PPTX")
    elif conf.type is ReqType.CONFIG:
        print(conf)

# 请求参数


def help():
    print(
        "monitor.exe\n\t{0}\n\t{1}\n\t{2}\n\t{3}\n\t{4}\n\t{5}\n\t{6}".format(
            "-h|--help\t帮助文档",
            "-t|--type\t请求服务类型\n\t\t1:\tPDF2PPTX\n\t\t2:\tIMAGES2PPTX\n\t\t3:\tPDF2IMAGES",
            "-s|--src\t请求转换资源文件路径",
            "-d|--dest\t请求转换资源转换后保存路径",
            "-p|--dpi\tPDF转换参数：指定转换图片 DPI 值",
            "-e|--extension\tPDF转换参数：指定转换图片扩展名",
            "-o|--open\t是否于转换后打开相应目录"))


if __name__ == "__main__":
    main()
