"""
instalar o pillow:
pip install Pillow
"""

from PIL import Image



image = Image.new('RGB', (300, 300), (255,0,0))

for i in range(5):
    image.save(f'quadradovermelho{i}.png')
