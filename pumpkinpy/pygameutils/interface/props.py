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

def BoolProp(name="", description="", default=False):
    return {"type": "bool", "name": name, "description": description, "default": default}


def IntProp(name="", description="", default: int = 0, **kwargs):
    final = {"type": "int", "name": name,
             "description": description, "default": default}

    if "min" in kwargs:
        minimum = kwargs["min"]
        if minimum > default:
            raise ValueError("Minimum is greater than default.")
        final["min"] = minimum

        if "soft_min" in kwargs:
            soft_min = kwargs["soft_min"]
            if soft_min < minimum:
                raise ValueError("Soft minimum is less than minimum.")
            final["soft_min"] = soft_min

    if "max" in kwargs:
        maximum = kwargs["max"]
        if maximum < default:
            raise ValueError("Maximum is smaller than default.")
        final["max"] = maximum

        if "soft_max" in kwargs:
            soft_max = kwargs["soft_max"]
            if soft_max > maximum:
                raise ValueError("Soft maximum is greater than maximum.")
            final["soft_max"] = soft_max

    return final


def FloatProp(name="", description="", default: int = 0, **kwargs):
    final = {"type": "float", "name": name,
             "description": description, "default": default}

    if "min" in kwargs:
        minimum = kwargs["min"]
        if minimum > default:
            raise ValueError("Minimum is greater than default.")
        final["min"] = minimum

        if "soft_min" in kwargs:
            soft_min = kwargs["soft_min"]
            if soft_min < minimum:
                raise ValueError("Soft minimum is less than minimum.")
            final["soft_min"] = soft_min

    if "max" in kwargs:
        maximum = kwargs["max"]
        if maximum < default:
            raise ValueError("Maximum is smaller than default.")
        final["max"] = maximum

        if "soft_max" in kwargs:
            soft_max = kwargs["soft_max"]
            if soft_max > maximum:
                raise ValueError("Soft maximum is greater than maximum.")
            final["soft_max"] = soft_max

    return final


def StringProp(name="", description="", default="", maxLen=0):
    return {"type": "str", "name": name, "description": description, "default": default, "maxLen": maxLen}
