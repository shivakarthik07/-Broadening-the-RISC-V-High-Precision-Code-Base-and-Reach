#!/usr/bin/env python3

import os
import time
import random


# game board stuff
WIDTH  = 30
HEIGHT = 15

DELAY = 0.15
GENERATIONS = 200


# --------------------------------------------------
# make first random board
# not really optimized but it works fine tbh
# --------------------------------------------------
def make_grid():

    board = []

    for yy in range(HEIGHT):

        temp_row = []

        for xx in range(WIDTH):

            # randomly alive/dead
            if random.random() < 0.25:
                temp_row.append(1)
            else:
                temp_row.append(0)

        board.append(temp_row)

    return board



# --------------------------------------------------
# checking nearby cells
# Conway rules depend on neighbors obviously
# --------------------------------------------------
def count_neighbors(grid, x, y):

    total = 0

    # maybe later convert this into offsets list?
    # leaving it for now

    for dy in (-1,0,1):

        for dx in (-1,0,1):

            if dx == 0 and dy == 0:
                continue

            nx = (x + dx) % WIDTH
            ny = (y + dy) % HEIGHT

            total = total + grid[ny][nx]

    return total



# next state calculation
# honestly this part took me a second to remember lol
def next_generation(grid):

    newer_grid = []

    for rowY in range(HEIGHT):

        current_row = []

        for colX in range(WIDTH):

            current = grid[rowY][colX]

            neigh = count_neighbors(grid,colX,rowY)

            # alive stays alive
            if current == 1:

                if neigh == 2 or neigh == 3:
                    current_row.append(1)

                else:
                    current_row.append(0)

            else:

                # dead cell reborn
                if neigh == 3:
                    current_row.append(1)

                else:
                    current_row.append(0)

        newer_grid.append(current_row)

    return newer_grid



# --------------------------------------------------
# draw everything to terminal
# --------------------------------------------------
def render(grid , generation):

    # clearing screen depending on OS
    os.system("cls" if os.name == "nt" else "clear")

    print("Conway's Game of Life")
    print("Generation ->", generation)

    print("=" * WIDTH)

    for r in grid:

        txt = ""

        for c in r:

            if c == 1:
                txt += "█"
            else:
                txt += " "

        print(txt)

    print("=" * WIDTH)

    # kinda unnecessary but looks nicer
    print("█ means alive")
    print("space means dead")


# maybe split this later
def main():

    game_grid = make_grid()

    # old test pattern
    # keeping this here because i might reuse it
    #
    # game_grid = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]
    #
    # glider = [
    #     (1,0),
    #     (2,1),
    #     (0,2),
    #     (1,2),
    #     (2,2)
    # ]
    #
    # for gx,gy in glider:
    #     game_grid[gy][gx] = 1


    gen_counter = 0

    while gen_counter < GENERATIONS:

        render(game_grid, gen_counter)

        time.sleep(DELAY)

        updated = next_generation(game_grid)

        # temporary variable probably not needed
        game_grid = updated

        gen_counter += 1


# entry point
if __name__ == "__main__":

      main()
