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
import numpy as np


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


def ChangeColorCount(imagePath, colorCount, replaceFile=False):
    image = Image.open(imagePath).convert("RGB")
    pixels = np.array(image)

    width, height = image.size
    for x in range(height):
        for y in range(width):
            try:
                pixel = pixels[x][y]
                r, g, b = pixel

                try:
                    r = round(r * colorCount / 255) * (255 / colorCount)
                    g = round(g * colorCount / 255) * (255 / colorCount)
                    b = round(b * colorCount / 255) * (255 / colorCount)

                except ZeroDivisionError:
                    pass

                pixels[x][y] = (r, g, b)

            except IndexError:
                pass

    image = Image.fromarray(pixels)

    if replaceFile:
        image.save(imagePath)
    else:
        fileName, fileExt = os.path.splitext(imagePath)
        fileName += "_ppy"
        imagePath = fileName + fileExt
        image.save(imagePath)


def Dither(imagePath, factor, replaceFile=False):
    image = Image.open(imagePath).convert("RGB")
    image.thumbnail((800, 800))
    pixels = np.array(image, dtype=np.float64)

    width, height = image.size
    for x in range(height):
        for y in range(width):
            try:
                pixel = pixels[x][y]
                r, g, b = pixel

                try:
                    newR = round(r * factor / 255) * (255 / factor)
                    newG = round(g * factor / 255) * (255 / factor)
                    newB = round(b * factor / 255) * (255 / factor)

                except ZeroDivisionError:
                    pass

                errR, errG, errB = r - newR, g - newG, b - newB

                pixels[x + 1][y    ] += (errR * 7/16, errG * 7/16, errB * 7/16)
                pixels[x - 1][y + 1] += (errR * 3/16, errG * 3/16, errB * 3/16)
                pixels[x    ][y + 1] += (errR * 5/16, errG * 5/16, errB * 5/16)
                pixels[x + 1][y + 1] += (errR * 1/16, errG * 1/16, errB * 1/16)

            except IndexError:
                pass

    image = Image.fromarray(pixels)
    image.show()

    # if replaceFile:
    #     image.save(imagePath)
    # else:
    #     fileName, fileExt = os.path.splitext(imagePath)
    #     fileName += "_ppy"
    #     imagePath = fileName + fileExt
    #     image.save(imagePath)


Dither(os.path.join(os.path.realpath(os.path.dirname(__file__)), "Cave.png"), 2)