#  phoney_dictate/phoney_dictate/iface.py
#
#  Copyright 2026 Leon Dionne <ldionne@dridesign.sh.cn>
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
Functions for retrieving local network netmask
"""
from netifaces import ifaddresses, interfaces, AF_INET

def address_subnet():
	for iface in interfaces():
		infos = ifaddresses(iface)
		if AF_INET in infos:
			for address_info in infos[AF_INET]:
				if address_info['addr'].startswith('127'):
					continue
				i_parts = [ int(part) for part in address_info['addr'].split('.') ]
				m_parts = [ int(part) for part in address_info['netmask'].split('.') ]
				s_parts = [ i_parts[i] & m_parts[i] for i in range(4) ]
				width = f'{m_parts[0]:b}{m_parts[1]:b}{m_parts[2]:b}{m_parts[3]:b}'.count('1')
				return address_info['addr'], '.'.join(str(spart) for spart in s_parts ) + f'/{width}'
	return None


#  end phoney_dictate/phoney_dictate/iface.py
