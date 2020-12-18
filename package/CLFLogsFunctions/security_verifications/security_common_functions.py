##
## package
## File description:
## security_common_functions
##

import datetime

def find_world_in_str(string, test_words): # try to find word in a str with a list
    nb_words = 0
    test_words_lenght = len(test_words)
    for i in range (0, test_words_lenght):
        if (string.count(test_words[i]) != -1):
            nb_words += string.count(test_words[i])
    return (nb_words)

def security_report_name_gen(logs_type):
    date = datetime.datetime.now()
    str1 = "Security_reports/" + logs_type + "/SecurityReport_"
    str2 = str(date.day) + "-" + str(date.month) + "-" + str(date.year) + "_" + str(date.hour) + '-' + str(date.minute)
    return (str1 + str2 + ".txt")