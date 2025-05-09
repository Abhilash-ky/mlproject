import sys

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() # __ is used to ignore the first two values
    file_name = exc_tb.tb_frame.f_code.co_filename # get the file name
    error_message = "Error occred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))   #getlne number & error_message
    return error_message
    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) # call the parent class constructer
        self.error_message = error_message_detail(error_message,error_detail) # call the error message detail function
    def __str__(self):
        return self.error_message