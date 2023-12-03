import pygame
import sys
import random

#Initializing the game

pygame.init()

font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

#Game Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)

#Create the game window
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tennis Game")

#Defining out players
player1 = pygame.Rect(50, HEIGHT // 2 - 50, 10, 100)
player2 = pygame.Rect(WIDTH - 60, HEIGHT // 2 - 50, 10, 100)

#Defining out ball
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_speed_x = 5
ball_speed_y = 5

#Scores
score_player_1 = 0
score_player_2 = 0 

#Game over flag
game_over = False

#Auto player speed
auto_player_speed = 5

#Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if not game_over:
        #player 1 control
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player1.top > 0:
            player1.y -= 5
        if keys[pygame.K_DOWN] and player1.bottom < HEIGHT:
            player1.y += 5
        if keys[pygame.K_LEFT] and player1.left > 0:
            player1.y -= 5
        if keys[pygame.K_RIGHT] and player1.right < WIDTH // 2:
            player1.y += 5
        
        #player 2 control
        if ball.centery < player2.centery and player2.top > 0:
            player2.y -= auto_player_speed
        elif ball.centery > player2.centery and player2.bottom < HEIGHT:
            player2.y += auto_player_speed

        #Ball movement
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        #Ball collision with top bottom walls
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y =- ball_speed_y
        
        #Ball collison with players
        if ball.colliderect(player1) or ball.colliderect(player2):
            ball_speed_x =- ball_speed_x

        #Ball out of bounds
        if ball.left <= 0:
            score_player_2 += 1
            ball_speed_x = abs(ball_speed_x)
            ball_speed_y = random.choice([-5,5])
            ball.x = WIDTH // 2 - 15
            ball.y = HEIGHT // 2 - 15
        if ball.right >= WIDTH:
            score_player_1 += 1
            ball_speed_x = -abs(ball_speed_x)
            ball_speed_y = random.choice([-5,5])
            ball.x = WIDTH // 2 - 15
            ball.y = HEIGHT // 2 - 15
            
        
    # Clear the screen
    screen.fill(BLACK)

    #Drawing players and ball
    pygame.draw.rect(screen,WHITE, player1)
    pygame.draw.rect(screen,WHITE, player2)
    pygame.draw.ellipse(screen,WHITE, ball)

    #Draw scores
    score_display = font.render(f"{score_player_1} - {score_player_2}", True, WHITE)
    screen.blit(score_display, (WIDTH // 2 - 40, 10))

    #Update the display
    pygame.display.update()

    #Cap the frame rate
    clock.tick(FPS)

    #Game over Condition
    if score_player_1 >= 5 or score_player_2 >= 5:
        game_over = True

#Display the winners
winner = "Player 1" if score_player_1 >= 5 else "Player 2"
winner_display = font.render(f"Game Over {winner} winns", True, WHITE)
screen.blit(winner_display, (WIDTH // 2- 150, HEIGHT // 2 - 18))
pygame.display.update()

#Wait for a moment before quitting
pygame.time.wait(3000)
pygame.quit()
sys.exit