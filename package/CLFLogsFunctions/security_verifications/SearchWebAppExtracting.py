##
## LogsAnalyserTool
## File description:
## SearchWebAppExtracting
##

from . import security_common_functions as sec_common
import re
import sys

def WebExtraction_attack_score():
    ""


def is_the_same_path(str_A, str_B): # permit to know if two log have the same URL
    """print( str_A.url)
    test = str_A.url.replace(" ", "")
    print (test)"""

def compare_logs_similarity(str_A, str_B): #compare prowimity between url, method(GET), date and IP
    """if (is_the_same_path(str_A, str_B) == 1): #url
        print ("la ressource des deux lignes de logs possèdes la meme URL-->", str_A.url)
    print("\n##################\n")"""

def WebExtraction_attack(log_object, fd_report, security_test, fd, i, two_logs):
    if (two_logs[2] == 0):
        two_logs[0] = log_object
        two_logs[2] = 1
    elif (two_logs[2] == 1):
        two_logs[1] = log_object
        two_logs[2] = 0
    if (i > 0):
        if (two_logs[2] == 1):
            compare_logs_similarity(two_logs[1], two_logs[0])
        elif (two_logs[2] == 0):
            compare_logs_similarity(two_logs[0], two_logs[1])
    return (two_logs)