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
import numpy as np
import random
from colorsys import hsv_to_rgb, rgb_to_hsv
from .errors import *

pygame.init()


class ButtonText:
    """
    class ButtonText: General purpose text-based button.
    button.Draw(WINDOW) in game loop
    button.clicked to check if clicked.
    """

    def __init__(self, loc, size, bgColIdle, bgColHover, bgColPress, text, textOffset=(0, 0), border=0, borderCol=(0, 0, 0), clickButton=0):
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
        :param borderCol: Color of border (ignored if no border).
        :param clickButton: Mouse button to register as a click (0 for left, 1 for middle, and 2 for right).
        """
        self.loc = loc
        self.size = size
        self.textLoc = (loc[0] + textOffset[0] + (size[0]-text.get_width()) //
                        2, loc[1] + textOffset[1] + (size[1]-text.get_height())//2)
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

    def Draw(self, window, events):
        """
        Draws button on a window.
        :param window: Pygame window object to draw on.
        :param events: Events obtained from pygame.events.get()
        """
        pygame.draw.rect(window, self.currBgCol, self.loc + self.size)
        window.blit(self.text, self.textLoc)
        if self.border:
            pygame.draw.rect(window, self.borderCol,
                             self.loc+self.size, self.borderWidth)

        mouse = pygame.mouse.get_pos()
        click = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

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


class TextInput:
    def __init__(self, loc, size, bgCol, borderWidth=5, borderCol=(0, 0, 0), initialText="", label="", font=pygame.font.SysFont("comicsans", 35),
                 textCol=(0, 0, 0), cursorCol=(0, 0, 1), repeatInitial=400, repeatInterval=35, maxLen=-1, password=False, editing=False):
        """
        Input text class for Pygame.
        :param loc: Pixel location (x, y).
        :param size: Pixel size (x, y).
        :param bgCol: Background color (R, G, B).
        :param borderWidth: Width of border (pixels).
        :param borderCol: Color of border (RGB).
        :param initialText: Text to start with.
        :param label: Label (name) of input.
        :param font: pygame.font object.
        :param textCol: Color of text.
        :param cursorCol: Color of cursor.
        :param repeatInitial: Initial delay (ms) for repeating (pressed down keys).
        :param repeatInterval: Delay between repeats (pressed down keys).
        :param maxLen: Maximum length of string (-1 = inf)
        :param password: Boolean specifying whether to display as asterisks (*).
        :param editing: Default to enter edit mode.
        """

        self.passwordField = password

        self.loc, self.size = loc, size

        self.editing = editing

        self.textCol = textCol
        self.password = password
        self.text = initialText
        self.label = label
        self.maxLen = maxLen

        self.rect = pygame.Rect(*loc, *size)
        self.bgCol = bgCol
        self.borderCol, self.borderWidth = borderCol, borderWidth

        self.font = font

        self.surface = pygame.Surface((1, 1))
        self.surface.set_alpha(0)

        self.keyrepeatCounters = {}
        self.keyrepeatInitial = repeatInitial
        self.keyrepeatInterval = repeatInterval

        self.cursorSurf = pygame.Surface(
            (int(font.get_height() / 20 + 1), font.get_height()))
        self.cursorSurf.fill(cursorCol)
        self.cursorPos = len(initialText)
        self.cursorVisible = True
        self.cursorSwitch = 500
        self.cursorCounter = 0

        self.clock = pygame.time.Clock()

    def Draw(self, window, events):
        pygame.draw.rect(window, self.bgCol, self.rect)
        if self.borderWidth:
            pygame.draw.rect(window, self.borderCol,
                             self.rect, self.borderWidth)

        textPos = (int(self.loc[0] + self.size[0]//2 - self.surface.get_width()/2),
                   int(self.loc[1] + self.size[1]//2 - self.surface.get_height()/2))
        window.blit(self.surface, textPos)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.editing = True
                else:
                    self.editing = False

            if not self.text:
                self.password = False
                self.text = self.label

            if self.editing and self.text == self.label:
                self.ClearText()
                self.password = True if self.passwordField else False

            if event.type == pygame.KEYDOWN:
                self.cursorVisible = True

                if event.key not in self.keyrepeatCounters:
                    if not event.key == pygame.K_RETURN:
                        self.keyrepeatCounters[event.key] = [0, event.unicode]

                if self.editing:
                    if event.key == pygame.K_BACKSPACE:
                        self.text = (
                            self.text[:max(self.cursorPos - 1, 0)]
                            + self.text[self.cursorPos:]
                        )

                        self.cursorPos = max(self.cursorPos - 1, 0)
                    elif event.key == pygame.K_DELETE:
                        self.text = (
                            self.text[:self.cursorPos]
                            + self.text[self.cursorPos + 1:]
                        )

                    elif event.key == pygame.K_RETURN:
                        return True

                    elif event.key == pygame.K_RIGHT:
                        self.cursorPos = min(
                            self.cursorPos + 1, len(self.text))

                    elif event.key == pygame.K_LEFT:
                        self.cursorPos = max(self.cursorPos - 1, 0)

                    elif event.key == pygame.K_END:
                        self.cursorPos = len(self.text)

                    elif event.key == pygame.K_HOME:
                        self.cursorPos = 0

                    elif len(self.text) < self.maxLen or self.maxLen == -1:
                        self.text = (
                            self.text[:self.cursorPos]
                            + event.unicode
                            + self.text[self.cursorPos:]
                        )
                        self.cursorPos += len(event.unicode)

            elif event.type == pygame.KEYUP:
                if event.key in self.keyrepeatCounters:
                    del self.keyrepeatCounters[event.key]

        for key in self.keyrepeatCounters:
            self.keyrepeatCounters[key][0] += self.clock.get_time()

            if self.keyrepeatCounters[key][0] >= self.keyrepeatInitial:
                self.keyrepeatCounters[key][0] = (
                    self.keyrepeatInitial
                    - self.keyrepeatInterval
                )

                eventKey, eventUnicode = key, self.keyrepeatCounters[key][1]
                pygame.event.post(pygame.event.Event(
                    pygame.KEYDOWN, key=eventKey, unicode=eventUnicode))

        string = self.text
        if self.password:
            string = "*" * len(self.text)
        self.surface = self.font.render(str(string), 1, self.textCol)

        self.cursorCounter += self.clock.get_time()
        if self.cursorCounter >= self.cursorSwitch:
            self.cursorCounter %= self.cursorSwitch
            self.cursorVisible = not self.cursorVisible

        if self.cursorVisible:
            cursorY = self.font.size(self.text[:self.cursorPos])[0]
            if self.cursorPos > 0:
                cursorY -= self.cursorSurf.get_width()
            if self.editing:
                self.surface.blit(self.cursorSurf, (cursorY, 0))

        self.clock.tick()
        return False

    def GetCursorPos(self):
        return self.cursorPos

    def SetTextColor(self, color):
        self.textCol = color

    def SetCursorColor(self, color):
        self.cursor_surface.fill(color)

    def ClearText(self):
        self.text = ""
        self.cursorPos = 0

    def __repr__(self):
        return self.text


class Slider:
    def __init__(self, rectLoc, rectSize, rectCol=(128, 128, 128), circleCol=(255, 255, 255), valRange=(1, 100), initialVal=20, font=None, text=None, textCol=(0, 0, 0), horiz=True):
        """
        Creates a slider with various tweakable parameters.

        :param rectLoc: The (x, y) location of the rectangle underneath the circle.
        :type rectLoc: tuple
        :param rectSize: The (width, height) size of the rectangle underneath the circle.
        :type rectSize: tuple
        :param rectCol: The (R, G, B) color of the rectangle underneath the circle.
        :type rectCol: tuple
        :param circleCol: The (R, G, B) color of the circle above the rectangle.
        :type circleCol: tuple
        :param valRange: A tuple indicating the range of values that the slider can scroll through (min, max).
        :type valRange: tuple
        :param initialVal: The starting value of the slider.
        :type initialVal: int
        :param horiz: A boolean indicating whether or not the slider is horizontal(True) or vertical(False)
        :type horiz: boolean
        """

        self.x, self.y = int(rectLoc[0]), int(rectLoc[1])
        self.width, self.height = int(rectSize[0]), int(rectSize[1])
        self.rectCol, self.circleCol = rectCol, circleCol
        if not (valRange[0] <= initialVal <= valRange[1]):
            raise InputError("PumpkinPy: the initial value is not within the value range")
        self.valRange = valRange[0], valRange[1] + 1
        self.value = initialVal
        self.font, self.text = font, text
        self.textCol = textCol
        self.radius = int(self.height/2) if horiz else int(self.width/2)
        self.radius += 3
        self.horiz = horiz

    def GetValue(self):
        """
        Returns the current value of the slider.

        :return: Current value of the slider
        :rtype: int
        """
        return self.value

    def Draw(self, window):
        """
        Meant to be ran every game loop iteration. Updates and draws the object given window.

        :param window: The window that the slider should be drawn on.
        """
        if pygame.mouse.get_pressed()[0]:
            if pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(pygame.mouse.get_pos()):
                self.value = int(np.interp(pygame.mouse.get_pos()[0], (self.x, self.x + self.width), self.valRange)) if self.horiz else int(
                    np.interp(pygame.mouse.get_pos()[1], (self.y, self.y + self.height), self.valRange))

        pygame.draw.rect(window, self.rectCol, (int(self.x), int(
            self.y), int(self.width), int(self.height)))

        if self.horiz:
            circleX = np.interp(
                self.value, self.valRange, (self.x, self.x + self.width))
            pygame.draw.circle(window, self.circleCol, (int(
                circleX), int(self.y + self.height/2)), int(self.radius))

        else:
            circleY = np.interp(
                self.value, self.valRange, (self.y, self.y + self.height))
            pygame.draw.circle(window, self.circleCol, (int(
                self.x + self.width/2), int(circleY)), int(self.radius))

        if self.font is not None and self.text is not None:
            text = self.font.render(self.text, 1, self.textCol)
            window.blit(text, (int(self.x + self.width/2 -
                                   text.get_width()/2), int(self.y + self.height + 5)))


class BarGraph:
    def __init__(self,
                 loc,
                 size,
                 categories=("Foo", "Bar"),
                 values=(80, 30),
                 graphColor=(0, 0, 0),
                 font=pygame.font.SysFont("comicsans", 20),
                 yaxisRot=0,
                 xaxisRot=0,
                 gap=5,
                 adjust=100,
                 widthScale=1,
                 heightScale=1,
                 horiz=False):

        self.x, self.y = loc[0], loc[1]
        self.width, self.height = size[0], size[1]

        if len(categories) != len(values):
            raise InputError("PumpkinPy: the length of the categories should equal the length of the values")
        self.categories, self.values = categories, values

        if horiz:
            self.catWidth = (self.height - adjust - len(categories)
                             * gap)//len(categories) * widthScale
        else:
            self.catWidth = (self.width - adjust - len(categories)
                             * gap)//len(categories) * widthScale
        self.gap, self.adjust = gap, adjust
        self.font = font
        self.yaxisRot, self.xaxisRot = yaxisRot, xaxisRot
        self.graphColor = graphColor
        self.widthScale, self.heightScale = widthScale, heightScale
        self.horiz = horiz
        self.surf = pygame.Surface(size, pygame.SRCALPHA)
        self._CreateSurf()

    def GetSurf(self):
        return self.surf

    def _CreateSurf(self):
        self.surf.fill((0, 0, 0, 0))
        gap = self.catWidth
        for i in range(len(self.categories)):
            color = (random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255))
            while sum(color) < 120:
                color = (random.randint(0, 255), random.randint(
                    0, 255), random.randint(0, 255))
            if self.horiz:
                pygame.draw.rect(self.surf, color, (5 + self.adjust, gap*i*self.widthScale +
                                                    i*self.gap, self.values[i]*self.heightScale, self.catWidth))
                text = self.font.render(self.categories[i], 1, self.graphColor)
                self.surf.blit(pygame.transform.rotate(
                    text, self.yaxisRot), (self.x, gap*i*self.widthScale + i*self.gap + self.catWidth//2))
                text = self.font.render(
                    str(self.values[i]), 1, self.graphColor)
                self.surf.blit(text, (5 + self.adjust + self.values[i]*self.heightScale//2 - text.get_width(
                )//2, gap*i*self.widthScale + i*self.gap + self.catWidth//2 - text.get_height()//2))

            else:
                pygame.draw.rect(self.surf, color, (5 + self.adjust + gap*i*self.widthScale + i*self.gap, self.height -
                                                    5 - self.adjust - self.values[i]*self.heightScale, self.catWidth, self.values[i]*self.heightScale))
                text = self.font.render(self.categories[i], 1, self.graphColor)
                self.surf.blit(pygame.transform.rotate(text, self.xaxisRot), (5 + self.adjust + gap*i *
                                                                              self.widthScale + i*self.gap + self.catWidth//2 - text.get_width()//2, self.height - 5 - self.adjust + 10))
                text = self.font.render(
                    str(self.values[i]), 1, self.graphColor)
                self.surf.blit(text, (5 + self.adjust + gap*i*self.widthScale + i*self.gap + self.catWidth //
                                      2 - text.get_width()//2, self.height - 5 - self.adjust - self.values[i]*self.heightScale//2 - text.get_height()//2))

        self._CreateGraph()

    def _CreateGraph(self):
        pygame.draw.rect(self.surf, self.graphColor,
                         (self.adjust, 0, 5, self.height - self.adjust))
        pygame.draw.rect(self.surf, self.graphColor, (self.adjust,
                                                      self.height - 5 - self.adjust, self.width - self.adjust, 5))

    def Draw(self, window):
        window.blit(self.surf, (self.x, self.y))


class ColorPicker:
    def __init__(self, wheelPos, wheelRad, sliderPos, sliderSize, sliderHoriz, sliderInvert, cursorRad, displayRectLoc, displayRectSize=(150, 150)):
        self.wheelPos, self.wheelRad = wheelPos, wheelRad
        self.sliderPos, self.sliderSize, self.sliderHoriz, self.sliderInvert = sliderPos, sliderSize, sliderHoriz, sliderInvert
        self.cursorRad = cursorRad
        self.displayRectLoc, self.displayRectSize = displayRectLoc, displayRectSize
        self.wheelCursor, self.sliderCursor = list((wheelPos[0] - cursorRad, wheelPos[1] - cursorRad)), list(
            (sliderPos[0] + sliderSize[0]//2 - cursorRad, sliderPos[1] + sliderSize[1]//2 - cursorRad))
        self.sliderSurf = pygame.Surface(sliderSize)
        self.wheelSurf = pygame.transform.scale(
            pygame.image.load("color_picker.png"), (wheelRad*2,)*2)
        self.cursorSurf = pygame.Surface(
            (self.cursorRad*2,)*2, pygame.SRCALPHA)
        self.wheelDarken = pygame.Surface((wheelRad*2,)*2, pygame.SRCALPHA)
        self._CreateWheel()
        self._CreateSlider()
        self._CreateCursor()
        self._UpdateWheel()

    def Draw(self, window):
        pygame.draw.rect(window, self.GetRGB(),
                         (*self.displayRectLoc, *self.displayRectSize))
        window.blit(self.sliderSurf, self.sliderPos)
        window.blit(self.cursorSurf, self.sliderCursor)
        window.blit(
            self.wheelSurf, (self.wheelPos[0] - self.wheelRad, self.wheelPos[1] - self.wheelRad))
        window.blit(
            self.wheelDarken, (self.wheelPos[0] - self.wheelRad, self.wheelPos[1] - self.wheelRad))
        window.blit(self.cursorSurf, self.wheelCursor)

    def Update(self, window):
        self.Draw(window)
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            if ((self.wheelPos[0] - x)**2 + (self.wheelPos[1] - y)**2)**0.5 < self.wheelRad - 2:
                self.wheelCursor = (x - self.cursorRad, y - self.cursorRad)
            elif self.sliderPos[0] < x < self.sliderPos[0] + self.sliderSize[0] and self.sliderPos[1] < y < self.sliderPos[1] + self.sliderSize[1]:
                self.sliderCursor[1] = y - self.cursorRad
                self._UpdateWheel()

    def GetRGB(self):
        wrgb = self.wheelSurf.get_at((self.wheelCursor[0] - self.wheelPos[0] + self.cursorRad +
                                      self.wheelRad, self.wheelCursor[1] - self.wheelPos[1] + self.cursorRad + self.wheelRad))
        srgb = self.sliderSurf.get_at(
            (self.sliderCursor[0] - self.sliderPos[0] + self.cursorRad, self.sliderCursor[1] - self.sliderPos[1] + self.cursorRad))
        whsv = rgb_to_hsv(*(np.array(wrgb)/255)[:3])
        shsv = rgb_to_hsv(*(np.array(srgb)/255)[:3])
        hsv = (whsv[0], whsv[1], shsv[2])
        rgb = np.array(hsv_to_rgb(*hsv))*255
        return rgb

    def GetHSV(self):
        rgb = (np.array(self.GetRGB())/255)[:3]
        return np.array(rgb_to_hsv(*rgb))*255

    def _UpdateWheel(self):
        pygame.draw.circle(self.wheelDarken, (0, 0, 0, np.interp(
            self.GetHSV()[2], (0, 255), (255, 0))), (self.wheelRad,)*2, self.wheelRad)

    def _CreateWheel(self):
        pygame.draw.circle(self.wheelSurf, (0, 0, 0),
                           (self.wheelRad,)*2, self.wheelRad, 2)

    def _CreateSlider(self):
        w, h = self.sliderSize
        if self.sliderHoriz:
            for x in range(w):
                if self.sliderInvert:
                    value = np.interp(x, (0, w), (0, 255))
                else:
                    value = np.interp(x, (0, w), (255, 0))
                pygame.draw.rect(self.sliderSurf, (value,)*3, (x, 0, 1, h))

        else:
            for y in range(h):
                if self.sliderInvert:
                    value = np.interp(y, (0, h), (0, 255))
                else:
                    value = np.interp(y, (0, h), (255, 0))
                pygame.draw.rect(self.sliderSurf, (value,)*3, (0, y, w, 1))
        pygame.draw.rect(self.sliderSurf, (0, 0, 0), (0, 0, w, h), 1)

    def _CreateCursor(self):
        self.cursorSurf.fill((0, 0, 0, 0))
        pygame.draw.circle(self.cursorSurf, (255, 255, 255),
                           (self.cursorRad,)*2, self.cursorRad)
        pygame.draw.circle(self.cursorSurf, (0, 0, 0),
                           (self.cursorRad,)*2, self.cursorRad, 2)


class Checkbox:
    def __init__(self, loc, size, checkCol=(0, 0, 0), padding=5, text="Checkbox", font=pygame.font.SysFont("comicsans", 80)):
        self.loc, self.size = loc, size
        self.text = text
        self.font = font
        self.color = checkCol
        self.padding = padding
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(os.path.realpath(os.path.dirname(__file__)), "checkmark.png")), (size[0] - padding*2, size[1] - padding*2))
        self.checked = False
        if checkCol != (0,)*3:
            self.ChangeCheckColor(checkCol)

    def Draw(self, window, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(*self.loc, *self.size).collidepoint(event.pos):
                    self.checked = not self.checked

        pygame.draw.rect(window, (0, 0, 0), (*self.loc, *self.size), 3)
        text = self.font.render(self.text, 1, (0, 0, 0))
        window.blit(text, (self.loc[0] + self.size[0] + 5, self.loc[1] + self.size[1]//2 - text.get_height()//2))
        if self.checked:
            window.blit(self.image, (self.loc[0] + self.padding, self.loc[1] + self.padding))

    def ChangeCheckColor(self, color):
        w, h = self.image.get_size()
        for x in range(w):
            for y in range(h):
                if self.image.get_at((x, y))[3] != 0:
                    self.image.set_at((x, y), color)


class Dropdown:
    def __init__(self, loc, size, initialText, popSize, choices, font, color, highlightCol):
        self.loc, self.size = loc, size
        self.initialText = initialText
        self.popSize = popSize
        self.choices = choices
        self.font = font
        self.color = color
        self.highlightCol = highlightCol