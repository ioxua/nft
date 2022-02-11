from PIL import Image, ImageDraw, ImageFont

crypto_width = 500
crypto_height = 500
crypto_size = (crypto_width, crypto_height)

# ideas: random bg/font color, with no regard for contrast
# how to list all characters from a ttf file?

def render_chars_from_font(font_file, size=16):
    font = ImageFont.truetype("./fonts/Roboto-Regular.ttf", size)
    render_character('a', font)


def render_character(crypto_char, font):
    """
    thank you https://stackoverflow.com/a/1970930
    """


    crypto_img = Image.new('RGB', crypto_size, color = (0, 0, 0))
    
    crypto_draw = ImageDraw.Draw(crypto_img)

    crypto_text_size = crypto_draw.textsize(crypto_char, font=font)
    crypto_draw.text(((W-w)/2,(H-h)/2), crypto_char, fill="black")
    
    crypto_img.save('pil_text.png')