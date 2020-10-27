#  ##### BEGIN GPL LICENSE BLOCK #####
# 
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

def Send(conn, msg, header=256):
    """
    Sends a socket message.
    :param conn: Socket connection.
    :param msg: Message (bytes).
    :param header: Length of header message.
    """
    length = len(msg)
    headMsg = (str(length) + " "*header-length).encode()
    conn.send(headMsg)
    conn.send(msg)