#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
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

try:
    logging.info("epd7in3f Demo")

    epd = epd7in3f.EPD()   
    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    logging.info("read img whatever")
    Himage = Image.open(os.path.join(picdir, 'ben_is_a_hack.bmp'))
    
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font40 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 40)
    
    # # Drawing on the image
    # logging.info("1.Drawing on the image...")
    # Himage = Image.new('RGB', (epd.width, epd.height), epd.WHITE)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    # draw.text((5, 0), 'hello world', font = font18, fill = epd.RED)
    # draw.text((5, 20), '7.3inch e-Paper (F)', font = font24, fill = epd.YELLOW)
    # read from an arg called overlay-text
    overlay_text = sys.argv[1] if len(sys.argv) > 1 else ""

    draw.text((5, 45), overlay_text, font = font40, fill = epd.RED)
    #draw.text((5, 45), 'days until worlds', font = font40, fill = epd.RED)
    #draw.text((5, 85), '100', font = font40, fill = epd.RED)

    epd.display(epd.getbuffer(Himage))    # font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)

except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in3f.epdconfig.module_exit(cleanup=True)
    exit()
