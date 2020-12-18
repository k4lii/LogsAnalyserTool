##
## LogsAnalyserTool
## File description:
## class_definition
##

class Front_logs(): #Front log_obj object's structure
    def FrontLogStruct(self, host, date, request, url, protocol, http_code, time):
       self.host = host
       self.date = date
       self.request = request
       self.url = url
       self.protocol = protocol
       self.http_code = http_code
       self.time = time