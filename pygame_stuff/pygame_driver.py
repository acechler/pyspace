import pygame
import math
import random

class Node:
    def __init__(self, value):
        self.value = value

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, node):
        self.adjacency_list[node] = []

    def add_edge(self, node1, node2):
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def remove_edge(self, node1, node2):
        self.adjacency_list[node1].remove(node2)
        self.adjacency_list[node2].remove(node1)

    def remove_vertex(self, node):
        while self.adjacency_list[node]:
            adjacent_node = self.adjacency_list[node][-1]
            self.remove_edge(node, adjacent_node)
        self.adjacency_list.pop(node, None)



class PygameDriver:
    def __init__(self):
        pass

    @staticmethod
    def run():

        x = 25
        y = 30
        # Initialize pygame
        pygame.init()

        node1 = Node((10,20))
        node2 = Node((40,60))
        node3 = Node((80,20))
        node4 = Node((200,20))
        graph = Graph()

        graph.add_vertex(node1)
        graph.add_vertex(node2)
        graph.add_vertex(node3)
        graph.add_vertex(node4)


        graph.add_edge(node1, node2)
        graph.add_edge(node1, node3)
        graph.add_edge(node2, node4)

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
            a += 0.001  # adjust this value to change the speed of the square

            # Drawing on the screen
            screen.fill((0, 0, 0))  # Fill the screen with black color
           
            pygame.draw.line(screen,(255,0,0),(x,y),(cx,cy))
            pygame.draw.line(screen,(255,0,0),(x,y),(cx-r,cy+r))
            pygame.draw.line(screen,(255,0,0),(x+r,y-r),(x,y))


            
            # Update the display
            pygame.display.flip()

        # Quit the game
        pygame.quit()
