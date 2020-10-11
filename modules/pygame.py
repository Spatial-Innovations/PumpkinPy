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

class Colors:
    # Static colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 0, 255)

    # Dynamic colors
    def Gray(value):
        if not 0 <= value <= 255:
            raise ValueError(f"Invalid value: {value}")
        return (value,) * 3


class Fonts:
    small = {
        "ROBOTO": pygame.font.SysFont("roboto", 18),
        "COMICSANS": pygame.font.SysFont("comicsans", 18),
        "ARIAL": pygame.font.SysFont("arial", 18),
        "GEORGIA": pygame.font.SysFont("georgia", 18)
    }

    medium = {
        "ROBOTO": pygame.font.SysFont("roboto", 36),
        "COMICSANS": pygame.font.SysFont("comicsans", 36),
        "ARIAL": pygame.font.SysFont("arial", 36),
        "GEORGIA": pygame.font.SysFont("georgia", 36)
    }

    large = {
        "ROBOTO": pygame.font.SysFont("roboto", 48),
        "COMICSANS": pygame.font.SysFont("comicsans", 48),
        "ARIAL": pygame.font.SysFont("arial", 48),
        "GEORGIA": pygame.font.SysFont("georgia", 48)
    }


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


class ImageButton:
    def __init__(self, loc, size, idleImage, activeImage, borderColor=Colors.BLACK, borderThickness=0):
        """
        Creates a button that you can click. It alternates between images whether or not it is clicked

        :param loc: the x, y position of the button
        :param size: the width and height of the button
        :param idleImage: the image the button is displaying if the button has not been clicked yet
        :param activeImage: the image the button is displaying if the button has been clicked
        """
        self.active = False
        self.loc, self.size = loc, size
        self.idleImage, self.activeImage = idleImage, activeImage
        self.borderColor, self.thickness = borderColor, borderThickness

    def Draw(self, window):
        """
        Draws the button on the given surface
        
        :param window: the surface you want to draw the button on
        """
        window.blit(pygame.scale.transform(self.activeImage if self.active else self.idleImage, self.size), self.loc)
        pygame.draw.rect(window, self.borderColor, (*self.loc, *self.size), self.thickness)

    def Update(self, window, events):
        """
        Intended to call this method every iteration of your game loop. It draws the button and checks clicking.
        
        :param window: the surface you want to draw the button on
        :param events: the events from your project(pygame.event.get())
        """
        self.Draw(window)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.active = True if self.active == False else False
