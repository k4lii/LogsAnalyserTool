##
## LogsAnalyserTool
## File description:
## LogsAnalyserTool
##

import sys
import os.path
from package.common_functions.common_1 import *
from package.CLFLogsFunctions.import_log import *
from package.BackLogs.import_log import *
from package.CLFLogsFunctions.security_verifications import SearchSQLinjection, SearchXSSattack, SearchCSRFattack, SearchWebAppExtracting, security_common_functions as sec_common

###################FRONT FUNCTIONS####################

#---------------GLOBAL VARIABLES --> Front_security_tests--------------#
front_list_security_test = [0, 0] #nb_xss/nb_sql
#----------------------------------------------------------------------#

def Front_specific_security_tests(security_test, options, log_object, fd_report):
    for i in range(0, len(options)):
        if (options[i] == "-xss"):
            call_as_thread(SearchXSSattack.XSS_attack, (log_object, fd_report, security_test, ))
        if (options[i] == "-sql"):
            call_as_thread(SearchSQLinjection.SQL_injection, (log_object, fd_report, security_test, ))
    return (security_test)

def Front_result(fd_report, security_test, line_nb, sys_argv):
    fd_report.write("\n##########RESULTS##########\n" +"\nFILE->" + sys_argv[2] + "\nTOTAL LOGS->"  + str(line_nb) + "\nSQL INJECTIONS->" + str(security_test[1]) + "\nXSS INJECTIONS->" +\
    str(security_test[0]) + "\nPERCENTAGE OF SUSPECT LOGS->" + str(((security_test[1] + security_test[0]) / line_nb) * 100)[:5] + "%")

def Front_security_tests(sys_argv, options, fd): #function who call all the security tests functions for Frontend logs
    step = 0
    line_nb = count_lines(sys.argv[2])
    fd_report = open(sec_common.security_report_name_gen("Frontend"), "a")
    two_logs = [Front_logs(), Front_logs(), 0]

    for i in range(0, line_nb):
        step = print_step(step, i, line_nb)
        log_object = import_inova_front_log(fd)
        if (log_object != -1): #if the actual line is a correct log
            if (len(options) > 0): #if specifics parameters are selected
                Front_specific_security_tests(front_list_security_test, options, log_object, fd_report)
            else: #if no optional parameters are selected, calling all test in threads
                call_as_thread(SearchSQLinjection.SQL_injection, (log_object, fd_report, front_list_security_test, ))
                call_as_thread(SearchXSSattack.XSS_attack, (log_object, fd_report, front_list_security_test, ))
                call_as_thread(SearchWebAppExtracting.WebExtraction_attack, (log_object, fd_report, front_list_security_test, fd, i, two_logs, ))
    Front_result(fd_report, front_list_security_test, line_nb, sys_argv)
    fd_report.close()
    fd.close()

###################BACK FUNCTIONS####################

def Back_security_tests(sys_argv, options, fd): #function who call all the security tests functions for Frontend logs
    line_nb = count_lines(sys.argv[2])
    
    for i in range(0, line_nb):
        log_object = import_inova_back_log(fd)
    fd.close()

###################MAIN####################

def Main_error_managment():
    if (len(sys.argv) < 3 or sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        print("######OPTIONS######\nLogsAnalyserTool --backlogs/-b [logfile] || --frontlogs/-f [logfile(UTF-8)] [-xss]/[-sql]/[csrf]")
        sys.exit(0)
    elif (os.path.isfile(sys.argv[2]) == True):
        return (open(sys.argv[2], "r"))
    else:
        print("Incorrect file !")
        sys.exit(0)

def Launch(fd):
    if (len(sys.argv) > 2):
        options = list()
        for i in range(3, len(sys.argv)):
            options.append(sys.argv[i])
    if (sys.argv[1] == "--backend" or sys.argv[1] == "-b"):
        Back_security_tests(sys.argv, options, fd)
    elif (sys.argv[1] == "--frontend" or sys.argv[1] == "-f"):
        Front_security_tests(sys.argv, options, fd)
    else:
        print("Incorrect option !")
        sys.exit(0)

Launch(Main_error_managment())