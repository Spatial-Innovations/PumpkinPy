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

scene = None
object = None

selectable_objects = []
selected_bones = []
selected_editable_bones = []
selected_editable_fcurves = []
selected_editable_objects = []
selected_editable_sequences = []
selected_nla_strips = []
selected_objects = []
selected_pose_bones = []
selected_pose_bones_from_active_object = []
selected_sequences = []
selected_visible_fcurves = []


class preferences:
    class addons:
        def get(key, default=None):
            pass
