#!/usr/bin/python
# -*- coding:utf-8 -*-
from PyQt4 import QtGui,QtCore,Qt
import sys
import mainWindows
import loginWindows

'''
Xiami For Linux Project
'''
class XiamiPlayer(object):
    def __init__(self):
        super(XiamiPlayer, self).__init__()
        self.app = QtGui.QApplication(sys.argv)
                
        self.loginWindow = loginWindows.LoginWindows()
        self.loginWindow.inputEnd.connect(self.loginInputEnd)
        self.loginWindow.show()

        # Run
        sys.exit(self.app.exec_())

    def loginInputEnd(self,mail,pwd):
        self.mainWinow = mainWindows.MainWindow()
        print mail,pwd        

if __name__ == '__main__':
    xiamiPlayer = XiamiPlayer()
