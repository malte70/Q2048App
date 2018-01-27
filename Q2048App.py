#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWebKitWidgets

class AppInfo(object):
	Name        = "Q2048App"
	Version     = "0.0.1"
	Description = "Gabriele Cirulli's 2048, wrapped in a minimal Qt desktop application"
	WebViewURL  = "https://gabrielecirulli.github.io/2048/"
	
class Q2048MainWindow(PyQt5.QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.title  = AppInfo.Name + " " + AppInfo.Version
		self.left   = 10
		self.top    = 10
		self.width  = 640
		self.height = 400
		self.initUI()
		
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		
		self.webview = PyQt5.QtWebKitWidgets.QWebView()
		self.webview.load(
			PyQt5.QtCore.QUrl(AppInfo.WebViewURL)
		)
		
		self.setCentralWidget(self.webview)
		
		self.showMaximized()
		
		
def main():
	app = PyQt5.QtWidgets.QApplication(sys.argv)
	
	main_window = Q2048MainWindow()
	app.exec()
	
if __name__ == "__main__":
	main()
	
