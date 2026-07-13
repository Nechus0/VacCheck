import urllib.request
import os
from PIL import Image, ImageDraw, ImageFont

# Download Inter Bold font
font_url = "https://github.com/rsms/inter/raw/master/docs/font-files/Inter-Bold.ttf"
font_path = "Inter-Bold.ttf"
if not os.path.exists(font_path):
    urllib.request.urlretrieve(font_url, font_path)

# Download Inter Regular font
font_url_reg = "https://github.com/rsms/inter/raw/master/docs/font-files/Inter-Regular.ttf"
font_path_reg = "Inter-Regular.ttf"
if not os.path.exists(font_path_reg):
    urllib.request.urlretrieve(font_url_reg, font_path_reg)

size = (512, 512)
img = Image.new('RGB', size, color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# Load fonts
try:
    font_large = ImageFont.truetype(font_path, 220)
    font_small = ImageFont.truetype(font_path_reg, 80)
except Exception as e:
    print(f"Failed to load font: {e}")
    font_large = ImageFont.load_default()
    font_small = ImageFont.load_default()

# Calculate text bounding boxes to center them
text_vac = "VAC"
text_check = "check"

# For Pillow >= 8.0.0, use textbbox
try:
    bbox_vac = font_large.getbbox(text_vac)
    w_vac = bbox_vac[2] - bbox_vac[0]
    h_vac = bbox_vac[3] - bbox_vac[1]
    
    bbox_check = font_small.getbbox(text_check)
    w_check = bbox_check[2] - bbox_check[0]
    h_check = bbox_check[3] - bbox_check[1]
except AttributeError:
    # Older Pillow
    w_vac, h_vac = font_large.getsize(text_vac)
    w_check, h_check = font_small.getsize(text_check)

x_vac = (size[0] - w_vac) / 2
# shift up a bit to make room for 'check'
y_vac = (size[1] - h_vac - h_check - 20) / 2 - 20

x_check = (size[0] - w_check) / 2
y_check = y_vac + h_vac + 20

# Draw text
draw.text((x_vac, y_vac), text_vac, font=font_large, fill=(0, 0, 0))
draw.text((x_check, y_check), text_check, font=font_small, fill=(0, 0, 0))

# Also draw a border? User asked for clean B&W.
# No border needed, iOS clips to rounded square automatically.

img.save('apple-touch-icon.png')
print("Saved apple-touch-icon.png")

# Also save a favicon.ico just in case
img.resize((64, 64)).save('favicon.ico')
