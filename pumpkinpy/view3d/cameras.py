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
        self._angle = angle
        self._size = size
        self._shift = shift

    def render(self, mesh, matcap=None):
        """
        Renders the given mesh.
        :param mesh: Mesh object
        :type mesh: pumpkinpy.view3d.Mesh
        :param matcap: Matcap image to render as
        :type matcap: pygame.surface, or None
        """

    def set_angle(self, angle):
        """
        Sets the camera angle.
        :param angle: Tuple of floats specifying (latitude, longitude)
        :type angle: Tuple[float, float]
        """
        self._angle = angle

    def set_size(self, size):
        """
        Sets the camera size.
        :param size: Float specifying orthographic size of camera
        :type size: float
        """
        self._size = size

    def set_shift(self, shift):
        """
        Sets the camera shift.
        :param shift: Tuple of floats specifying (x_shift, y_shift)
        :type shift: Tuple[float, float]
        """
        self._shift = shift