import random, time

try:
    import pygame
    pygame.init()

    screen = pygame.display.set_mode((400, 200))
    pygame.display.set_caption("Mini Audio Visualizer")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        for i in range(40):
            h = random.randint(1, 150)
            pygame.draw.rect(screen, (0, 255, 0), (i * 10, 200 - h, 8, h))

        pygame.display.flip()
        time.sleep(0.05)

    pygame.quit()

except Exception as e:
    print("Requires pygame -", e)
