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

from PIL import Image
import os


def JpgToPng(imagePath, replaceFile=False):
    image = Image.open(imagePath)
    if replaceFile:
        image.save(imagePath.replace(".jpg", ".png"))
    else:
        fileName, fileExt = os.path.splitext(imagePath)
        fileName += "_ppy"
        fileExt = ".png"
        imagePath = fileName + fileExt
        image.save(imagePath)


def PngToJpg(imagePath, replaceFile=False):
    image = Image.open(imagePath).convert(mode="RGB")
    if replaceFile:
        image.save(imagePath.replace(".png", ".jpg"))
    else:
        fileName, fileExt = os.path.splitext(imagePath)
        fileName += "_ppy"
        fileExt = ".jpg"
        imagePath = fileName + fileExt
        image.save(imagePath)
