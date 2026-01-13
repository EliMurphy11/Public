from PIL import Image
import os

src = os.path.join(os.getcwd(), 'python_work', 'Alien_Game_and_its_other_folders', 'images', 'sabrina_carpenter.webp')
out = os.path.join(os.getcwd(), 'python_work', 'Alien_Game_and_its_other_folders', 'images', 'sabrina_carpenter.png')

if not os.path.isfile(src):
    raise SystemExit(f"Source image not found: {src}")

img = Image.open(src).convert('RGBA')
width, height = img.size
scale = 0.88  # make the image ~12% smaller
new_size = (max(1, int(width * scale)), max(1, int(height * scale)))

img = img.resize(new_size, Image.LANCZOS)
img.save(out, format='PNG')
print('Saved resized PNG to:', out)
