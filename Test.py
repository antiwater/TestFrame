# -*- coding: utf-8 -*-
#字体库
import reportlab.lib.fonts
#canvas画图的类库
from reportlab.pdfgen.canvas import Canvas
#用于定位的inch库，inch将作为我们的高度宽度的单位
from reportlab.lib.units import inch


if __name__ == "__main__":
    #声明Canvas类对象，传入的就是要生成的pdf文件名字
    can = Canvas('report.pdf')
    pdf_head(can, "test for REPORTLAB!")
    #showpage将保留之前的操作内容之后新建一张空白页
    can.showPage()
    #将所有的页内容存到打开的pdf文件里面。
    can.save()


def pdf_head(canvas, headtext):
    #setFont是字体设置的函数，第一个参数是类型，第二个是大小
    canvas.setFont("Helvetica-Bold", 11.5)
    #向一张pdf页面上写string
    canvas.drawString(1*inch, 10.5*inch, headtext)
    #画一个矩形，并填充为黑色
    canvas.rect(1*inch, 10.3*inch, 6.5*inch, 0.12*inch,fill=1)
    #画一条直线
    canvas.line(1*inch, 10*inch, 7.5*inch, 10*inch)