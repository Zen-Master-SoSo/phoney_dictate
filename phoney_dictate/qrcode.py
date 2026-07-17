#  phoney_dictate/qrcode.py
#
#  Copyright 2025 Leon Dionne <ldionne@dridesign.sh.cn>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
"""
A voice recognition "app" which sends your cell phone's voice recognition input to your computer.
"""
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel
from qrcodegen import QrCode


class QRCodeDialog(QDialog):
	"""
	Shows the host url encoded as a qrcode.
	"""

	def __init__(self, parent, url):
		super().__init__(parent)
		qrcode = QrCode.encode_text(url, QrCode.Ecc.MEDIUM)
		qrsize = qrcode.get_size()
		block_size = 420 // qrsize
		pixmap = QPixmap(qrsize * block_size, qrsize * block_size)
		painter = QPainter(pixmap)
		for x in range(qrsize):
			for y in range(qrsize):
				rect = QRect(x * block_size, y * block_size, block_size, block_size)
				painter.fillRect(rect, Qt.black if qrcode.get_module(x, y) else Qt.white)
		painter.end()
		label = QLabel(self)
		label.setPixmap(pixmap)
		label.setFixedSize(qrsize * block_size, qrsize * block_size)
		lo = QVBoxLayout()
		lo.addWidget(label)
		self.setLayout(lo)


#  end phoney_dictate/qrcode.py
