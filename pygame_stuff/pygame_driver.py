import pygame

class PygameDriver:
    def __init__(self):
        pass

    @staticmethod
    def run():

        x = 25

        # Initialize pygame
        pygame.init()

        # Set up the display
        screen_width = 800
        screen_height = 600
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Pygame Window")

        # Game loop
        running = True
        while running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Game logic
            x = (x + 1) % screen_width
            # Drawing on the screen
            screen.fill((255, 255, 255))  # Fill the screen with white color
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, 30, 60, 60))

            # Update the display
            pygame.display.flip()

        # Quit the game
        pygame.quit()
