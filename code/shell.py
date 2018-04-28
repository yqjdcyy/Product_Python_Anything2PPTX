
import os
import subprocess

from config import config as conf
from config import setting
from log import ACOLogger

# Params

logger = ACOLogger().logger


# Shell.PDF2IMAGES

def PDF2IMAGES():
    # log
    logger.info("PDF2IMAGES")

    # init
    pre()

    # run
    logger.debug("java", "-jar", setting.jar, conf.src,
                 conf.dest, str(conf.dpi), conf.ext)
    p = subprocess.Popen(["java", "-jar", setting.jar, conf.src,
                          conf.dest, str(conf.dpi), conf.ext],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()

    # return
    if stderr:
        logger.error("STDERR: %s", stderr)
        return None
    else:
        logger.info("STDOUT: %s", stdout)
        # logger.info(conf.dest)
        return conf.dest


# Shell.PDF2PPTX


def PDF2PPTX():
    logger.info("PDF2PPTX")

    path = PDF2IMAGES()
    if path:
        conf.src = path
        IMAGES2PPTX()


# Shell.IMAGES2PPTX


def IMAGES2PPTX():
    # log
    logger.info("IMAGES2PPTX")

    # init
    pre()
    exe = os.getcwd() + "/" + setting.exe
    bOpen = "true"
    if False == conf.open:
        bOpen = "false"

    # run
    logger.info("IMAGES2PPTX: %s %s %s %s", exe, conf.src,
                conf.dest, setting.template, bOpen)
    s, d = subprocess.getstatusoutput(
        [exe,  conf.src, conf.dest, setting.template, bOpen])
    logger.info("STDOUT:")
    logger.info(s)
    logger.info(d)

    if 0 != s:
        logger.error("STDERR: %s", d)


# Shell.DataInit

def pre():
    if not conf.dest:
        logger.debug("Pre Config.src=%s", conf.src)
        if os.path.isfile(conf.src):
            idx = 0
            try:
                idx = conf.src.rindex("\\")
            except Exception:
                idx = conf.src.rindex("/")
            conf.dest = conf.src[0:idx]
        else:
            conf.dest = conf.src
