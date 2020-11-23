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


class Mesh:
    def __init__(self, verts, faces, colors):
        """
        Initializes the mesh.
        :param verts: List of vertex locations.
        :type verts: Tuple[Tuple[float, float, float]]
        :param faces: List of 3 or more indexes corresponding to verts.
        :type faces: Tuple[Tuple[int]]
        :param colors: Tuple of RGB colors corresponding to each face.
        :type colors: Tuple[Tuple[int, int, int]]
        """
        self.set_mesh(verts, faces, colors)

    def set_mesh(self, verts, faces, colors):
        """
        Initializes the mesh.
        :param verts: List of vertex locations.
        :type verts: Tuple[Tuple[float, float, float]]
        :param faces: List of 3 or more indexes corresponding to verts.
        :type faces: Tuple[Tuple[int]]
        :param colors: Tuple of RGB colors corresponding to each face.
        :type colors: Tuple[Tuple[int, int, int]]
        """
        self.verts = verts
        self.faces = []
        for i, face in enumerate(faces):
            self.faces.append([colors[i], []])
            for i in face:
                self.faces[-1][1].append(verts[i])