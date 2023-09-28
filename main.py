import pygame
pygame.init()

width = 1000
height = 600
display = pygame.display.set_mode((width, height))

score1 = 0
score2 = 0
clock = pygame.time.Clock()
time = 15
pygame.time.set_timer(pygame.USEREVENT, 1000)

player1 = pygame.image.load("images/player2.png")
player1_coor = player1.get_rect()
player1_coor.bottomright = (200, 200)

player2 = pygame.image.load("images/player2.png")
player2_coor = player2.get_rect()
player2_coor.topleft = (800, 400)

winning = pygame.mixer.Sound("sounds/win.wav")
t_over = pygame.mixer.Sound("sounds/t_over.wav")
tag_s = pygame.mixer.Sound("sounds/tag.mp3.mp3")

font1 = pygame.font.SysFont("arial", 24, False, False)
font2 = pygame.font.SysFont("arial", 35, False, False)

p1_score_text = font1.render(f"Player 1: {score1}", True, (255, 255, 255))
p1_score_text_coor = p1_score_text.get_rect()
p1_score_text_coor.topleft = (50, 50)

p2_score_text = font1.render(f"Player 2: {score2}", True, (255, 255, 255))
p2_score_text_coor = p2_score_text.get_rect()
p2_score_text_coor.topright = (950, 50)

time_text = font1.render(f"Time: {time}", True, (255, 255, 255))
time_text_coor = time_text.get_rect()
time_text_coor.center = (500, 60)

p1_won_text = font2.render("Player 1 Won", True, (255, 255, 255))
p1_won_text_coor = p1_won_text.get_rect()
p1_won_text_coor.center = (width // 2, height // 2)

p2_won_text = font2.render("Player 2 Won", True, (255, 255, 255))
p2_won_text_koor = p2_won_text.get_rect()
p2_won_text_koor.center = (width // 2, height // 2)

again_text = font2.render("Do you want to play again? Yes: Y, No: N", True, (255, 255, 255))
again_text_coor = again_text.get_rect()
again_text_coor.center = (width // 2, height // 2)

FPS = 30
speed = 15
turn = 1

durum = True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            durum = False
        if etkinlik.type == pygame.USEREVENT:
            time -= 1
            time_text = font1.render(f"Time: {time}", True, (255, 255, 255))

    tus = pygame.key.get_pressed()
    if tus[pygame.K_LEFT] and player1_coor.left > 0:
        player1_coor.x -= speed
    elif tus[pygame.K_RIGHT] and player1_coor.right < width:
        player1_coor.x += speed
    elif tus[pygame.K_UP] and player1_coor.top > 0:
        player1_coor.y -= speed
    elif tus[pygame.K_DOWN] and player1_coor.bottom < height:
        player1_coor.y += speed

    if tus[pygame.K_a] and player2_coor.left > 0:
        player2_coor.x -= speed
    elif tus[pygame.K_d] and player2_coor.right < width:
        player2_coor.x += speed
    elif tus[pygame.K_w] and player2_coor.top > 0:
        player2_coor.y -= speed
    elif tus[pygame.K_s] and player2_coor.bottom < height:
        player2_coor.y += speed

    if time > 0:
        if turn % 2 == 1:
            if player1_coor.colliderect(player2_coor):
                score2 += 1
                p1_score_text = font1.render(f"Player 1: {score1}", True, (255, 255, 255))
                tag_s.play()
                player1_coor.x = 200
                player1_coor.y = 200
                player2_coor.x = 800
                player2_coor.y = 400
                time = 15
                time_text = font1.render(f"Time: {time}", True, (255, 255, 255))
                turn += 1
        elif turn % 2 == 0:
            if player2_coor.colliderect(player1_coor):
                score2 += 1
                p2_score_text = font1.render(f"Player 2: {score2}", True, (255, 255, 255))
                tag_s.play()
                player1_coor.x = 200
                player1_coor.y = 200
                player2_coor.x = 800
                player2_coor.y = 400
                time = 15
                time_text = font1.render(f"Time: {time}", True, (255, 255, 255))
                turn += 1
    elif time <= 0:
        if turn % 2 == 1:
            score2 += 1
            p2_score_text = font1.render(f"Player 2: {score2}", True, (255, 255, 255))
            t_over.play()
            player1_coor.x = 200
            player1_coor.y = 200
            player2_coor.x = 800
            player2_coor.y = 400
            time = 15
            time_text = font1.render(f"Time: {time}", True, (255, 255, 255))
            turn += 1
        elif turn % 2 == 0:
            score1 += 1
            p1_score_text = font1.render(f"Player 1: {score1}", True, (255, 255, 255))
            t_over.play()
            player1_coor.x = 200
            player1_coor.y = 200
            player2_coor.x = 800
            player2_coor.y = 400
            time = 15
            time_text = font1.render(f"Time: {time}", True, (255, 255, 255))
            turn += 1
    if score1 == 5 or score2 == 5:
        if score2 == 5:
            winning.play()
            display.fill((0, 0, 0))
            display.blit(p1_won_text, p1_won_text_coor)
            pygame.display.update()
            pygame.time.delay(5000)
            display.fill((0, 0, 0))
            display.blit(again_text, again_text_coor)
            pygame.display.update()
            durum2 = True
            while durum2:
                for etkinlik2 in pygame.event.get():
                    if etkinlik2.type == pygame.KEYDOWN:
                        if etkinlik2.key == pygame.K_e:
                            score1 = 0
                            score2 = 0
                            p1_score_text = font1.render(f"Player 1: {score1}", True, (255, 255, 255))
                            p2_score_text = font1.render(f"Player 2: {score2}", True, (255, 255, 255))
                            player1_coor.x = 200
                            player1_coor.y = 200
                            player2_coor.x = 800
                            player2_coor.y = 400
                            time = 15
                            time_text = font1.render(f"Time: {time}", True, (255, 255, 255))
                            turn = 1
                            pygame.display.update()
                            clock.tick(FPS)
                            durum2 = False

                        if etkinlik2.key == pygame.K_h:
                            pygame.time.delay(200)
                            durum2 = False
                            durum = False

                        if etkinlik2.key == pygame.K_ESCAPE:
                            durum3 = False
                            durum = False

                    if etkinlik2.type == pygame.QUIT:
                        durum3 = False
                        durum = False

        elif score2 == 5:
            winning.play()
            display.fill((0, 0, 0))
            display.blit(p2_won_text, p2_won_text_koor)
            pygame.display.update()
            pygame.time.delay(5000)
            display.fill((0, 0, 0))
            display.blit(again_text, again_text_coor)
            pygame.display.update()
            durum3 = True
            while durum3:
                for element in pygame.event.get():
                    if element.type == pygame.KEYDOWN:
                        if element.key == pygame.K_e:
                            score1 = 0
                            score2 = 0
                            p1_score_text = font1.render(f"Player 1: {score1}", True, (255, 255, 255))
                            p2_score_text = font1.render(f"Player 2: {score2}", True, (255, 255, 255))
                            player1_coor.x = 200
                            player1_coor.y = 200
                            player2_coor.x = 800
                            player2_coor.y = 400
                            stime = 15
                            time_text = font1.render(f"Time: {time}", True, (255, 255, 255))
                            turn = 1
                            pygame.display.update()
                            clock.tick(FPS)
                            durum3 = False

                        if element.key == pygame.K_h:
                            pygame.time.delay(200)
                            durum3 = False
                            durum = False

                        if element.key == pygame.K_ESCAPE:
                            durum3 = False
                            durum = False

                    if element.type == pygame.QUIT:
                        durum3 = False
                        durum = False

    display.fill((0, 0, 0))
    display.blit(player1, player1_coor)
    display.blit(player2, player2_coor)
    display.blit(p1_score_text, p1_score_text_coor)
    display.blit(p2_score_text, p2_score_text_coor)
    display.blit(time_text, time_text_coor)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
