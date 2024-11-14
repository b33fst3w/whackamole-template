import pygame, random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_pos_x = 0
        mole_pos_y = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            for i in range(1, 17):
                pygame.draw.line(screen, 'dark green', (0, (32*i)), (640,(32*i)))
            for i in range(1,21):
                pygame.draw.line(screen, 'dark green', ((32*i), 0), ((32*i),512))
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = event.pos
                maus_row = mouse_x//32
                maus_col = mouse_y//32
                mole_row = mole_pos_x//32
                mole_col = mole_pos_y//32
                if maus_row == mole_row and maus_col == mole_col:
                    mole_pos_x = random.randrange(0,19) * 32
                    mole_pos_y = random.randrange(0, 15) * 32
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_pos_x, mole_pos_y)))
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
