from PIL import Image

def resize_svg(input_file, output_file, width, height):
  """
  This function resizes an SVG image to the specified width and height.

  Args:
      input_file (str): Path to the input SVG file.
      output_file (str): Path to save the resized SVG file.
      width (int): Desired width for the resized image.
      height (int): Desired height for the resized image.
  """
  try:
    with Image.open(input_file) as svg_image:
      svg_image = svg_image.resize((width, height), Image.LANCZOS)  # Use LANCZOS for better quality
      svg_image.save(output_file)
      print(f"Successfully resized {input_file} to {output_file} ({width}x{height})")
  except Exception as e:
    print(f"Error resizing SVG image: {e}")

# Example usage
input_file = "navajo_taco.jpg"
output_file = "navajo_taco.jpg"
new_width = 1110
new_height = 480

resize_svg(input_file, output_file, new_width, new_height)