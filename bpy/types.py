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

class Layout:
    def prop():
        pass
    def separator():
        pass
    def operator():
        pass

class Object:
    location = (0, 0, 0)
    rotation = (0, 0, 0)
    scale = (0, 0, 0)
    name = ""
    pass_index = 0
    data = None
    
    def keyframe_insert(self, data_path, index=-1, frame=0, group="", options=set()):
        pass

class Scene:
    pass

class Panel:
    layout = Layout()

class Operator:
    layout = Layout()
    
class PropertyGroup:
    pass