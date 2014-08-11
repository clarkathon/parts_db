#!/usr/bin/python


"""
This is the actual GUI we will use to enter in the .csv and the simple entry ways


"""

import sys
from PyQt4 import QtGui, QtCore


class parts(QtGui.QWidget):

	def __init__(self):

		super(parts, self).__init__()

		self.initUI()

	def initUI(self):

		#qbtn = QtGui.QPushButton('Quit', self)
		#qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)  
		
		#qbtn.resize(qbtn.sizeHint())
		#qbtn.move(200, 200)

		part_no = QtGui.QLabel('Part Number')
		package = QtGui.QLabel('Package')
		description = QtGui.QLabel('Description or Details')
		quantity = QtGui.QLabel('Quantity')
		projects = QtGui.QLabel('Projects')
		

		self.setGeometry(150, 150, 600, 400)
		self.setWindowTitle('Inventory Set Up')
		self.show()

def main():

	app = QtGui.QApplication(sys.argv)

	start = parts()

	sys.exit(app.exec_())



if __name__ == '__main__':
	main()

