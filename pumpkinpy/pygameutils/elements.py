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
    """
    class ButtonText: General purpose text-based button.
    button.Draw(WINDOW); button.Update() in game loop
    button.clicked to check if clicked.
    """
    def __init__(self, loc, size, bgColIdle, bgColHover, bgColPress, text, textOffset, border=0, borderCol=None, clickButton=0):
        """
        Initializes the button.
        :param loc: Tuple specifying pixel location: (100, 100)
        :param size: Tuple specifying pixel width and height dimensions: (200, 50)
        :param bgColIdle: Color (RGB) when not hovered over or clicked.
        :param bgColHover: Color (RGB) when hovered but not clicked.
        :param bgColPress: Color (RGB) when clicked.
        :param text: Pygame text object (obtained from font.render())
        :param textOffset: Offset location of text from center of button: (10, 10)
        :param border: Width of border (set to 0 to disable).
        :param borderCol=None: Color of border (ignored if no border).
        :param clickButton: Mouse button to register as a click (0 for left, 1 for middle, and 2 for right).
        """
        self.loc = loc
        self.size = size
        self.textLoc = (loc[0] + textOffset[0] + (size[0]-text.get_width())//2, loc[1] + textOffset[1] + (size[1]-text.get_height())//2)
        self.bgCols = {
            "IDLE": bgColIdle,
            "HOVER": bgColHover,
            "PRESS": bgColPress
        }
        self.currBgCol = bgColIdle
        self.text = text
        self.border = border > 0
        self.borderWidth = border
        self.borderCol = borderCol
        self.clickButton = clickButton
        self.clicked = False

    def Draw(self, window):
        """
        Draws button on a window.
        :param window: Pygame window object to draw on.
        """
        pygame.draw.rect(window, self.currBgCol, self.loc+self.size)
        window.blit(self.text, self.textLoc)
        if self.border:
            pygame.draw.rect(window, self.borderCol, self.loc+self.size, self.borderWidth)

    def Update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[self.clickButton]

        loc = self.loc
        size = self.size
        if (loc[0] <= mouse[0] <= loc[0]+size[0]) and (loc[1] <= mouse[1] <= loc[1]+size[1]):
            if click:
                self.currBgCol = self.bgCols["PRESS"]
                self.clicked = True
            else:
                self.currBgCol = self.bgCols["HOVER"]
                self.clicked = False
        else:
            self.currBgCol = self.bgCols["IDLE"]
            self.clicked = False