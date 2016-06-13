# coding=utf-8
import FrameStrings
import time
from HttpUtil import *

# class TestResult:
#     def __init__(self):
#         # self.__executeTime__ = time.strftime(FrameStrings.ISOTIMEFORMAT, time.localtime())
#         self.__responseCode__ = -1
#         self.__resultString__ = ''
#         self.__escapedTime__ = -1
#          #用例执行日期时间





class TestCase:
    __argNames__ = []
    __caseId__ = -1
    # __testResult__ = TestResult()
    __isencrpt__ = FrameStrings.sNoEncrypt
    __requestString__ = ''
    __responseCode__ = -1
    __resultString__ = ''
    __executeTime__ = ''
    __result__ = FrameStrings.sResultNotExecute

    ###
    def getResultExecuteTime(self):
        return self.__executeTime__
    def setResultExecuteTime(self):
        self.__executeTime__ = time.strftime(FrameStrings.ISOTIMEFORMAT, time.localtime())
        #  self.__executeTime__ = time.time()
    #运行结果
    def setRunStatus(self,str):
        self.__result__ = str
    def getRunStatus(self):
        return self.__result__
    #应答代码
    def setResultResponseCode(self,code):
        self.__responseCode__ = code
    def getResultResponseCode(self):
        return self.__responseCode__
    #应答全文
    def setResultResponseString(self,s):
        self.__resultString__ = s
    def getResultResponseString(self):
        return self.__resultString__
    #执行用例耗时
    def getResultEscapedTime(self):
        return self.__escapedTime__
    def setResultEscapedTime(self,t):
        self.__escapedTime__ = t
    ###
    # def getTestResult(self):
    #     return self.__testResult__
    # def setHttpResposne(self,response):
    #     self.__httpResponse__ = response
    # def getHttpResponse(self):
    #     return self.__httpResponse__

    def setRequestString(self,reqString):
        self.__requestString__ = reqString
    def getRequestString(self):
        return self.__requestString__

    def __init__(self,caseid,argnames,isencrypt):
        print('###  init test case ###',caseid)
        #如果参数名列表为空，返回
        if(len(argnames) <= 0):
            print('No args!')
            exit()
        self.__isencrpt__ = isencrypt
        self.__caseId__ = caseid
        self.__argNames__ = []
        self.__argNames__ = argnames
        self.__caseId__ = caseid
        # self.__testResult__ = TestResult()
        self.__httpResponse__ = None
        self.rowNo = -1




