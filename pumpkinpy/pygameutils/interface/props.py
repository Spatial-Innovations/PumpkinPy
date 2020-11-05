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

def BoolProp(name: str = "", description: str = "", default: bool = False) -> dict:
    return {"type": "bool", "name": name, "description": description, "default": default}


def IntProp(name: str = "", description: str = "", default: int = 0, **kwargs) -> dict:
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


def FloatProp(name: str = "", description: str = "", default: int = 0, **kwargs) -> dict:
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


def StringProp(name: str = "", description: str = "", default: str = "", maxLen: int = 0) -> dict:
    return {"type": "str", "name": name, "description": description, "default": default, "maxLen": maxLen}


def EnumProp(name: str = "", description: str = "", items: list = "", expand: bool = False) -> dict:
    return {"name": name, "description": description, "items": items, "expand": expand}
