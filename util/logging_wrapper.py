#
# Copyright (c) all rights reserved
# Author: Lohnwave waveluozu@163.com
# Created on 2024-1-5
#
from logging.handlers import TimedRotatingFileHandler
import logging
from datetime import datetime

# call in main module
def LogInit(prefix='test', out_file=False, log_level="INFO"):
    # define log format
    log_format = '%(asctime)s:%(msecs)03d %(threadName)s %(levelname)s %(filename)s:%(lineno)d %(message)s'
    date_format = '%Y%m%d %H:%M:%S'

    # create a logger
    logger = logging.getLogger()
    logger.setLevel(log_level)

    if out_file == True:
        current_time = datetime.now().strftime("%Y%m%d-%H%M%S")
        # create a file handler split by day
        logt_file_handler = TimedRotatingFileHandler(
            filename=f'{prefix}-{current_time}.log', # file name
            when='midnight', # split by day in midnight
            interval=1,
            backupCount=7, # maintain 7 days log
            encoding='utf-8' # set encoding
        )
        logt_file_handler.suffix = "%Y%m%d-%H%M%S.log" # file name suffix

        logt_file_handler.setFormatter(logging.Formatter(log_format, datefmt=date_format))

        # add handler to logger
        logger.addHandler(logt_file_handler)
    else:
        logging.basicConfig(
            level=log_level,
            format=log_format,
            datefmt=date_format
        )

    logger.info('service begin running...')