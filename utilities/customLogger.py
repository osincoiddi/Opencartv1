#utility file is used as a common file for all test cases.
##Logs files:
# Type of logs;
# 1)Warn log
# 2)Debug log
# 3)Info log
# 3)Error log
# 4)Fatal log
#Note:debug log is recommended since it provides detail info

import logging
import os
from logging import basicConfig


class LogGen():
    @staticmethod
    def loggen():
        path=os.path.abspath(os.curdir)+ '\\logs\\automation.log'
        logging.basicConfig(filename=path,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)#set log type of your choice ie error,warn,debug.
        return logger


# #Approach2
# class LogGen():
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename="..\\logs\\automation.log",
#                             format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%y %I:%M:%S %p')
#         logger = logging.getLogger()
#         logger.setlevel(logging.ERROR)
#         return logger
