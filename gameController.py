import pygame
import sys

def runGame(grid):
    # Initialize Pygame
    pygame.init()

    displaySize = 1200
    # Set up display
    width, height = displaySize, displaySize
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Grid of Squares")

    # Define the size of each square
    square_size = int(displaySize/grid.getGridSize())


    # Number of rows and columns
    rows = grid.getGridSize()
    columns = grid.getGridSize()

    paused = False
    
    # Main loop
    while True:
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused  # Toggle pause state
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Clear the screen
        screen.fill("white")

        # Draw the grid of squares
        for i in range(rows):
            for j in range(columns):
                x = j * square_size
                y = i * square_size
                #fill base on current state
                if grid.getGrid()[i,j] == 1:
                    # Draw the filled rectangle
                    pygame.draw.rect(screen, "black", (x, y, square_size, square_size))
        
        #make call here to set the new grid state based upon rules
        grid.calculateFState()
        # Update the display
        pygame.display.flip()
        pygame.time.delay(50)  # Optional delay to control the speed
        