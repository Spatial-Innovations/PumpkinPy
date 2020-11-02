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

class CameraOrtho:
    """
    Orthographic camera used in rendering.
    """
    def __init__(self, loc=(0, 0, 0), rot=(0, 0, 0), size=1):
        """
        Initialize the camera.
        :param loc: 3D location (x, y, z) of camera.
        :param rot: 3D Euler rotation (x, y, z) of camera.
        :param size: Orthographic size of camera (horizontal, vertical will be auto generated).
        """
        self.type = "ORTHO"
        self.loc = loc
        self.rot = rot
        self.size = size


class CameraPersp:
    """
    Perspective camera used in rendering.
    """
    def __init__(self, loc=(0, 0, 0), rot=(0, 0, 0), fov=1):
        """
        Initialize the camera.
        :param loc: 3D location (x, y, z) of camera.
        :param rot: 3D Euler rotation (x, y, z) of camera.
        :param fov: Field of view of camera (horizontal, vertical will be auto generated.).
        """
        self.type = "PERSP"
        self.loc = loc
        self.rot = rot
        self.fov = fov


class Face:
    """
    3D mesh face.
    """
    def __init__(self, verts, color):
        """
        Initalize the face.
        :param verts: List or tuple of vertex locations (x, y, z) in order.
        :param color: Color (rgb) of face.
        """
        self.verts = verts
        self.color = color