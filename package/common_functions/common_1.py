##
## LogsAnalyserTool
## File description:
## functions1
##

import re
import threading

def print_step(step, id, line_nb): #print step in percentage -> if you do real time analysis, you should remove this functions
    if (int((id / line_nb) * 100) == step): #print the calculation progression
        step += 5
        print(step, "%")
    return (step)

def multiple_replace(banned_char, log_line, replace_with): # replace many characters in one time
    for i in range (0, len(banned_char)):
       log_line = log_line.replace(banned_char[i], replace_with)
    return (log_line.split())

def is_a_correct_front_log_line(log_line): # verify if a line is a real log's line(using IP)
    if (re.match(r'([0-9]{1,3}\.){3}[0-9]{1,3}', log_line)):
        return (1)
    return (0)

def is_a_correct_back_log_line(log_line): # verify if a line is a real log's line(using DATE)
    if (re.match(r'[0-9]{2}([:][0-9]{2}){2}[,][0-9]{3}', log_line)):
        return (1)
    return (0)

def count_lines(file): #count all lines
    i = 0
    fd = open(file, 'r')
    for line in fd:
	    i += 1
    fd.close()
    return (i)

def count_logs(sys_argv): # count all "true" log's lines
    nb_logs = 0
    fd = open(sys_argv[2], 'r')
    nb_lines = count_lines(sys_argv[2])
    for x in range (0, nb_lines):
        str = fd.readline()
        if (sys_argv[1] == "-backend"):
            if (is_a_correct_back_log_line(str[:12])):
                nb_logs += 1
        elif (sys_argv[1] == "-frontend"):
            if (is_a_correct_front_log_line(str[:12])):
                nb_logs += 1
    return (nb_logs)

def call_as_thread(function_name, options):
    thread = threading.Thread(target = function_name, args = options)
    thread.start()
    thread.join()