##
## LogsAnalyserTool
## File description:
## class_definition
##

class Back_logs(): #Back log_obj object's structure
    def BackLogStruct(self, date, status, java_classname, thread, action_info):
       self.date = date
       self.status = status
       self.java_classname = java_classname
       self.thread = thread
       self.action_info = action_info