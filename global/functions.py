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

def ClearConsole():
    """
    Clears the program console.
    :return: None
    """

    import os
    os.system("cls")


def ChooseFile(startPath=None):
    """
    Uses tkinter to choose a file with a file browser.
    :param startPath=None: Starting path of file browser
    :return: None
    """

    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    
    Tk().withdraw()
    return askopenfilename(startPath)