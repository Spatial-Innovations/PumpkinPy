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

import os
import sys
from tkinter import Tk
from tkinter.filedialog import askdirectory

Tk().withdraw()
print("Select python directory to install PumpkinPy. You need to remove an existing version, if applicable.")
directory = askdirectory()

if directory == "":
    sys.exit()
if not directory.endswith("pumpkinpy"):
    directory = os.path.join(directory, "pumpkinpy")

if os.path.isdir(directory):
    input(f"Directory already exists: {directory}")
    sys.exit()

os.system(f"git clone https://github.com/Spatial-Innovations/PumpkinPy.git {directory}")
input("Pumpkinpy is installed. You can also contribute, as a Github repository was cloned.")