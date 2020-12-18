##
## LogsAnalyserTool
## File description:
## back_logs_functions
##

from datetime import datetime
from package.common_functions.common_1 import *
from .class_definition import *

def parse_backend_log(log_line): #parse one back-end log
    banned_char = ['\"', '-', ';','[',']', "'"]
    return (multiple_replace(banned_char, log_line, ""))

def remove_gap_btw_logs(line): #remove the gap between log's lines 
    if (line == "Request"):
        return (5)
    else:
        return (4)

def import_inova_back_log(fd): #import all backend's log in an object
    log_obj = Back_logs()
    line = fd.readline()
    
    if (is_a_correct_back_log_line(line[:12])):
        parsed_log = parse_backend_log(line)
        start = remove_gap_btw_logs(parsed_log[5])
        log_obj.BackLogStruct(datetime.strptime(parsed_log[0],"%H:%M:%S,%f").strftime('%H:%M:%S'),\
        parsed_log[1], parsed_log[2], line[line.find('(') + 1 : line.find(')')], parsed_log[start:])
    return (log_obj)
