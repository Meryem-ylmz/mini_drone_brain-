import pygame
from config import (
    CELL_SIZE,
    GREEN,
    GRID_WIDTH,
    GRID_HEIGHT
)


class Drone:
    def __init__(self, start_position):
        self.position = start_position

    def move(self, dx, dy, grid_map):

        x, y = self.position

        new_x = x + dx
        new_y = y + dy

        # Harita sınırı kontrolü

        if new_x < 0:
            return

        if new_x >= GRID_WIDTH:
            return

        if new_y < 0:
            return

        if new_y >= GRID_HEIGHT:
            return

        # Engel kontrolü

        if grid_map.grid[new_y][new_x] == 1:
            return

        self.position = (new_x, new_y)

    def draw(self, screen):

        x, y = self.position

        pixel_x = x * CELL_SIZE
        pixel_y = y * CELL_SIZE

        pygame.draw.circle(
            screen,
            GREEN,
            (
                pixel_x + CELL_SIZE // 2,
                pixel_y + CELL_SIZE // 2
            ),
            CELL_SIZE // 3
        )