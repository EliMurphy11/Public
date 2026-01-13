import os
import pygame

# Initialize pygame for Surface drawing
pygame.init()

# Create a large canvas to draw detail, then scale down
W, H = 256, 176
surf = pygame.Surface((W, H), pygame.SRCALPHA)

# Nugget base colors
base = (222, 170, 110)
shadow = (170, 110, 60)
spot_dark = (155, 95, 45)
spot_light = (200, 140, 80)
high = (255, 230, 200)

# Draw irregular nugget shape using overlapping ellipses and polygons
pygame.draw.ellipse(surf, base, (16, 28, 224, 120))
pygame.draw.ellipse(surf, base, (40, 8, 176, 128))
pygame.draw.ellipse(surf, base, (0, 44, 140, 90))

# Add darker rim for depth
pygame.draw.ellipse(surf, shadow, (12, 32, 232, 124), 10)

# Add textured spots (crumbs)
crumbs = [
    (60, 54, 12), (120, 74, 14), (82, 98, 9), (156, 46, 10),
    (38, 86, 8), (170, 82, 7), (110, 36, 8)
]
for x, y, r in crumbs:
    pygame.draw.circle(surf, spot_dark, (x, y), r)
    # inner lighter rim for the crumb
    pygame.draw.circle(surf, spot_light, (x-2, y-1), int(r*0.6))

# Highlights to convey crunchiness
pygame.draw.ellipse(surf, high, (72, 22, 48, 22))
pygame.draw.ellipse(surf, high, (116, 10, 60, 24))

# Subtle translucent sheen layers
for alpha, rect in [(30, (70,20,48,22)), (18, (110,8,60,24))]:
    layer = pygame.Surface((W, H), pygame.SRCALPHA)
    pygame.draw.ellipse(layer, (255,255,255,alpha), rect)
    surf.blit(layer, (0,0))

# Add some small crunchy specks with varying opacities
import random
random.seed(42)
for _ in range(25):
    x = random.randint(10, W-10)
    y = random.randint(20, H-20)
    r = random.randint(1, 3)
    col = (*random.choice([(140,90,45),(180,120,70),(210,150,90)]), random.randint(180, 255))
    pygame.draw.circle(surf, col, (x, y), r)

# Smoothscale down for in-game size
final = pygame.transform.smoothscale(surf, (96, 64))

# Save into both project image folders
root = os.getcwd()  # /Users/reginamurphy/Public
paths = [
    os.path.join(root, 'python_work', 'Alien_Game', 'images', 'chicken_nugget.png'),
    os.path.join(root, 'python_work', 'Alien_Game_clean', 'images', 'chicken_nugget.png'),
]

for p in paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    pygame.image.save(final, p)
    print('Wrote', p)

pygame.quit()
