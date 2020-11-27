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

import pygame
from math import pi, radians, sin, cos
from time import sleep


class CamOrtho:
    def __init__(self, angle, size, shift):
        """
        Initializes camera.
        :param angle: Tuple of floats specifying (latitude, longitude)
        :type angle: Tuple[float, float]
        :param size: Float specifying orthographic size of camera
        :type size: float
        :param shift: Tuple of floats specifying (x_shift, y_shift)
        :type shift: Tuple[float, float]
        """
        self.angle = angle
        self.size = size
        self.shift = shift

    def render(self, resolution, mesh, matcap=None):
        """
        Renders the given mesh.
        :param resolution: Tuple of pixel resolutions. The Y size will be adjusted, and the X size will be the ortho size.
        :type resolution: Tuple[int, int]
        :param mesh: Mesh object
        :type mesh: pumpkinpy.view3d.Mesh
        :param matcap: Matcap image to render as
        :type matcap: pygame.surface, or None
        """
        surface = pygame.Surface(resolution)
        for face in mesh.faces:
            curr_verts = []
            for vert in face[1]:
                curr_verts.append(self._project_vert(vert, resolution))
            pygame.draw.polygon(surface, (128, 128, 128), curr_verts)

        return surface

    def _project_vert(self, loc, res):
        """
        z = inverse cos' shift right pi/4
        x = inverse cos shift left pi/4
        """
        angle = (radians(self.angle[0]), radians(self.angle[1]))
        scale_fac = (res[0] / self.size, res[1] / self.size)
        pix_loc = []

        # X location
        x_axis = cos(angle[1]) * loc[0] * scale_fac[0]
        y_axis = sin(angle[1]) * loc[1] * scale_fac[0]
        pix_loc.append(x_axis + y_axis)
        #print(x_axis, y_axis)

        # Y location
        x_axis = sin(angle[1]) * loc[0] * scale_fac[1]
        y_axis = -1 * cos(angle[1]) * loc[1] * scale_fac[1]
        z_axis = sin(angle[0]) * loc[2] * scale_fac[1]
        pix_loc.append(x_axis + y_axis + z_axis)
        #print(x_axis, y_axis, z_axis)

        pix_loc = (pix_loc[0] + res[0]//2, pix_loc[1] + res[1]//2)
        #raise SystemExit
        return pix_loc