# This is a python image library!
from PIL import Image, ImageDraw, ImageFont


def generate_image_with_text(text: str, filename: str, dimensions = (1080, 1080), color = (255, 255, 255)):
    """Creates an image with text
    This function takes in the text that we want written
    onto the image and creates a simple image with the passed
    dimensions and an RGB background also passed to the function."""

    width, height = dimensions

    # Create an image with the passed dimensions and RGB background
    img = Image.new('RGB', dimensions, color=color)

    # Write the passed text onto the image
    drawing_context = ImageDraw.Draw(img)

    # I chose this font from Google Fonts because
    # I liked it. It's downloaded into the folder that
    # gen_images.py is in. The second argument is
    # the font size if you want to change it.
    font = ImageFont.truetype("manrope.ttf", 120)

    # The anchor = mm says that we want place the center of the text at
    # the passed coordinates which is right in the middle of the image
    drawing_context.text((width / 2, height / 2), text, fill = (0,0,0), font = font, anchor = "mm")

    # Save the image
    img.save(filename)

def main():

    # We want 10k images
    NUM_IMAGES = 1000

    for i in range(NUM_IMAGES):
        filename = f'images/num_{i}.png'
        # Note that I'm only passing in the first two arguments
        # because I'm okay with the defaults for the remaining
        # ones.
        generate_image_with_text(str(i), filename)

# This block runs the main function if
# we call [python gen_images.py]
if __name__ == "__main__":
    main()
