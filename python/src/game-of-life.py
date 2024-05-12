"""Conway's Game of Life

- Living cells with 2 or 3 neighbors stay alive in the next step of the simulation.
- Dead cells with exactly three neighbors become alive in the next step of the simulation.
- Any other cell dies or stays dead in the next step of the simulation.

"""

import random

# Imports go at the top
from microbit import *


class Life:
    STATIC: bool = False
    WRAP: bool = True

    ALIVE: int = 9
    DEAD: int = 0

    WIDTH: int = 5
    HEIGHT: int = 5

    def __init__(self) -> None:
        self.alive: int = 0

        # x, y, on/off
        dot: "tuple[int, int, int]" = (0, 0, self.DEAD)

        self.grid: "list[list[tuple[int, int, int]]]" = [
            [dot, dot, dot, dot, dot],
            [dot, dot, dot, dot, dot],
            [dot, dot, dot, dot, dot],
            [dot, dot, dot, dot, dot],
            [dot, dot, dot, dot, dot],
        ]

    def setup(self) -> None:
        display.clear()

        self.alive = 0

        for row in range(0, self.HEIGHT):
            for col in range(0, self.WIDTH):
                if self.STATIC:
                    self.set_dot(row, col, self.DEAD)
                elif random.randint(0, 2) == 1:
                    self.set_dot(row, col, self.ALIVE)
                    self.alive += 1
                else:
                    self.set_dot(row, col, self.DEAD)

        if self.STATIC:
            self.set_dot(0, 2, self.ALIVE)
            self.set_dot(1, 2, self.ALIVE)
            self.set_dot(2, 2, self.ALIVE)
            self.set_dot(3, 2, self.ALIVE)
            self.set_dot(4, 2, self.ALIVE)

            self.set_dot(2, 0, self.ALIVE)
            self.set_dot(2, 1, self.ALIVE)
            self.set_dot(2, 2, self.ALIVE)
            self.set_dot(2, 3, self.ALIVE)
            self.set_dot(2, 4, self.ALIVE)

            self.set_dot(0, 0, self.ALIVE)
            self.set_dot(1, 1, self.ALIVE)
            self.set_dot(2, 2, self.ALIVE)
            self.set_dot(3, 3, self.ALIVE)
            self.set_dot(4, 4, self.ALIVE)

            self.set_dot(4, 0, self.ALIVE)
            self.set_dot(3, 1, self.ALIVE)
            self.set_dot(2, 2, self.ALIVE)
            self.set_dot(1, 3, self.ALIVE)
            self.set_dot(0, 4, self.ALIVE)

        print("INFO: left alive: " + str(self.alive))

    def redraw(self) -> None:
        for row in self.grid:
            for cell in row:
                display.set_pixel(*cell)

    def set_dot(self, x: int, y: int, state: int) -> None:
        self.grid[x][y] = (x, y, state)

    def evolve(self) -> None:
        self.alive = 0

        # x, y, on/off
        dot: "tuple[int, int, int]" = (0, 0, self.DEAD)

        next_grid: "list[list[tuple[int, int, int]]]" = [
            [dot, dot, dot, dot, dot],
            [dot, dot, dot, dot, dot],
            [dot, dot, dot, dot, dot],
            [dot, dot, dot, dot, dot],
            [dot, dot, dot, dot, dot],
        ]

        for row in range(0, self.HEIGHT):
            for col in range(0, self.WIDTH):
                if self.WRAP:
                    left = (col - 1) % self.WIDTH
                    right = (col + 1) % self.WIDTH
                    above = (row - 1) % self.HEIGHT
                    below = (row + 1) % self.HEIGHT
                else:
                    if col - 1 < 0:
                        left = 0
                    else:
                        left = col - 1

                    if col + 1 >= self.WIDTH:
                        right = 4
                    else:
                        right = col + 1

                    if row - 1 < 0:
                        above = 0
                    else:
                        above = row - 1

                    if row + 1 >= self.HEIGHT:
                        below = 4
                    else:
                        below = row + 1

                count: int = 0

                if self.grid[left][above][2] == self.ALIVE:
                    count += 1
                if self.grid[col][above][2] == self.ALIVE:
                    count += 1
                if self.grid[right][above][2] == self.ALIVE:
                    count += 1
                if self.grid[left][col][2] == self.ALIVE:
                    count += 1
                if self.grid[right][col][2] == self.ALIVE:
                    count += 1
                if self.grid[left][below][2] == self.ALIVE:
                    count += 1
                if self.grid[row][below][2] == self.ALIVE:
                    count += 1
                if self.grid[right][below][2] == self.ALIVE:
                    count += 1

                if self.grid[row][col][2] == self.ALIVE and count in [2, 3]:
                    next_grid[row][col] = (row, col, self.ALIVE)
                    self.alive += 1
                elif self.grid[row][col][2] == self.DEAD and count == 3:
                    next_grid[row][col] = (row, col, self.ALIVE)
                    self.alive += 1
                else:
                    next_grid[row][col] = (row, col, self.DEAD)

        self.grid = next_grid.copy()

        print("INFO: left alive: " + str(self.alive))


dot: "tuple[int, int, int]" = (0, 0, 0)

life: Life = Life()
life.setup()

# Code in a 'while True:' loop repeats forever
while True:
    print("INFO: grid=" + str(life.grid))
    print()

    life.redraw()

    sleep(1000)

    life.evolve()

    if life.alive <= 1:
        display.show(Image.NO)
        sleep(2000)
        life.setup()
