##
## LogsAnalyserTool
## File description:
## functions1
##

from datetime import datetime
from package.common_functions.common_1 import *
from .class_definition import *

def parse_front_log(log_line): #parse one front-end log
    banned_char = ['\"', '-', ';','[',']', "'", '+']
    return (multiple_replace(banned_char, log_line, ""))

def import_inova_front_log(fd): #import all backend's log in an object
    log_obj = Front_logs()
    line = fd.readline()

    if (is_a_correct_front_log_line(line[:10])):
        parsed_log = parse_front_log(line)
        log_obj.FrontLogStruct(parsed_log[0], datetime.strptime(parsed_log[1], "%d/%b/%Y:%H:%M:%S"),\
        parsed_log[3], parsed_log[4], parsed_log[5], parsed_log[6], parsed_log[7])
        return (log_obj)
    else:
        return (-1)