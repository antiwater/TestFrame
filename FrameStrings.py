# coding=utf-8
import sys

#error messages
sError = 'Error!'
sEmpyt = 'Empty!'
sNoArgs = 'No args!'
sInvalidArgName = 'Invalid argument name!'
#excel cell content
sEncrypt   = 'Y'
sNoEncrypt = 'N'
#null
sNull = '@Null'

#test reuslt
sResultOK = 'PASS'
sResultFail = 'FAILED'
sResultNotExecute = 'NonExecute'

#time format
ISOTIMEFORMAT= '%Y-%m-%d %X'

#http
HTTPTIMEOUT = 10
HTTPPORT = 80

#Excel Col Define
XLResponseCode  = 7
XLResultString  = 8
XLExecuteTime   = 9
XLResult        = 10
XLEscapedTime   = 11
XLDescription   = 12

# #debug
# def get_info():
#     print sys._getframe().f_code.co_filename  #当前文件名，可以通过__file__获得
#     print sys._getframe().f_code.co_name  #当前函数名
#     print sys._getframe().f_lineno #当前行号



TESTURL = 'http://enohp.mindai.com/v3/borrow/getlist/all_tender_list?mdurl=KzT8EQhWazkCuSgg3Ei6cluAL9zMER%2BVx3ZsZlUSZBKHA0V3S9aciRUDGa3ycAuSPAjymMm0If6B%0Ah4F5jIIJZQPXTTSlNvw8dXdyNYwwQcKBNaTNWdw6i%2FGxBiWV9ykWfd%2BBbv7Oj3qSlJTg5uzW8byr%0APVOgx%2FXoeMgQQiBKn2ERKHgfD2nmv%2BXcUxyUEmzE3DW%2F7s4vf%2B40Txvn1mv9Fg%3D%3D'