import sys

def error_msg_detail(err_msg:Exception, err_detail:sys)-> str: # type: ignore
    _,_,ex_tb = err_detail.exc_info()
    filename:str = ex_tb.tb_frame.f_code.co_filename # type: ignore
    line_no:int = ex_tb.tb_lineno # type: ignore

    return "error occurred in script: [{0}] \nat line number [{1}] \nerror: [{2}]".format(
        filename, line_no, str(err_msg)
    )

class CustomException(Exception):
    def __init__(self, error:Exception, err_detail:sys): # type: ignore
        super().__init__(error) # type: ignore
        self.error = error_msg_detail(error, err_detail)
    
    def __str__(self):
        return self.error







