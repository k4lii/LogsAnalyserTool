##
## LogsAnalyserTool
## File description:
## SearchXSSattack
##

from . import security_common_functions as sec_common
import re

def print_xss_line(priority, log_object, fd):
    fd.write("XSS_INJECTION->" + priority + " | " + str(log_object.date) + " | HOST->" + log_object.host + " | REQUEST->" +\
    log_object.request + " | URL->" + log_object.url)
    fd.write("\n")

def xss_warn_score(log_url): # return a nb who correspond to the log's line dangerosity --> BETA
    special_char = ["%21", "%22", "%23", "%24", "%25", "%26", "%27", "%28", "%29", "%2A", "%21", "%21", "%21", "%3D", "%2A", "%3F", "%5E"]
    warn_score = sec_common.find_world_in_str(log_url, special_char)
    if (re.search(r'(%3C).*(%3E)', log_url) or re.search(r'(%253C).*(%253E)', log_url)):
        warn_score += 10
    return (warn_score)

def XSS_attack(log_object, fd, security_test):
    warn_score = xss_warn_score(log_object.url)
    if (re.search(r'(%3C).*(%3E)', log_object.url) or re.search(r'(%253C).*(%253E)', log_object.url)):
        if (warn_score >= 5 and warn_score < 20):
            print_xss_line("LOW", log_object, fd)
        elif (warn_score >= 20 and warn_score < 50):
            print_xss_line("MEDIUM", log_object, fd)
        elif (warn_score >= 50):
            print_xss_line("HIGH", log_object, fd)
        security_test[0] += 1