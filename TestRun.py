# coding=utf-8
from TestCase import *
from HttpUtil import *
from XlsUtil import *

def run(filename,sheetname):
    a = XlsUtil(filename)
    a.open()
    baseurl = a.getTestUrl(sheetname) + a.getInterfaceName(sheetname) + 'mdurl='
    caseList = a.getTestCaseListBySheetName(sheetname)
    requrl = ''
    for c in caseList:
        requrl = baseurl + c.getRequestString()
        r = HttpGet(requrl)
        c.setRunStatus(r.getRunStatus())
        c.setResultResponseCode(r.getResponseCode())
        c.setResultResponseString(r.getResponseString())
        c.setResultEscapedTime(r.getCostTime())
        c.setResultExecuteTime()
    a.writeTestResult(caseList,sheetname)



