import pygame
import math
class PygameDriver:
    def __init__(self):
        pass

    @staticmethod
    def run():

        x = 25
        y = 30
        # Initialize pygame
        pygame.init()

        # Set up the display
        screen_width = 800
        screen_height = 600
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Pygame Window")
        # Define the parameters for the circle
        cx, cy = screen_width // 2, screen_height // 2  # center of the circle
        r = 100  # radius of the circle
        a = 0  # angle
        # Game loop
        running = True
        while running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Game logic
            x = cx + r * math.cos(a)
            y = cy + r * math.sin(a)
            a += 0.01  # adjust this value to change the speed of the square

            # Drawing on the screen
            screen.fill((255, 255, 255))  # Fill the screen with white color
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, 60, 60))


            # Update the display
            pygame.display.flip()

        # Quit the game
        pygame.quit()
