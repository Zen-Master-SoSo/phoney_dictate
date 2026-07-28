#  phoney-dictate/__main__.py
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
import sys, argparse
from PyQt5.QtWidgets import QApplication
from qt_extras import exceptions_hook
from xdg_soso import is_xdg
from phoney_dictate import MainWindow, PhoneyDictateSetup


def main():
	parser = argparse.ArgumentParser()
	parser.epilog = __doc__
	if is_xdg():
		parser.add_argument('--install', '-i', action = 'store_true',
			help = """Install this application into your desktop
environment. This will create a desktop launcher so you can start PhoneyDictate from
your menu or Dash.""")
		parser.add_argument('--uninstall', '-u', action = 'store_true',
			help = """Remove PhoneyDictate from your desktop environment.
The program will still be on your computer, and can be called from the command
line as "phoney-dictate", but you won't be able to see it in your desktop
applications menu.""")
	options = parser.parse_args()

	if options.install:
		PhoneyDictateSetup().install()
	elif options.uninstall:
		PhoneyDictateSetup().uninstall()
	else:
		app = QApplication(sys.argv)
		sys.excepthook = exceptions_hook
		window = MainWindow()
		window.show()
		sys.exit(app.exec())

if __name__ == '__main__':
	main()


#  end phoney-dictate/__main__.py
