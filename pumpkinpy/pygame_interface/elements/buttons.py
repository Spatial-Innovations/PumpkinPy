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
        self._calc_text_pos()

    def update_info(self, **kwargs):
        """
        Updates location, size, etc
        :param kwargs: All arguments in __init__
        """
        self._loc = kwargs["loc"] if "loc" in kwargs else self._loc
        self._size = kwargs["size"] if "size" in kwargs else self._size
        self._colors = kwargs["colors"] if "colors" in kwargs else self._colors
        self._border = kwargs["border"] if "border" in kwargs else self._border
        self._border_color = kwargs["border_color"] if "border_color" in kwargs else self._border_color
        self._texts = kwargs["texts"] if "texts" in kwargs else self._texts
        self._text_offset = kwargs["text_offset"] if "text_offset" in kwargs else self._text_offset
        self._click_buttons = kwargs["click_buttons"] if "click_buttons" in kwargs else self._click_buttons
        self._calc_text_pos()
    
    def draw(self, window, events):
        """
        Draws the button on the window.
        """
        if self.clicked(events):
            rect_color = self.colors[2]
            text = self._texts[2]
            text_loc = self._text_pos[2]
        elif self.hovered():
            rect_color = self.colors[1]
            text = self._texts[1]
            text_loc = self._text_pos[1]
        else:
            rect_color = self.colors[0]
            text = self._texts[0]
            text_loc = self._text_pos[0]

        pygame.draw.rect(window, rect_color, self._loc+self._size)
        window.blit(text, text_loc)
        if self._border > 0:
            pygame.draw.rect(window, self.border_color, self._loc+self._size, self._border)

    def hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        if (self._loc[0] <= mouse_pos[0] <= self._loc[0]+self._size[0]) and (self._loc[1] <= mouse_pos[1] <= self._loc[1]+self._size[1]):
            return True
        else:
            return False
    
    def clicked(self, events):
        if self.hovered():
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button in self._click_buttons:
                        return True

        return False

    def _calc_text_pos(self):
        self._text_pos = []
        for i in range(3):
            diff = (self._size[0] - self._texts[i].get_width(), self._size[1] - self._texts[i].get_height())
            self._text_pos.append((diff[0]+self._loc[0], diff[1]+self._loc[1]))