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

def BoolProperty(name="", description="", default=False):
    pass
def BoolVectorProperty(name="", description="", default=(False, False, False), size=3):
    pass
def IntProperty(name="", description="", default=0):
    pass
def IntVectorProperty(name="", description="", default=(0, 0, 0), size=3):
    pass
def FloatProperty(name="", description="", default=0):
    pass
def FloatVectorProperty(name="", description="", default=(0, 0, 0), size=3):
    pass
def StringProperty(name="", description="", default=""):
    pass
def EnumProperty(name="", description="", items=[]):
    pass
def PointerProperty(type=None):
    pass
def CollectionProperty():
    pass
def RemoveProperty():
    pass