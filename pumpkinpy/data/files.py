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
import zlib

def Compress(path):
    """
    Compresses a file with zlib compression, then stores to path + "_comp".
    :param path: Path of file to compress (works best with text files).
    """
    with open(path, "rb") as file:
        uncompressed = file.read()
    
    parts = os.path.split(path)
    newPath = os.path.join(os.path.dirname(path), os.path.dirname(parts[0])+"_comp", parts[1])
    with open(newPath, "wb") as file:
        file.write(zlib.compress(uncompressed))