class GridMap:
    def __init__(self):
        self.grid = [
            [0 for _ in range(20)]
            for _ in range(15)
        ]

        self.base_position = (1, 1)
        self.mission_position = (15, 10)

        self.grid[self.base_position[1]][self.base_position[0]] = 2
        self.grid[self.mission_position[1]][self.mission_position[0]] = 3

        self.obstacles = [
            (5, 5), (6, 5), (7, 5),
            (10, 8), (11, 8), (12, 8),
            (8, 2), (8, 3), (8, 4)
        ]

        for x, y in self.obstacles:
            self.grid[y][x] = 1