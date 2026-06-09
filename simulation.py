import pygame
from config import *
from grid_map import GridMap
from drone import Drone


class Simulation:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )

        pygame.display.set_caption(
            "Mini Otonom Drone Brain"
        )

        self.clock = pygame.time.Clock()

        self.grid_map = GridMap()

        self.drone = Drone(
            self.grid_map.base_position
        )

        self.running = True

    def draw_grid(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):

                cell = self.grid_map.grid[y][x]

                if cell == 0:
                    color = WHITE

                elif cell == 1:
                    color = BLACK

                elif cell == 2:
                    color = BLUE

                elif cell == 3:
                    color = RED

                pixel_x = x * CELL_SIZE
                pixel_y = y * CELL_SIZE

                pygame.draw.rect(
                    self.screen,
                    color,
                    (
                        pixel_x,
                        pixel_y,
                        CELL_SIZE,
                        CELL_SIZE
                    )
                )

                pygame.draw.rect(
                    self.screen,
                    GRAY,
                    (
                        pixel_x,
                        pixel_y,
                        CELL_SIZE,
                        CELL_SIZE
                    ),
                    1
                )

    def run(self):

        while self.running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        self.drone.move(1, 0, self.grid_map)

                    elif event.key == pygame.K_LEFT:
                        self.drone.move(-1, 0, self.grid_map)

                    elif event.key == pygame.K_UP:
                        self.drone.move(0, -1, self.grid_map)

                    elif event.key == pygame.K_DOWN:
                        self.drone.move(0, 1, self.grid_map)

            self.screen.fill(WHITE)

            self.draw_grid()

            self.drone.draw(self.screen)

            pygame.display.update()

            self.clock.tick(FPS)

        pygame.quit()