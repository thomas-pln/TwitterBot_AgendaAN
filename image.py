from PIL import Image, ImageFont, ImageDraw
from timeDate import todayFR, today

def printTxtImage():
    """
    Créer une image avec la date actuelle inscrite dessus.
    Base de l'image dans /data/util et la sauvegarde dans /data/txtImages
    """
    image = Image.open("./data/util/base.png")

    title_font = ImageFont.truetype('./data/util/Rondal-Regular.ttf', 400)

    title_text = todayFR()

    image_editable = ImageDraw.Draw(image)

    image_editable.text((75,300), title_text, (0, 0, 0), font=title_font)

    image.save("./data/txtImages/"+today()+".png")

