try:
	from Pyside6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from Pyside2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance

import maya.OpenMayaUi as omui
import os

ICON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'icon'))

class PrimitiveCreatorDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.resize(300,350)
		self.setWindowTitle('Primitive Creator')

		self.main_layout = QtWidgets.QVBoxLayuot()
		self.setLayout(self.main_layout)

		self.primitive_listWidget = QtWidgets.QListWidget()
		self.primitive_listWidget.setIconSize(QtCore.QSize(60,60))
		self.primitive_listWidget.setSpacing(8)
		self.primitive_listWidget.setViewMode(QtWidgets,QListView.IconMode)
		self.primitive_listWidget.setMovement(QtWidgets.QListView.Static)
		self.primitive_listWidget.setResizeMode(QtWidgets.QListView.Adjust)

		self.main_layout.addWidget(self.primitive_listWidget)

		self.name_layout = QtWidgets.QHBoxLayuot()
		self.main_layout.addLayout(self.name_layout)

		self.name_label = QtWidgets.QLabel('Name:')
		self.name_lineEdit.addLayout(self.name_layout)
		self.name_layout.addWidgets(self.name_label)
		self.name_layout.addWidgets(self.name_lineEdit)

		self.button_layout = QtWidget.QHBoxLayuot()
		self.main_layout.addLayout(self.button_layout)
		self.create_button = QtWidgets.QPushButton('Create')
		self.cancel_button = QtWidgets.QPushButton('Cancel')
		self.button_layout.addStretch()
		self.button_layout.addWidgets(self.create_button)
		self.button_layout.addWidgets(self.cancel_button)

		self.initIconWidgets()

	def initIconWidgets(self):
		prims = ['cone', 'cube', 'sphere', 'torus']
		for prim in prims:
			item = QtWidgets.QListWidgetItem(prim)
			item.setIcon(QtGui.QIcon(os.path.join(ICON_PATH, f'{prim}.png')))
			self.primitive_listWidget.addItem(item)


def run():
	global ui

	try:
		ui.close()
	except:
		pass
	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = PrimitiveCreatorDialog(parent=ptr)
	ui.show()