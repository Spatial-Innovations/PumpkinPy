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
    """
    Server class, to be created once in the server system.
    """

    def __init__(self, client, ip, port=5555, msgLen=4096):
        """
        Initializes the server.
        :param client: Client class (customized) to use.
        :param ip: Ip address of server.
        :param port: Port of server.
        :param msgLen: Message length of socket.
        """
        self.clientClass = client
        self.ip = ip
        self.port = port
        self.msgLen = msgLen

        self.clients = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((ip, port))

    def Start(self, cleanup=True):
        """
        Starts the server.
        :param cleanup: If True, will remove inactive clients.
        """
        threading.Thread(target=self._Accept, args=()).start()
        if cleanup:
            threading.Thread(target=self._Cleanup, args=()).start()

    def _Accept(self):
        self.server.listen()
        while True:
            conn, addr = self.server.accept()
            client = self.clientClass(conn, addr, self.msgLen)
            self.clients.append(client)
            threading.Thread(target=client.Start(), args=()).start()

    def _Cleanup(self):
        while True:
            for i, c in enumerate(self.clients):
                if not c.active:
                    del self.clients[i]


class Client:
    """
    Base client class, to be customized.
    """

    def __init__(self, conn, addr, msgLen):
        """
        Initializes the client. This will be called by the server.
        :param conn: Connection of client.
        :param addr: Address of client.
        :param msgLen: Message length.
        """
        self.conn = conn
        self.addr = addr
        self.msgLen = msgLen
        self.active = True

    def Start(self):
        """
        The customized function. This will be called on a separate thread when the client is accepted.
        Remember to create a disconnect protocol.
        """

    def Send(self, obj):
        """
        Sends an object to the client computer.
        :param obj: Object to send.
        """
        data = pickle.dumps(obj)
        self.conn.send(data)

    def Receive(self):
        """
        Receives an object from the client computer.
        """
        data = self.conn.recv(self.msgLen)
        return pickle.loads(data)
