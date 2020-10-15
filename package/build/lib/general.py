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

import os

def ClearConsole():
    """
    Clears the program console.
    :return: None
    """

    os.system("cls")


def Encrypt(text):
    """
    Applies a simple encryption to a string. Note: This is very easy to decrypt by using this module.
    :param text: Text to encrypt.
    :return: class str, encrypted text.
    """

    chars1 = "Sisw[*mWkb,0R;VCtK&:5-/Yo\"Oql_\\(1>I+L^\'?9vT$aU3!6.z7nAJ<g}dM=Hx#hFp~QyeX)fj|Z]`urcBN84GE@%DP2{"
    chars2 = "!GN:r2>s#?i%@,=}7dwP/b^<a\\M)U`cmLQ&hBp{y\"EKRvxXo(qFWIS.|DtA\'5*ln8;f+ZTeOJ$9zu-k4Y0CHg_V~1][6j3"
    
    final = ""
    for c in text:
        final += chars1[chars2.index(c)]

    return final


def Decrypt(text):
    """
    Decrypts text encrypted with pumpkinpy.global.functions.Encrypt().
    :param text: Text to decrypt.
    :return: class str, decrypted text.
    """

    chars1 = "Sisw[*mWkb,0R;VCtK&:5-/Yo\"Oql_\\(1>I+L^\'?9vT$aU3!6.z7nAJ<g}dM=Hx#hFp~QyeX)fj|Z]`urcBN84GE@%DP2{"
    chars2 = "!GN:r2>s#?i%@,=}7dwP/b^<a\\M)U`cmLQ&hBp{y\"EKRvxXo(qFWIS.|DtA\'5*ln8;f+ZTeOJ$9zu-k4Y0CHg_V~1][6j3"
    
    final = ""
    for c in text:
        final += chars2[chars1.index(c)]

    return final