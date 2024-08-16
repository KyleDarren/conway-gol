# Date started: 8/16/2024

import pygame
import numpy as np

# Define the dimensions of the grid
width, height = 800, 800
rows, cols = 50, 50
cell_size = width // cols

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def update_grid(grid):
    new_grid = np.copy(grid)
    for r in range(rows):
        for c in range(cols):
            # Count the number of live neighbors 3x3 subgrid
            # Exclude the current cell or the middle cell
            live_neighbors = np.sum(grid[r-1:r+2, c-1:c+2]) - grid[r, c]
            
            
            # Apply Conway's rules
            if grid[r, c] == 1:  # Alive
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[r, c] = 0  # Dies
            else:  # Dead
                if live_neighbors == 3:
                    new_grid[r, c] = 1  # Born
    return new_grid

def draw_grid(screen, grid):
    # Loop through rows
    # In every rows loop through columns
    for r in range(rows):
        for c in range(cols):
            color = WHITE if grid[r, c] == 1 else BLACK
            # c tells the number of column the rectangle will draw
            # r tells the number of row the rectangle will draw
            pygame.draw.rect(screen, color, (c * cell_size, r * cell_size, cell_size, cell_size))

def main():
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Game of Life")
    
    # Initialize grid
    grid = np.random.choice([0, 1], size=(rows, cols))
    print(grid)
    
    # Handle game event
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the grid
        grid = update_grid(grid)

        # Draw the grid
        screen.fill(BLACK)
        draw_grid(screen, grid)
        pygame.display.flip()

        pygame.time.delay(100)

    pygame.quit()

if __name__ == "__main__":
    main()
