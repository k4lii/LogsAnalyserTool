##
## LogsAnalyserTool
## File description:
## SearchCSRFattack
##

import re

def CSRF_attack(log_object, fd):
    #fd.write("##########CSRF ATTACK##########\n\n")
    if (re.search(r'(%3C).*(%3E)', log_object.url)):# recherche toutes les lignes entre balise -> <text>
        ""
        """
        fd.write("DATE->" + str(log_object[i].date) + " | HOST->" + log_object[i].host + " | REQUEST->" +\
        log_object[i].request +  " | URL->" + log_object[i].url)
        fd.write("\n")
        """