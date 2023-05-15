from PIL import Image


def resize(img_path):
    img = Image.open(img_path)
    width, height = img.size
    aspect_ratio = width / height
    new_height = int(100 / aspect_ratio)
    new_img = img.resize((100, new_height))
    new_img = new_img.convert("L")

    return new_img


def to_ascii(img_path):
    chars = '@$#*!;:~-,.  '
    img = resize(img_path)
    img_pixels = img.getdata()
    scalar = len(chars) / 255
    width, _ = img.size
    chars_list = ''.join([chars[int(pixel * scalar)] for pixel in img_pixels])
    output = '\n'.join([chars_list[i:i + width]for i in range(0, len(img_pixels), width)])
    return output



