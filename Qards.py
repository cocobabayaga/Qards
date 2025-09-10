import pygame

# Initialize game
pygame.init()

# Get monitor size
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h

# Set up the fullscreen game window
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption('QARDS')

# Auto-scale font size based on screen width
font_size = screen_width // 10
font = pygame.font.SysFont(None, font_size, bold=True)

# Render the title
title_text = "QARDS"
title_surface = font.render(title_text, True, (255, 255, 255))
title_rect = title_surface.get_rect(center=(screen_width // 2, font_size // 2 + 10))

# Game initialization
from Game import Game
game = Game()
game.init_and_shuffle_deck()
game.deal_cards(4, 8)
for player in game.players:
    print(f"Player {player.id} hand: {player.hand}")

running = True

# Game loop
while running:
    for event in pygame.event.get():


        if event.type == pygame.QUIT or \
           (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
    screen.fill((39, 59, 50))  # Clear screen with Casino green
    screen.blit(title_surface, title_rect)  # Draw title

    pygame.display.flip()

# Quit Pygame
pygame.quit()