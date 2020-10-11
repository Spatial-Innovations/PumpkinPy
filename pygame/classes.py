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
from .constants import Colors


class Button:
    def __init__(self, loc, size, font, text, bgCol=Colors.Gray(128), textCol=Colors.BLACK, borderThickness=0, borderColor=Colors.BLACK):
        """
        Creates a button which you can draw on the screen and check for clicks.

        :param loc: the x, y position of the button on the screen
        :param size: the width and height of the button
        :param font: a pygame.font.SysFont() instance
        :param text: the text that you want the button to display
        :param bgCol: the color of the button
        :param textCol: the color of the text you want to display
        :param borderThickness: the thickness of the border surrounding the button
        :param borderColor: the color of the border surrounding the button
        """
        self.loc, self.size = loc, size
        self.font = font
        self.text = text
        self.bgCol, self.textCol = bgCol, textCol
        self.thickness, self.borderColor = borderThickness, borderColor
        self.surf = font.render(text, 1, textCol)
        self.rect = pygame.Rect(*loc, *size)

    def ChangeText(self, newText):
        """
        Changes the text that will be displayed on top of the button
        :param newText: the new text that you want to change the current text to.
        :return: None
        """
        self.text = newText
        self.surf = self.font.render(self.text, 1, self.textCol)

    def ChangeTextColor(self, newTextColor):
        """
        Changes the color of the text
        :param newTextColor: the new color of the text.
        :return: None
        """
        self.textCol = newTextColor
        self.surf = self.font.render(self.text, 1, self.textCol)

    def ChangeBgColor(self, newBgColor):
        """
        Changes the background color of the button
        :param newBgColor: the new background color of the button.
        :return: None
        """
        self.bgCol = newBgColor

    def ChangeBorderColor(self, newBorderColor):
        """
        Changes the border color of the button
        :param newBorderColor: the new border color of the button.
        :return: None
        """
        self.borderColor = newBorderColor
    
    def ChangeBorderThickness(self, newBorderThickness):
        """
        Changes the thickness of the border
        :param newBorderThickenss: the new thickness of the border of the button.
        :return: None
        """
        self.thickness = newBorderThickness

    def Draw(self, window):
        """
        Draws the button onto the give surface
        :param window: the surface you want to draw the button to.
        :return: None
        """
        pygame.draw.rect(window, self.bgCol, self.rect)
        pygame.draw.rect(window, self.borderColor, self.rect, self.thickness)
        window.blit(self.surf, (int(self.loc[0] + self.size[0]/2 - self.surf.get_width()/2), int(self.loc[1] + self.size[1]/2 - self.surf.get_height()/2)))

    def Clicked(self):
        """
        Checks if the button is clicked
        :return: bool value indicating whether or not the button is clicked
        """
        return self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]
