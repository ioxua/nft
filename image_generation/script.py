from PIL import Image, ImageDraw, ImageFont

crypto_width = 500
crypto_height = 500
crypto_size = (crypto_width, crypto_height)

# ideas: random bg/font color, with no regard for contrast
# how to list all characters from a ttf file?

def render_chars_from_font(font_file, size=16):
    font = ImageFont.truetype("/Users/yehoshuaoliveira/Workspace/Ioxua/nft/image_generation/fonts/Roboto/Roboto-Regular.ttf", size)
    render_character('a', font)


def render_character(crypto_char, crypto_font):
    """
    thank you https://stackoverflow.com/a/1970930
    """


    crypto_img = Image.new('RGB', crypto_size, color = (0, 0, 0))
    
    crypto_draw = ImageDraw.Draw(crypto_img)

    crypto_text_size_w, crypto_text_size_h = crypto_draw.textsize(crypto_char, font=crypto_font)
    crypto_center_x = (crypto_width - crypto_text_size_w) / 2
    crypto_center_y = (crypto_height - crypto_text_size_h) / 2
    crypto_draw.text((crypto_center_x, crypto_center_y), crypto_char, fill="red", font=crypto_font)
    
    crypto_img.save('pil_text.png')

render_chars_from_font(None, size=120)