import pygame
import random

class Game2048:
    def __init__(self):
        pygame.init()
        self.grid_size = 4
        self.window_size = 400
        self.cell_size = self.window_size // self.grid_size
        self.screen = pygame.display.set_mode((self.window_size, self.window_size + 50))
        pygame.display.set_caption("2048")
        self.font = pygame.font.Font(None, 50)
        self.small_font = pygame.font.Font(None, 36)
        self.running = True
        self.game_over = False
        self.score = 0

        self.grid = [[0] * self.grid_size for _ in range(self.grid_size)]
        self.add_random_tile()
        self.add_random_tile()

    def add_random_tile(self):
        empty_cells = [(r, c) for r in range(self.grid_size) for c in range(self.grid_size) if self.grid[r][c] == 0]
        if empty_cells:
            r, c = random.choice(empty_cells)
            self.grid[r][c] = random.choices([2, 4], weights=[90, 10])[0]

    def compress_row(self, row):
        return [i for i in row if i != 0] + [0] * row.count(0)

    def merge_row(self, row):
        for i in range(self.grid_size - 1):
            if row[i] != 0 and row[i] == row[i + 1]:
                row[i] *= 2
                self.score += row[i]
                row[i + 1] = 0
        return row

    def process_row_left(self, row):
        row = self.compress_row(row)
        row = self.merge_row(row)
        row = self.compress_row(row)
        return row

    def move_left(self, grid):
        return [self.process_row_left(row) for row in grid]

    def reverse_grid(self, grid):
        return [row[::-1] for row in grid]

    def transpose_grid(self, grid):
        return [list(row) for row in zip(*grid)]

    def move(self, direction):
        if self.game_over:
            return

        original = [row[:] for row in self.grid]

        if direction == 'left':
            self.grid = self.move_left(self.grid)
        elif direction == 'right':
            self.grid = self.reverse_grid(self.move_left(self.reverse_grid(self.grid)))
        elif direction == 'up':
            self.grid = self.transpose_grid(self.move_left(self.transpose_grid(self.grid)))
        elif direction == 'down':
            transposed = self.transpose_grid(self.grid)
            reversed_transposed = self.reverse_grid(transposed)
            moved = self.move_left(reversed_transposed)
            self.grid = self.transpose_grid(self.reverse_grid(moved))

        if self.grid != original:
            self.add_random_tile()

        if not self.can_move():
            self.game_over = True

    def can_move(self):
        for row in self.grid:
            if 0 in row:
                return True
        for r in range(self.grid_size):
            for c in range(self.grid_size - 1):
                if self.grid[r][c] == self.grid[r][c + 1]:
                    return True
        for c in range(self.grid_size):
            for r in range(self.grid_size - 1):
                if self.grid[r][c] == self.grid[r + 1][c]:
                    return True
        return False

    def get_tile_color(self, value):
        colors = {
            0: (205, 193, 180),
            2: (238, 228, 218),
            4: (237, 224, 200),
            8: (242, 177, 121),
            16: (245, 149, 99),
            32: (246, 124, 95),
            64: (246, 94, 59),
            128: (237, 207, 114),
            256: (237, 204, 97),
            512: (237, 200, 80),
            1024: (237, 197, 63),
            2048: (237, 194, 46)
        }
        return colors.get(value, (60, 58, 50))

    def draw_grid(self):
        self.screen.fill((250, 248, 239))

        for row in range(self.grid_size):
            for col in range(self.grid_size):
                value = self.grid[row][col]
                rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, self.get_tile_color(value), rect)
                pygame.draw.rect(self.screen, (187, 173, 160), rect, 2)
                if value != 0:
                    text = self.font.render(str(value), True, (0, 0, 0))
                    text_rect = text.get_rect(center=rect.center)
                    self.screen.blit(text, text_rect)

        # Отображение счёта
        score_text = self.small_font.render(f"Score: {self.score}", True, (119, 110, 101))
        self.screen.blit(score_text, (10, self.window_size + 10))

        # Game Over
        if self.game_over:
            overlay = pygame.Surface((self.window_size, self.window_size))
            overlay.set_alpha(180)
            overlay.fill((255, 255, 255))
            self.screen.blit(overlay, (0, 0))
            game_over_text = self.font.render("Game Over", True, (119, 110, 101))
            text_rect = game_over_text.get_rect(center=(self.window_size // 2, self.window_size // 2))
            self.screen.blit(game_over_text, text_rect)

        pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                key_to_direction = {
                    pygame.K_LEFT: 'left',
                    pygame.K_RIGHT: 'right',
                    pygame.K_UP: 'up',
                    pygame.K_DOWN: 'down'
                }
                if event.key in key_to_direction:
                    self.move(key_to_direction[event.key])

    def run(self):
        while self.running:
            self.handle_input()
            self.draw_grid()
        pygame.quit()


if __name__ == "__main__":
    game = Game2048()
    game.run()
