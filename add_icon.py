"""
A script to add the icon to the bottom-right corner of an image.

This script uses the Pillow library to composite an icon onto a base image. It
scales the icon and padding dynamically based on the base 
image's dimensions, ensuring a consistent look across various sizes.

Using the arguments, you can specify the icon and set an output path.

Usage:
    
    To add a single, specific icon to an image:
    $ python add_icon.py <path_to_image> <icon_name.png>

    Example:
    $ python add_icon.py examples/originals/summer.png white_on_black.png

    To generate a version of the image for every available icon:
    $ python add_icon.py <path_to_image> all

    Example:
    $ python add_icon.py examples/originals/winter.png all

    Optional arguments:
    -o, --output: Specify a custom path for the output file.

    Example with optional arguments:
    $ python add_icon.py assets/photo.jpg blue.png -o results/photo_with_icon.png

Prerequisites:
    
    This script requires the Pillow library. You can install it using pip:
    $ pip install Pillow

"""
import argparse
from PIL import Image
import os

IMAGE_HEIGHT_TO_ICON_HEIGHT_RATIO = 40
IMAGE_HEIGHT_TO_PADDING_RATIO = 100

def _open_image(path):
    """Opens an image from a given path and converts it to RGBA format.

    Args:
        path (str): The file path to the image.

    Returns:
        Image.Image: The opened image object in RGBA format.
    """
    print(f"Opening image: {path}")
    return Image.open(path).convert("RGBA")

def _resize_icon(icon_image, base_height):
    """Resizes the icon based on the height of the base image.

    The new height is determined by the IMAGE_HEIGHT_TO_ICON_HEIGHT_RATIO.
    The width is scaled proportionally to maintain the aspect ratio.

    Args:
        icon_image (Image.Image): The icon image to resize.
        base_height (int): The height of the base image.

    Returns:
        Image.Image: The resized icon image.
    """
    new_icon_height = base_height / IMAGE_HEIGHT_TO_ICON_HEIGHT_RATIO
    icon_width, icon_height = icon_image.size
    aspect_ratio = icon_width / icon_height
    new_icon_width = int(new_icon_height * aspect_ratio)
    
    print(f"Resizing icon to {new_icon_width}x{int(new_icon_height)}")
    return icon_image.resize((new_icon_width, int(new_icon_height)), Image.Resampling.LANCZOS)

def _calculate_position(base_size, icon_size):
    """Calculates the bottom-right position for the icon.

    Args:
        base_size (tuple): A tuple (width, height) of the base image.
        icon_size (tuple): A tuple (width, height) of the icon image.

    Returns:
        tuple: A tuple (x, y) representing the top-left corner for the paste operation.
    """
    base_width, base_height = base_size
    icon_width, icon_height = icon_size
    
    padding = int(base_height / IMAGE_HEIGHT_TO_PADDING_RATIO)
        
    return (base_width - icon_width - padding, base_height - icon_height - padding)

def _generate_output_path(base_image_path, icon_name):
    """Generates the output file path.

    The format is: <base_name>_with_icon_<icon_name>.<ext>.

    Args:
        base_image_path (str): The path to the original base image.
        icon_name (str): The filename of the icon.

    Returns:
        str: The generated output file path.
    """
    dir_name, file_name = os.path.split(base_image_path)
    name, ext = os.path.splitext(file_name)
    icon_name_part, _ = os.path.splitext(icon_name)
    return os.path.join(dir_name, f"{name}_with_icon_{icon_name_part}{ext}")

def _composite_and_save(base_image, icon_image, position, output_path):
    """Composites the icon onto the base image and saves the result.

    Args:
        base_image (Image.Image): The base image.
        icon_image (Image.Image): The icon image.
        position (tuple): The (x, y) position to paste the icon.
        output_path (str): The path to save the final image.
    """
    icon_layer = Image.new("RGBA", base_image.size, (0, 0, 0, 0))
    icon_layer.paste(icon_image, position, icon_image)
    final_image = Image.alpha_composite(base_image, icon_layer)
    
    print(f"Saving result to: {output_path}")
    final_image.save(output_path, "PNG")
    print("Done.")

def _add_icon_to_single_image(base_image_path, icon_name, output_path=None):
    """Adds a single icon to the bottom right corner of an image.

    This function orchestrates the process of opening, resizing, positioning,
    and saving the image with the icon.

    Args:
        base_image_path (str): Path to the base image.
        icon_name (str): Name of the icon file.
        output_path (str, optional): Path for the output image. Defaults to None.

    Returns:
        str: The path to the saved image, or None if an error occurred.
    """
    icon_path = os.path.join('icon', 'png', icon_name)
    try:
        base_image = _open_image(base_image_path)
        icon_image = _open_image(icon_path)
        
        resized_icon = _resize_icon(icon_image, base_image.height)
        position = _calculate_position(base_image.size, resized_icon.size)
        
        if not output_path:
            output_path = _generate_output_path(base_image_path, icon_name)
            
        _composite_and_save(base_image, resized_icon, position, output_path)
        return output_path

    except FileNotFoundError as e:
        print(f"Error: {e}. Please check file paths.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main(base_image_path, icon_name, output_path=None):
    """Main function to add icon(s) to an image.

    If 'icon_name' is 'all', it processes all icons in the 'icon/png' directory.
    Otherwise, it processes a single specified icon.

    Args:
        base_image_path (str): Path to the base image.
        icon_name (str): Name of the icon, or 'all'.
        output_path (str, optional): Path for the output image. Defaults to None.
    """
    if icon_name.lower() == 'all':
        icon_dir = os.path.join('icon', 'png')
        if not os.path.isdir(icon_dir):
            print(f"Error: Icon directory not found at '{icon_dir}'")
            return

        icons = [f for f in os.listdir(icon_dir) if f.endswith('.png')]
        if not icons:
            print(f"No icons found in '{icon_dir}'")
            return
            
        print(f"Found icons: {', '.join(icons)}")
        for i, current_icon_name in enumerate(icons):
            print(f"Processing icon {i+1}/{len(icons)}: {current_icon_name}")
            _add_icon_to_single_image(base_image_path, current_icon_name, None)

    else:
        _add_icon_to_single_image(base_image_path, icon_name, output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add an icon to an image.")
    parser.add_argument("image_path", help="Path to the base image.")
    parser.add_argument("icon_name", help="Name of the icon file from the icon/png directory (e.g., 'white_on_black.png').")
    parser.add_argument("-o", "--output", help="Optional path for the output image.")
    
    args = parser.parse_args()

    main(args.image_path, args.icon_name, args.output)
