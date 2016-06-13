# coding=utf-8
import time
import FrameStrings
import urllib2
import sys
import socket

class HttpEntity:
    def __init__(self):
        self. __requesturl__ = ''
        self.__requestbody__ = ''
        self.__responsecode__ = ''
        self.__responsestring__ = ''
        self.starttime = 0
        self.endtime = 0
        self.__runStatus__ = FrameStrings.sResultNotExecute
    def getResponseCode(self):
        return self.__responsecode__
    def getResponseString(self):
        return self.__responsestring__
    def setResponseCode(self,code):
        self.__responsecode__ = code
    def setResponseString(self,resonsestring):
        self.__responsestring__ = resonsestring
    def setRunStatus(self,str):
        self.__runStatus__ = str
    def getRunStatus(self):
        return self.__runStatus__
    def getCostTime(self):
        return self.endtime - self.starttime

def HttpGet(url):
    print url
    e = HttpEntity()
    response = None
    try:
        e.starttime = time.time()
        request = urllib2.Request(url)
        request.add_header('Content-Type', 'text/plain;charset=UTF-8')
        response = urllib2.urlopen(request,timeout=FrameStrings.HTTPTIMEOUT)
        e.setResponseString(response.read())
        e.setResponseCode(response.code)
        e.endtime = time.time()
        e.setRunStatus(FrameStrings.sResultOK)
    except urllib2.URLError as ex:
        e.setRunStatus(FrameStrings.sResultFail)
        if hasattr(ex, 'code'):
            print 'Error code:',ex.code
        elif hasattr(ex, 'reason'):
            print 'Reason:',ex.reason
        e.setResponseCode(ex.code)
        print sys._getframe().f_code.co_name
        print ex.__class__,ex
    except socket.error:
        #超时
        e.setRunStatus(FrameStrings.sResultFail)
        e.setResponseCode('TIMEOUT')
    finally:
        if response:
            response.close()
    return e
