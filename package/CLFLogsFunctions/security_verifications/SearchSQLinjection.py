##
## LogsAnalyserTool
## File description:
## SearchSQLinjection
##

import re
from . import security_common_functions as sec_common

def sql_warn_nb(log_url, special_char, sql_key_words): # return percantage of dangerous characters in a log line --> BETA
    warn_score = sec_common.find_world_in_str(log_url, special_char)
    warn_score += sql_key_words
    if (warn_score > 0 and warn_score < 10):
        return ("LOW")
    elif (warn_score >= 10 and warn_score < 30):
        return ("MEDIUM")
    else:
        return ("HIGH")

def SQL_injection(log_object, fd, security_test):
    sql_special_world = ['EXEC XP_', 'EXEC SP_', 'OPENROWSET', 'EXECUTE IMMEDIATE', 'UNION SELECT', 'INSERT', 'UPDATE']
    sql_key_words = sec_common.find_world_in_str(log_object.url, sql_special_world)
    special_char = ["%21", "%22", "%23", "%24", "%25", "%26", "%27", "%28", "%29", "%2A", "%21", "%21", "%21", "%3D", "%2A", "%3F", "%5E"]
    if (re.match(r'[^\n]+(\%3D)|(=)(\%27)|(\')|(\-\-)|(\%23)', log_object.url) or\
        re.match(r'/\w*((\%27)|(\’))((\%6F)|o|(\%4F))((\%72)|r|(\%52))/ix', log_object.url) or sql_key_words > 0):
        fd.write("SQL INJECTIONS->" + sql_warn_nb(log_object.url, special_char, sql_key_words) + " | " + "DATE->" + str(log_object.date) +\
        " | HOST->" + log_object.host + " | REQUEST->" + log_object.request + " | URL->" + log_object.url)
        fd.write("\n")
        security_test[1] += 1