#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os
import argparse
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in3f
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--overlay-text', type=str, default="", help="Text to overlay on the image")
    args = parser.parse_args()
    overlay_text = args.overlay_text

    logging.info("epd7in3f Demo")

    epd = epd7in3f.EPD()   
    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    logging.info("read img whatever")
    Himage = Image.open(os.path.join(picdir, 'ben_is_a_hack.bmp'))
    
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font40 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 40)
    
    draw = ImageDraw.Draw(Himage)
    draw.text((5, 45), overlay_text, font = font40, fill = epd.RED)

    epd.display(epd.getbuffer(Himage))


if __name__ == "__main__":
    try:
        main()
    except IOError as e:
        logging.info(e)
    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd7in3f.epdconfig.module_exit(cleanup=True)
        exit()
