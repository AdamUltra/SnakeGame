import pygame
pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption('Snake Game by AdamUltra')
blue = (0, 0, 255)
red = (255, 0, 0)
GameOver = False
while not GameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOver = True
    pygame.draw.rect(dis, blue, [200, 150, 10, 10])
    pygame.display.update()
pygame.quit()
quit()
