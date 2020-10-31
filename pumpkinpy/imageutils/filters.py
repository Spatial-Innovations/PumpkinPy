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

from PIL import Image, ImageFilter, ImageEnhance
import os


def Grayscale(imagePath, replaceFile=False):
    image = Image.open(imagePath)
    image = image.convert(mode="L")
    if replaceFile:
        image.save(imagePath)
    else:
        fileName, fileExt = os.path.splitext(imagePath)
        fileName += "_ppy"
        imagePath = fileName + fileExt
        image.save(imagePath)


def GaussianBlur(imagePath, blurRadius, replaceFile=False):
    image = Image.open(imagePath)
    image = Image.filter(ImageFilter.GaussianBlur(blurRadius))

    if replaceFile:
        image.save(imagePath)
    else:
        fileName, fileExt = os.path.splitext(imagePath)
        fileName += "_ppy"
        imagePath = fileName + fileExt
        image.save(imagePath)


def EnhanceColor(imagePath, factor, replaceFile=False):
    image = Image.open(imagePath)
    image = ImageEnhance.Color(image).enhance(factor)

    if replaceFile:
        image.save(imagePath)
    else:
        fileName, fileExt = os.path.splitext(imagePath)
        fileName += "_ppy"
        imagePath = fileName + fileExt
        image.save(imagePath)


def EnhanceContrast(imagePath, factor, replaceFile=False):
    image = Image.open(imagePath)
    image = ImageEnhance.Contrast(image).enhance(factor)

    if replaceFile:
        image.save(imagePath)
    else:
        fileName, fileExt = os.path.splitext(imagePath)
        fileName += "_ppy"
        imagePath = fileName + fileExt
        image.save(imagePath)


def EnhanceBrightness(imagePath, factor, replaceFile=False):
    image = Image.open(imagePath)
    image = ImageEnhance.Brightness(image).enhance(factor)

    if replaceFile:
        image.save(imagePath)
    else:
        fileName, fileExt = os.path.splitext(imagePath)
        fileName += "_ppy"
        imagePath = fileName + fileExt
        image.save(imagePath)


def EnhanceSharpness(imagePath, factor, replaceFile=False):
    image = Image.open(imagePath)
    image = ImageEnhance.Sharpness(image).enhance(factor)

    if replaceFile:
        image.save(imagePath)
    else:
        fileName, fileExt = os.path.splitext(imagePath)
        fileName += "_ppy"
        imagePath = fileName + fileExt
        image.save(imagePath)


def Blend(image1Path, image2Path, factor, replaceFile=False):
    image1 = Image.open(image1Path)
    image2 = Image.open(image2Path)
    image = Image.blend(image1, image2, factor)

    if replaceFile:
        image.save(image1Path)
    else:
        fileName, fileExt = os.path.splitext(image1Path)
        fileName += "_ppy"
        imagePath = fileName + fileExt
        image.save(imagePath)
