# coding=utf-8
# import xlwt
import xlrd
import FrameStrings
import TestCase
import Encrypt
import string
import json
import FrameStrings
from xlutils.copy import copy
#修改编码，适配中文
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class XlsUtil:
    __filename__ = ''
    __hasopened__ = 0
    __currentsheet__ = ''
    __casecount__ = -1
    __argscount__ = -1
    __caselist__ = []
    __argsNameList__ = []
    __cursheetname__ = ''
    def __init__(self,filename):
        self.__filename__ = filename

    def open(self):
        if(self.__filename__ == ''):
            print('Please set file name first!')
            exit()
        try:
            xlrd.Book.encoding = "gbk"
            self.__book__ = xlrd.open_workbook(self.__filename__)
            self.__hasopened__ = 1
        except:
            print('Fail to open Excel file!')
            self.__hasopened__ = 0
            exit();

    def getInterfaceCount(self):
        if(self.__hasopened__ == 0):
            self.open()
        return  len(self.__book__.sheet_names())


    def writeTestResult(self,caselist,sheetname):
        self.__cursheetname__ = sheetname
        try:
            rb = xlrd.open_workbook(self.__filename__,formatting_info=True)
            rs = rb.sheet_by_name(sheetname)
            wb = copy(rb)
            #根据sheet名称获取sheet索引 用于get_sheet
            idx = rb.sheet_names().index(sheetname)
            ws = wb.get_sheet(idx)
            for c in caselist:
                ws.write(c.rowNo,FrameStrings.XLResult,c.getRunStatus())
                ws.write(c.rowNo,FrameStrings.XLExecuteTime,c.getResultExecuteTime())
                ws.write(c.rowNo,FrameStrings.XLResponseCode,c.getResultResponseCode())
                # ws.write(c.rowNo,FrameStrings.XLResponseCode,'11111')
                if(c.getRunStatus() == FrameStrings.sResultOK):
                    #json返回值状态 0:成功 1:错误
                    j = json.loads(c.getResultResponseString())
                    ws.write(c.rowNo,FrameStrings.XLResultString,j['result'])
                    ws.write(c.rowNo,FrameStrings.XLEscapedTime,c.getResultEscapedTime())
            wb.save(self.__filename__)

        except Exception,e:
            print sys._getframe().f_code.co_name
            print Exception,e



    def writeCell(self,sheetname,row,col,str):
        self.__cursheetname__ = sheetname
        try:
            rb = xlrd.open_workbook(self.__filename__)
            rs = rb.sheet_by_name(sheetname)
            wb = wb = copy(rb)
            ws = wb.get_sheet(0)
            ws.write(row,col,str)
            wb.save(self.__filename__)

        except Exception,e:
            print sys._getframe().f_code.co_name
            print Exception,e


    #根据行列坐标获取单元格内容
    def __getCellContent__(self,sheetname='Login',row=0,col=0):
        self.__cursheetname__ = sheetname
        try:
            self.__currentsheet__ = self.__book__.sheet_by_name(sheetname)
            if(self.__currentsheet__.cell(row,col).ctype == 0):
                return ''
            s = self.__currentsheet__.cell(row,col).value
            #数字，且以.0结尾，去掉.0
            s=str(s)
            if('0'== s[-1] and  '.' == s[-2]):
                s = s[:-2]
            return s.encode('utf-8')
        except Exception,e:
            print sys._getframe().f_code.co_name
            print Exception,":",e
            print('Fail to open sheet in __getCellContent__')
            return FrameStrings.sError

    #根据行获取整行内容
    #返回值为list
    def __getRowContent__(self,sheetname='Login',row=0):
        self.__cursheetname__ = sheetname
        try:
            self.__currentsheet__ = self.__book__.sheet_by_name(sheetname)
            return self.__currentsheet__.row_values(row)
        except:
            print sys._getframe().f_code.co_name
            print('Fail to open sheet in __getRowContent__')
            return FrameStrings.sError

    def getTestUrl(self,sheetname):
        self.__cursheetname__ = sheetname
        return self.__getCellContent__(sheetname='Login',row=0,col=1)
    def getInterfaceName(self,sheetname):
        self.__cursheetname__ = sheetname
        return self.__getCellContent__(sheetname='Login',row=1,col=1)
    def getIsEncrypt(self,sheetname):
        self.__cursheetname__ = sheetname
        return self.__getCellContent__(sheetname='Login',row=2,col=1)
    def getArgsCount(self,sheetname):
        self.__cursheetname__ = sheetname
        self.__argscount__ = int(self.__getCellContent__(sheetname='Login',row=3,col=1))
        return self.__argscount__
    def getCaseCount(self,sheetname):
         self.__cursheetname__ = sheetname
         try:
            self.__currentsheet__ = self.__book__.sheet_by_name(sheetname)
            self.__casecount__ = self.__currentsheet__.nrows-5
            return self.__casecount__
         except Exception,e:
            print sys._getframe().f_code.co_name
            print Exception,":",e
            print('Fail to open sheet in getCaseCount')
            return FrameStrings.sError

    def getArgsName(self,sheetname):
        self.__cursheetname__ = sheetname
        if(self.__argscount__ < 0):
            self.getArgsCount(sheetname)
        self.__argsNameList__ = self.__getRowContent__(sheetname=sheetname,row=4)[2:2+self.__argscount__]
        return self.__argsNameList__

    def getTestCaseListBySheetName(self,sheetname):
        if(self.__casecount__ <= 0):
            self.getCaseCount(sheetname)
        if(len(self.__argsNameList__) <= 0):
            self.getArgsName(sheetname)
        if(self.__argscount__ <= 0):
            self.getArgsCount(sheetname)

        list = []
        for i in range(0,self.__casecount__):
            c = TestCase.TestCase(i,self.__argsNameList__,self.getIsEncrypt(sheetname))
            #list.append(case)
            #添加参数名称和参数值
            #从第6行（row=5）开始是用例
            rowcontenlist = self.__getRowContent__(sheetname,5+i)
            s=''
            for j in range(0,self.__argscount__):
                #第5行（row=4）为参数名称
                #第3列（col=2）开始为参数名称
                argName = self.__getCellContent__(sheetname=sheetname,row=4,col=2+j)
                argVal  = self.__getCellContent__(sheetname=sheetname,row=5+i,col=2+j)
                c.rowNo = 5+i
                ####直接将参数名称和参数值转为字符串 e.g. name=xxl*passwd=1123
                if(len(argVal) > 0):
                    s += argName
                    s += '='
                    s += argVal
                    s += '&'
                ####
                if(self.getIsEncrypt(sheetname) == FrameStrings.sEncrypt):
                    c.setRequestString(Encrypt.Encrypt(s[0:-1]))
                else:
                    c.setRequestString(s[0:-1])
            list.append(c)

        self.__caselist__ = list

        return self.__caselist__





