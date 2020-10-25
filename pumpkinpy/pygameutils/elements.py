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

pygame.init()

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

    def Draw(self, window, events):
        """
        Draws button on a window.
        :param window: Pygame window object to draw on.
        :param events: Events obtained from pygame.events.get()
        """
        pygame.draw.rect(window, self.currBgCol, self.loc + self.size)
        window.blit(self.text, self.textLoc)
        if self.border:
            pygame.draw.rect(window, self.borderCol, self.loc+self.size, self.borderWidth)

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
    def __init__(self, loc, size, bgCol, borderWidth=5, borderCol=(0, 0, 0), initialText="", label="", font=pygame.font.SysFont("comicsans", 35), \
        textCol=(0, 0, 0), cursorCol=(0, 0, 1), repeatInitial=400, repeatInterval=35, maxLen=-1, password=False, editing=False):
        """
        Input text class for Pygame.
        :param loc: Pixel location (x, y).
        :param size: Pixel size (x, y).
        :param bgCol: Background color (RGB).
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

        self.cursorSurf = pygame.Surface((int(font.get_height() / 20 + 1), font.get_height()))
        self.cursorSurf.fill(cursorCol)
        self.cursorPos = len(initialText)
        self.cursorVisible = True
        self.cursorSwitch = 500
        self.cursorCounter = 0

        self.clock = pygame.time.Clock()

    def Draw(self, window, events):
        pygame.draw.rect(window, self.bgCol, self.rect)
        if self.borderWidth:
            pygame.draw.rect(window, self.borderCol, self.rect, self.borderWidth)

        textPos = (int(self.loc[0] + self.size[0]//2 - self.surface.get_width()/2), int(self.loc[1] + self.size[1]//2 - self.surface.get_height()/2))
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
                        self.cursorPos = min(self.cursorPos + 1, len(self.text))

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
                pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=eventKey, unicode=eventUnicode))

        string = self.text
        if self.password:
            string = "*" * len(self.text)
        self.surface = self.font.render(string, 1, self.textCol)

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
    def __init__(self):
        """
        Creates a slider with various tweakable parameters.
        """
        pass