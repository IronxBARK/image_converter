from PIL import Image
from pathlib import Path
from rembg import remove

def convert_image(input_path: str, output_format: str, output_path: str = None):
    """
    Convert an image to a specified format.

    :param input_path: Path to the input image file.
    :param output_format: Desired output format (e.g., 'JPEG', 'PNG').
    :return: Path to the converted image file.
    """

    # create paths
    input_path = Path(input_path)
    if not output_path:
        output_path = input_path.with_suffix(f".{output_format.lower()}")

    image = Image.open(input_path)
    
    match output_format.upper():
        case "JPEG" | "JPG":
            image = image.convert("RGB")  # convert to RGB for JPEG

        case "GIF":
            image = image.quantize(colors=256)  # convert to GIF with 256 colors

        case "TIFF":
            compression = input(
                "Enter TIFF compression type ('raw', 'none', 'packbits', 'tiff_lzw', 'tiff_adobe_deflate' , 'tiff_deflate', 'jpeg', 'group3', 'group4': "
            )

        case "ICO":
            image = image.resize((64, 64))  # resize for ICO format

        case _:
            # open image and convert for png, bmp , tiff and webp formats
            image = Image.open(input_path).convert("RGBA")

    (
        image.save(output_path, format=output_format)
        if output_format.upper() != "TIFF"
        else image.save(
            output_path, format=output_format.upper(), compression=compression
        )
    )

def remove_background(input_path: str, output_path: str = None):
    """
    Remove the background from an image using rembg.

    :param input_path: Path to the input image file.
    :param output_path: Path to save the output image file without background.
    """
    input_path = Path(input_path)
    if not output_path:
        output_path = Path(input_path).with_name(f"{input_path.stem}_no_bg.png")

    # Read the input image
    with open(input_path, "rb") as input_file:
        input_image = input_file.read()

    # Remove the background
    output_image = remove(input_image)

    # Save the output image
    with open(output_path, "wb") as output_file:
        output_file.write(output_image)
