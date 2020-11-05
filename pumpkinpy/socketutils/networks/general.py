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

import socket
import pickle
import threading


class Server:
    def __init__(self, client, ip, port=5555, msgLen=4096):
        self.clientClass = client
        self.ip = ip
        self.port = port
        self.msgLen = msgLen

        self.clients = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((ip, port))

    def Start(self, cleanup=True):
        threading.Thread(target=self._Accept, args=()).start()
        if cleanup:
            threading.Thread(target=self._Cleanup, args=()).start()

    def _Accept(self):
        self.server.listen()
        while True:
            conn, addr = self.server.accept()
            client = self.clientClass(conn, addr)
            self.clients.append(client)
            threading.Thread(target=client.Start(), args=()).start()

    def _Cleanup(self):
        while True:
            for i, c in enumerate(self.clients):
                if not c.active:
                    del self.clients[i]


class Client:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
