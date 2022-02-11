from PIL import Image, ImageDraw, ImageFont

size = (500,500)

# ideas: random bg/font color, with no regard for contrast
# how to list all characters from a ttf file?

def render_chars_from_font(font_file, size=16):
    font = ImageFont.truetype("./fonts/Roboto-Regular.ttf", size)
    render_character('a', font)


def render_character(char, font):
    """
    thank you https://stackoverflow.com/a/1970930
    """


img = Image.new('RGB', size, color = (0, 0, 0))
 
d = ImageDraw.Draw(img)
d.text((10,10), "Hello World", fill=(255,255,255))
 
img.save('pil_text.png')