
import subprocess
import os

from config import config as conf
from config import setting
from log import ACOLogger

# Params

log = ACOLogger()


# Shell.PDF2IMAGES

def PDF2IMAGES():
    # log
    log.logger.info("PDF2IMAGES")

    # init
    pre()

    # run
    log.logger.debug("java", "-jar", setting.jar, conf.src,
                     conf.dest, str(conf.dpi), conf.ext)
    p = subprocess.Popen(["java", "-jar", setting.jar, conf.src,
                          conf.dest, str(conf.dpi), conf.ext],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()

    # return
    if stderr:
        log.logger.error("STDERR: %s", stderr)
        return None
    else:
        log.logger.info("STDOUT: %s", stdout)
        # log.logger.info(conf.dest)
        return conf.dest


# Shell.PDF2PPTX


def PDF2PPTX():
    log.logger.info("PDF2PPTX")

    path = PDF2IMAGES()
    if path:
        conf.src = path
        IMAGES2PPTX()


# Shell.IMAGES2PPTX


def IMAGES2PPTX():
    # log
    log.logger.info("IMAGES2PPTX")

    # init
    pre()
    exe = os.getcwd() + "/" + setting.exe
    bOpen = "true"
    if False == conf.open:
        bOpen = "false"

    # run
    log.logger.info("IMAGES2PPTX: %s %s %s", exe, conf.src,
                    conf.dest, setting.template, bOpen)
    s, d = subprocess.getstatusoutput(
        [exe,  conf.src, conf.dest, setting.template, ])
    log.logger.info("STDOUT:")
    log.logger.info(s)
    log.logger.info(d)

    if 0 != s:
        log.logger.error("STDERR: %s", d)


# Shell.DataInit

def pre():
    if conf.src:
        if os.path.isfile(conf.src):
            conf.dest = conf.src[0:conf.src.rindex("\\")]
        else:
            conf.dest = conf.src
