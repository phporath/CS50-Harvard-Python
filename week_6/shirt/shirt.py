import sys
import os
from PIL import Image
from PIL import ImageOps


def main():
    len_argv = len(sys.argv)

    if len_argv < 2:
        sys.exit("Too few command-line arguments")

    if len_argv > 3:
        sys.exit("Too many command-line arguments")

    validation(sys.argv[1], sys.argv[2])
    new_image(sys.argv[1], sys.argv[2])


def validation(img_inp, img_out):
    allowed_extensions = [".jpg", ".jpeg", ".png"]

    input_ext = os.path.splitext(img_inp)[1].lower()
    output_ext = os.path.splitext(img_out)[1].lower()

    if input_ext not in allowed_extensions:
        sys.exit("Invalid input")

    if output_ext not in allowed_extensions:
        sys.exit("Invalid output")

    if not os.path.isfile(img_inp):
        sys.exit("Input does not exist")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")


def new_image(img_inp, img_out):
    shirt = Image.open("shirt.png")
    size = shirt.size

    try:
        img_original = Image.open(img_inp)
        img_original = ImageOps.fit(
            img_original, size, method=Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5)
        )
        img_original.paste(shirt, (0, 0), shirt)
        img_original.save(img_out)
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
