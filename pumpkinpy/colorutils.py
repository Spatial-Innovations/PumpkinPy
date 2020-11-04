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

from colorsys import *
import numpy as np


def RGBToHSV(rgb):
    rgb = np.array(rgb)/255
    hsv = np.array(rgb_to_hsv(rgb))*255
    return hsv


def RGBToHLS(rgb):
    rgb = np.array(rgb)/255
    hls = np.array(rgb_to_hls(rgb))*255
    return hls


def RGBToYIQ(rgb):
    rgb = np.array(rgb)/255
    yiq = np.array(rgb_to_yiq(rgb))*255
    return yiq


def HSVToRGB(hsv):
    hsv = np.array(hsv)/255
    rgb = np.array(hsv_to_rgb(hsv))*255
    return rgb


def HSVToYIQ(hsv):
    rgb = HSVToRGB(hsv)
    return RGBToYIQ(rgb)


def HSVToHLS(hsv):
    rgb = HSVToRGB(hsv)
    return RGBToHLS(rgb)


def YIQToRGB(yiq):
    yiq = np.array(yiq)/255
    rgb = np.array(yiq_to_rgb(yiq))*255
    return rgb


def YIQToHSV(yiq):
    rgb = YIQToRGB(yiq)
    return RGBToHSV(rgb)


def YIQToHLS(yiq):
    rgb = YIQToRGB(yiq)
    return RGBToHLS(rgb)


def HLSToRGB(hls):
    hls = np.array(hls)/255
    rgb = np.array(hls_to_rgb(hls))*255
    return rgb


def HLSToHSV(hls):
    rgb = HLSToRGB(hls)
    return RGBToHSV(rgb)


def HLSToYIQ(hls):
    rgb = HLSToRGB(hls)
    return RGBToYIQ(rgb)
