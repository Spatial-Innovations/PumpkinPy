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

import pygame
import random
import math

pygame.init()


class _Ball:
    def __init__(self, loc, radius, velocity, color):
        self.x, self.y = loc
        self.direction = random.randint(0, 360)
        self.color = color
        self.radius = radius
        self.velocity = velocity

    def Draw(self, window):
        pygame.draw.circle(window, self.color, (round(self.x), round(self.y)), self.radius)

    def Move(self):
        self.x += self.velocity * math.sin(math.radians(self.direction))
        self.y -= self.velocity * math.cos(math.radians(self.direction))


class BallBackground:
    def __init__(self, scene, numBalls, radiusRange, velocityRange):
        """
        Creates a background which is interactive and colorful

        :param scene: A tuple containing (x, y, width, height), this determines where the background will take place
        :param numBalls: The number of balls in the background
        :param radiusRange: A tuple which contains the min and max values of a balls' radius
        :param velocityRange: A tuple which contains the min and max values of a balls' velocity
        """
        self.scene = scene
        self.numBalls = numBalls
        self.radiusRange, self.velocityRange = radiusRange, velocityRange
        self.balls = []
        self.CreateBalls()


    def Update(self, window, events):
        """
        This method is meant to be run every iteration of the gameloop.
        It updates the whole background.
        :param window: The pygame window
        :param events: The events of the window (pygame.event.get())
        """
        for ball in self.balls:
            ball.Move()
            ball.Draw(window)

        self.DestroyBalls()
        self.AddBalls(events)


    def CreateBalls(self):
        """
        Creates the first set of balls
        """
        for _ in range(self.numBalls):
            self.balls.append(_Ball((random.randint(self.scene[0], self.scene[2]), random.randint(self.scene[1], self.scene[3])),
                                    random.randint(*self.radiusRange),
                                    random.randint(*self.velocityRange),
                                    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))


    def DestroyBalls(self):
        """
        Destroys the balls that have gone outside of the boundary.
        It also adds the number of balls it has destroyed to maintain stability.
        """
        rem = []

        for ball in self.balls:
            if ball.x - ball.radius > self.scene[2]:
                rem.append(ball)
            elif ball.x + ball.radius < self.scene[0]:
                rem.append(ball)
            elif ball.y - ball.radius > self.scene[3]:
                rem.append(ball)
            elif ball.y + ball.radius < self.scene[1]:
                rem.append(ball)

        for r in rem:
            self.balls.remove(r)
            self.balls.append(_Ball((random.randint(self.scene[0], self.scene[2]), random.randint(self.scene[1], self.scene[3])),
                                    random.randint(*self.radiusRange),
                                    random.randint(*self.velocityRange),
                                    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))


    def AddBalls(self, events):
        """
        Adds more balls if you have clicked or scrolled.
        And removes the extra ones to maintain stability.
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.balls.append(_Ball((pygame.mouse.get_pos()),
                                        random.randint(*self.radiusRange),
                                        random.randint(*self.velocityRange),
                                       (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))
                self.balls.pop(0)

