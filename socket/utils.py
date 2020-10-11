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

import zlib
from ..global.functions import Encrypt, Decrypt

def Receive(conn, header=256):
    """
    Receives a message from a socket connection.
    :param conn: Connection obtained from \"conn, addr = server.accept()\"
    :param header: Amount of bytes in header message.
    :return: class bytes, received message.
    """

    msg = conn.recv(header)
    while not msg:
        msg = conn.recv(header)

    msg = conn.recv(int(msg))
    return msg


def Send(conn, msg, header=256):
    """
    Sends a message to a socket connection.
    :param conn: Connection obtained from \"conn, addr = server.accept()\"
    :param msg: Message to send in bytes format.
    :param header: Amount of bytes in header message.
    :return: None
    """

    length = len(msg)
    headerMsg = str(length).encode() + b" " * (header-length)
    conn.send(headerMsg)
    conn.send(msg)


def Compress(msg):
    """
    Compresses and encrypts a message Note: The encryption can be found in pumpkinpy.global.functions.Encrypt.
    :param msg: String message to compress.
    :return: Compressed bytes message.
    """

    return zlib.compress(Encrypt(msg).encode())