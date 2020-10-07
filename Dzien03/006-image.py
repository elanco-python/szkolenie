
from PIL import Image, ImageDraw, ImageFont, ImageFilter

image = Image.open("../extras/pasek.jpg")
font = ImageFont.truetype("../extras/trebuc.ttf", 44)

text = "Python jest SUPER!"
draw = ImageDraw.Draw(image)
draw.text( (200,500), text, font=font, fill="white" )
image.save("wynik.jpg")

blurred = image.filter(ImageFilter.BLUR)
blurred.save("blur.jpg")

grayed = image.convert("L")
grayed.save("grayed.jpg")

grayed = grayed.rotate(45)
#grayed.show()

print("="*80)
# miniaturki
import os, glob

files = glob.glob("tablice/**/*.jpg", recursive=True)
for file in files:
    #print(os.path.abspath(file))
    file_name, ext = os.path.splitext(file)
    #print(file_name,ext)
    new_file = f"{file_name}-thumb{ext}"
    print(new_file)
    with Image.open(file) as im:
        im.thumbnail( (400,200) )
        im.save(new_file)


