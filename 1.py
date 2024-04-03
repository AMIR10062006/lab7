import pygame
import math
import datetime

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Clock")

def draw_clock_face():
    center = (200, 200)
    radius = 150
    pygame.draw.circle(screen, (255, 255, 255), center, radius, 2)
    font = pygame.font.Font(None, 36)
    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))
        text = font.render(str(i), True, (255, 255, 255))
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)

def draw_clock_hands():
    center = (200, 200)
    current_time = datetime.datetime.now()
    hour_angle = math.radians((current_time.hour % 12) * 30 - 90 + current_time.minute * 0.5)
    hour_hand_length = 80
    hour_hand = (
        center[0] + int(hour_hand_length * math.cos(hour_angle)),
        center[1] + int(hour_hand_length * math.sin(hour_angle))
    )
    pygame.draw.line(screen, (255, 0, 0), center, hour_hand, 6)
    minute_angle = math.radians(current_time.minute * 6 - 90)
    minute_hand_length = 120
    minute_hand = (
        center[0] + int(minute_hand_length * math.cos(minute_angle)),
        center[1] + int(minute_hand_length * math.sin(minute_angle))
    )
    pygame.draw.line(screen, (0, 255, 0), center, minute_hand, 4)
    second_angle = math.radians(current_time.second * 6 - 90)
    second_hand_length = 130
    second_hand = (
        center[0] + int(second_hand_length * math.cos(second_angle)),
        center[1] + int(second_hand_length * math.sin(second_angle))
    )
    pygame.draw.line(screen, (0, 0, 255), center, second_hand, 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    draw_clock_face()
    draw_clock_hands()
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
