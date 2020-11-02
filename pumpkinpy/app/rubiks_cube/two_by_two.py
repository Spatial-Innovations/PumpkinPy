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
        """
        if "fromMoves" in kwargs:
            self.fromMoves = kwargs["fromMoves"]
            self.currDepth = kwargs["currDepth"]
            self.finalDepth = kwargs["finalDepth"]
            self.position = kwargs["position"]
            self.Search()
        else:
            self.position = kwargs["position"]