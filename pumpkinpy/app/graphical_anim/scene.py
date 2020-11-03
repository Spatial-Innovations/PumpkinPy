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
import sys
import shutil
import numpy
import pygame
import cv2
from PIL import Image
from .errors import ExportError


class Scene2D:
    def __init__(self, resolution, fps):
        """
        Initializes 2D scene.
        :param resolution: Reesolution (x, y) pixels of final video.
        :param fps: Frames per second of final video.
        """
        self.res = resolution
        self.fps = fps
        self.layers = []

    def __repr__(self):
        return f"""StrawberryPy Scene object:
Resolution: {self.res}
Fps: {self.fps}
{len(self.layers)} Layers"""

    def AddLayer(self, layer):
        """
        Append a layer to the layer list.
        :param layer: Layer object to append.
        """
        self.layers.append(layer)

    def Render(self):
        surface = pygame.Surface(self.res)
        for l in self.layers:
            surface.blit(l.Render(self.res), (0, 0))

        pixels = []
        for y in range(self.res[1]):
            pixels.append([])
            for x in range(self.res[0]):
                pixels[y].append(surface.get_at((x, y)))

        return [pixels]

    def Export(self, path):
        """
        Exports into a video file.
        :param path: Path of final video.
        """
        # Check extension
        if not path.endswith(".mp4"):
            raise ExportError("StrawberryPy: Only .mp4 files are allowed.")

        print(f"Exporting to {path}")
        # Initialize directory
        PARENT = os.path.dirname(__file__)
        tmpDir = os.path.join(PARENT, "tmp")
        print(f"Step 1/4: Create tmp directory: {tmpDir}")
        os.makedirs(tmpDir, exist_ok=True)

        # Save images to frames
        print("Step 2/4: Saving images to tmp directory.")
        for i, frame in enumerate(self.Render()):
            pixels = numpy.array(frame, dtype=numpy.uint8)
            Image.fromarray(pixels).save(
                os.path.join(PARENT, "tmp", f"{i}.png"))

        # Compile into video
        print("Step 3/4: Compiling video")
        images = [img for img in os.listdir(tmpDir)]
        frame = cv2.imread(os.path.join(tmpDir, images[0]))
        height, width, layers = frame.shape
        video = cv2.VideoWriter(path, 0, self.fps, (width, height))
        for img in images:
            video.write(cv2.imread(os.path.join(tmpDir, img)))

        video.release()

        # Clean up
        print("Step 4/4: Clean up")
        cv2.destroyAllWindows()
        shutil.rmtree(tmpDir)


class Layer:
    def __init__(self):
        self.shapes = []

    def __repr__(self):
        return f"""StrawberryPy Layer object:
Shapes: {len(self.shapes)}"""

    def Add(self, shape):
        self.shapes.append(shape)

    def Render(self, resolution):
        surface = pygame.Surface(resolution)
        for s in self.shapes:
            s.Draw(surface)

        return surface
