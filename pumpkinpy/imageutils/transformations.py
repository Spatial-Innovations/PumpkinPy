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


def Resize(imagePath, newSize, replaceFile=False) -> None:
    image = Image.open(imagePath)
    image.thumbnail(newSize)

    if replaceFile:
        image.save(imagePath)
    else:
        fileName, fileExt = os.path.splitext(imagePath)
        fileName += "_ppy"
        imagePath = fileName + fileExt
        image.save(imagePath)


def Rotate(imagePath, rotation, replaceFile=False) -> None:
    image = Image.open(imagePath)
    image = image.rotate(-rotation)

    if replaceFile:
        image.save(imagePath)
    else:
        fileName, fileExt = os.path.splitext(imagePath)
        fileName += "_ppy"
        imagePath = fileName + fileExt
        image.save(imagePath)


def Crop(imagePath, leftBound, topBound, rightBound, bottomBound, replaceFile=False) -> None:
    image = Image.open(imagePath)
    image = image.crop((leftBound, topBound, rightBound, bottomBound))

    if replaceFile:
        image.save(imagePath)
    else:
        fileName, fileExt = os.path.splitext(imagePath)
        fileName += "_ppy"
        imagePath = fileName + fileExt
        image.save(imagePath)


def FlipLeftRight(imagePath, replaceFile=False) -> None:
    image = Image.open(imagePath)
    image = image.transpose(Image.FLIP_LEFT_RIGHT)

    if replaceFile:
        image.save(imagePath)
    else:
        fileName, fileExt = os.path.splitext(imagePath)
        fileName += "_ppy"
        imagePath = fileName + fileExt
        image.save(imagePath)


def FlipTopBottom(imagePath, replaceFile=False) -> None:
    image = Image.open(imagePath)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)

    if replaceFile:
        image.save(imagePath)
    else:
        fileName, fileExt = os.path.splitext(imagePath)
        fileName += "_ppy"
        imagePath = fileName + fileExt
        image.save(imagePath)
