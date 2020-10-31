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
import threading
import pickle

class Server:
    """Server class, for use once in server file."""
    clients = []

    def __init__(self, ip, port):
        """
        Initializes server.
        :param ip: Ip address of server.
        :param port: Port of server.
        """
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((ip, port))

    def Start(self, removeInactiveClients=True):
        """
        Starts accepting clients.
        :param removeInactiveClients=True: Remove disconnected clients.
        """
        threading.Thread(target=self._Accept, args=()).start()
        if removeInactiveClients:
            threading.Thread(target=self._RemoveInactive, args=()).start()

    def _Accept(self):
        self.server.listen()
        while True:
            conn, addr = self.server.accept()
            self.clients.append(AcceptedClient(conn, addr))

    def _RemoveInactive(self):
        while True:
            for i, c in enumerate(self.clients):
                if not c.active:
                    del self.clients[i]


class AcceptedClient:
    """Client accepted from server."""
    active = True

    def __init__(self, conn, addr):
        """
        Initializes client.
        :param conn: Connection.
        :param addr: Address.
        """
        self.conn = conn
        self.addr = addr

    def Send(self, obj):
        """
        Sends a message.
        :param obj: Any object to send (will use pickle.)
        """
        data = pickle.dumps(obj)
        self.conn.send(data)

    def Receive(self, msgLen=4096):
        """
        Receives a message.
        :param msgLen: Length of bytes to receive.
        :return: Object received.
        """
        data = self.obj.recv(msgLen)
        return pickle.loads(data)


class Client:
    """Client object to use in client file."""
    def __init__(self, conn):
        """
        Initializes client.
        :param conn: Connection.
        """
        self.conn = conn

    def Send(self, obj):
        """
        Sends a message.
        :param obj: Any object to send (will use pickle.)
        """
        data = pickle.dumps(obj)
        self.conn.send(data)

    def Receive(self, msgLen=4096):
        """
        Receives a message.
        :param msgLen: Length of bytes to receive.
        :return: Object received.
        """
        data = self.obj.recv(msgLen)
        return pickle.loads(data)