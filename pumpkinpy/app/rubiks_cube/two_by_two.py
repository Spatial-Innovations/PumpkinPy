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

class Cube:
    def __init__(self, **kwargs):
        """
        2 by 2 cube class.
        :param position (kwarg): position of cube as described in readme.
        :param finalDepth (kwarg): Final depth of search
        """
        if "fromMoves" in kwargs:
            self.position = kwargs["position"]
            self.currDepth = kwargs["currDepth"]
            self.finalDepth = kwargs["finalDepth"]
            self.fromMoves = kwargs["fromMoves"]
            self.Search()
        else:
            self.position = kwargs["position"]
            self.currDepth = 0
            self.finalDepth = kwargs["finalDepth"]
            self.fromMoves = []

    def Search(self):
        self.branches = []
        moves = ("MoveU", "MoveUPrime", "MoveR", "MoveRPrime", "MoveF", "MoveFPrime")
        for m in moves:
            currCube = Cube(position=self.position, currDepth=self.currDepth+1, finalDepth=self.finalDepth, fromMoves=self.fromMoves)
            getattr(currCube, m)()
            self.branches.append(currCube)

    def MoveU(self):
        pos = self.position
        pos[0][0], pos[0][1], pos[0][2], pos[0][3] = pos[0][3], pos[0][0], pos[0][1], pos[0][2]
        pos[1][1], pos[1][0], pos[5][1], pos[5][0], pos[3][1], pos[3][0], pos[4][1], pos[4][0] = \
            pos[4][1], pos[4][0], pos[1][1], pos[1][0], pos[5][1], pos[5][0], pos[3][1], pos[3][0]

    def MoveUPrime(self):
        pos = self.position
        pos[0][0], pos[0][1], pos[0][2], pos[0][3] = pos[0][1], pos[0][2], pos[0][3], pos[0][0]
        pos[1][1], pos[1][0], pos[4][1], pos[4][0], pos[3][1], pos[3][0], pos[5][1], pos[5][0] = \
            pos[5][1], pos[5][0], pos[1][1], pos[1][0], pos[4][1], pos[4][0], pos[3][1], pos[3][0]

    def MoveR(self):
        pos = self.position
        pos[4][0], pos[4][1], pos[4][2], pos[4][3] = pos[4][3], pos[4][0], pos[4][1], pos[4][2]
        pos[0][2], pos[0][1], pos[3][0], pos[3][3], pos[2][2], pos[2][1], pos[1][2], pos[1][1] = \
            pos[1][2], pos[1][1], pos[0][2], pos[0][1], pos[3][0], pos[3][3], pos[2][2], pos[2][1]

    def MoveRPrime(self):
        pos = self.position
        pos[4][0], pos[4][1], pos[4][2], pos[4][3] = pos[4][1], pos[4][2], pos[4][3], pos[4][0]
        pos[0][2], pos[0][1], pos[1][2], pos[1][1], pos[2][2], pos[2][1], pos[3][0], pos[3][3] = \
            pos[3][0], pos[3][3], pos[0][2], pos[0][1], pos[1][2], pos[1][1], pos[2][2], pos[2][1]

    def MoveF(self):
        pos = self.position
        pos[1][0], pos[1][1], pos[1][2], pos[1][3] = pos[1][3], pos[1][0], pos[1][1], pos[1][2]
        pos[0][3], pos[0][2], pos[4][0], pos[4][3], pos[2][1], pos[2][0], pos[5][2], pos[5][1] = \
            pos[5][2], pos[5][1], pos[0][3], pos[0][2], pos[4][0], pos[4][3], pos[2][1], pos[2][0]

    def MoveFPrime(self):
        pos = self.position
        pos[1][0], pos[1][1], pos[1][2], pos[1][3] = pos[1][1], pos[1][2], pos[1][3], pos[1][0]
        pos[0][3], pos[0][2], pos[5][2], pos[5][1], pos[2][1], pos[2][0], pos[4][0], pos[4][3] = \
            pos[4][0], pos[4][3], pos[0][3], pos[0][2], pos[5][2], pos[5][1], pos[2][1], pos[2][0]