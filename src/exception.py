import sys
def exception_message(error,error_details:sys):
    
    _,_,exc_tb = error_details.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "The error is  happend in [{0}] file in [{1}] number line and the message is [{2}] ".format(
        filename,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        
        self.error_message = exception_message(error_message,error_details)
        
    def __str__(self):
        return self.error_message