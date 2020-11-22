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


class ButtonText:
    def __init__(self, loc, size, colors, border, border_color, texts, text_offset, click_buttons):
        """
        Initializes button. All of these parameters can be re-defined when drawing.
        :param loc: Location of the button
        :type loc: Tuple[int, int]
        :param size: Size of the button
        :type size: Tuple[int, int]
        :param colors: Tuple of (idle color, hover color, click color)
        :type colors: Tuple[Tuple[int, int, int], Tuple[int, int, int], Tuple[int, int, int]]
        :param border: Border thickness
        :type border: int
        :param border_color: Color of border
        :type border_color: Tuple[int, int, int]
        :param texts: Tuple of (idle text, hover text, click text)
        :type texts: Tuple[PygameSurface, PygameSurface, PygameSurface]
        :param text_offset: Offset of text relative to centered
        :type text_offset: Tuple[int, int]
        :param click_buttons: Tuple of buttons to register as click (LMB=1, MMB=2, RMB=3)
        :type click_buttons: Tuple[int]
        """

        self._loc = loc
        self._size = size
        self._colors = colors
        self._border = border
        self._border_color = border_color
        self._texts = texts
        self._text_offset = text_offset
        self._click_buttons = click_buttons

    def draw(self, window, **kwargs):
        """
        Draws the button on the window.
        kwargs include all args in ButtonText.__init__.
        """