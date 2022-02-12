from PIL import Image, ImageDraw, ImageFont
from itertools import chain
import random
import hashlib

from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode

crypto_width = 500
crypto_height = 500
crypto_size = (crypto_width, crypto_height)

# ideas: random bg/font color, with no regard for contrast
# how to include cyrilir/greek letters?

def is_char_valid(table_char):
    (unicode_point, character, unicode_name) = table_char
    # print(f'{unicode_point} is {65 >= unicode_point and unicode_point <= 90}')
    return unicode_point >= 65 and unicode_point <= 90
    # TODO: a-z; cyrilic; greek

def get_all_chars_from_ttf(font_file, is_valid):
    """
    hihi https://stackoverflow.com/a/19438403
    """

    ttf = TTFont(font_file, 0, allowVID=0, ignoreDecompileErrors=True, fontNumber=-1)

    # [(unicode_point, character, unicode_name?)]
    chars = chain.from_iterable([y + (Unicode[y[0]],) for y in x.cmap.items()] for x in ttf["cmap"].tables)
    filtered = list(dict.fromkeys(filter(is_valid, chars)))
    # print('filtered', filtered)
    return filtered


def render_chars_from_font(crypto_font_file, dest_path, is_valid, crypto_size=16):
    crypto_hash = int(hashlib.sha1(crypto_font_file.encode("utf-8")).hexdigest(), 16) % (10 ** 14)

    print(crypto_hash)
    random.seed(crypto_hash)

    crypto_font = ImageFont.truetype(crypto_font_file, crypto_size)
    all_chars = get_all_chars_from_ttf(crypto_font_file, is_valid)
    # print(all_chars)

    for char in all_chars:
        # [(unicode_point, character, unicode_name?)]
        crypto_file_name = char[2].replace(' ', '_').lower()
        render_character(char[1], crypto_font, dest_path, crypto_file_name)


def render_character(crypto_char, crypto_font, dest_path, crypto_file_name):
    """
    thank you https://stackoverflow.com/a/1970930
    """

    crypto_bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    crypto_fg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    crypto_img = Image.new('RGB', crypto_size, color = crypto_bg_color)
    crypto_draw = ImageDraw.Draw(crypto_img)

    crypto_text_size_w, crypto_text_size_h = crypto_draw.textsize(crypto_char, font=crypto_font)
    crypto_center_x = (crypto_width - crypto_text_size_w) / 2
    crypto_center_y = (crypto_height - crypto_text_size_h) / 2
    crypto_draw.text((crypto_center_x, crypto_center_y), crypto_char, fill=crypto_fg_color, font=crypto_font)
    
    crypto_img.save(f'{dest_path}/{crypto_file_name}.png')


def create_unicode_validation(is_valid):
    def validation(table_char):
        (unicode_point, character, unicode_name) = table_char
        # print(f'{unicode_point} is {65 >= unicode_point and unicode_point <= 90}')
        return is_valid(unicode_point)
    # TODO: a-z; cyrilic; greek
    return validation


render_chars_from_font(
    "/Users/yehoshuaoliveira/Workspace/Ioxua/nft/image_generation/fonts/Roboto/Roboto-Regular.ttf",
    "/Users/yehoshuaoliveira/Workspace/Ioxua/nft/results/LETTERS",
    create_unicode_validation(lambda unicode_point: unicode_point >= 65 and unicode_point <= 90),
    220,
)