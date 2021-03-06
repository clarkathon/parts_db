#!/usr/bin/python


"""
This is the actual GUI we will use to enter in the .csv and the simple entry ways
We will be able to add or edit a part and we will be able to add or edit a projects


"""

import sys
import os
from PyQt4 import QtGui, QtCore


# These lines are so that the models can be used in the GUI
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "inventory.settings")
from parts.models import *


class parts_gui(QtGui.QWidget):

	def __init__(self):

		super(parts_gui, self).__init__()

		self.initUI()


	def initUI(self):

		wkr_btn = QtGui.QPushButton('Add Worker', self)
		wkr_btn.clicked.connect(add_worker)  
		
		wkr_btn.resize(wkr_btn.sizeHint())
		wkr_btn.move(200, 200)

		part_no = QtGui.QLabel('Part Number')
		package = QtGui.QLabel('Package')
		description = QtGui.QLabel('Description or Details')
		quantity = QtGui.QLabel('Quantity')
		projects = QtGui.QLabel('Projects')
		

		self.setGeometry(150, 150, 600, 400)
		self.setWindowTitle('Inventory Set Up')
		self.show()


def add_worker():
	w = Worker(first="dummy", last="dummy", role="none", access="none")
	w.save()


def main():

	app = QtGui.QApplication(sys.argv)

	start = parts_gui()

	sys.exit(app.exec_())



if __name__ == '__main__':
	main()

