from PIL import Image, ImageDraw, ImageFont

class TextImageGenerator:
    def __init__(self, width=300, height=100, background_color=(255, 255, 255), text_color=(0, 0, 0), font=None):
        # Initialize the class with the given parameters
        self.width = width
        self.height = height
        self.background_color = background_color
        self.text_color = text_color
        self.font = font if font else ImageFont.load_default()

    def generate_image(self, text):
        # Create a new image with the given dimensions and background color
        image = Image.new('RGB', (self.width, self.height), self.background_color)
        draw = ImageDraw.Draw(image)

        # Get the bounding box of the text to calculate its dimensions
        bbox = draw.textbbox((0, 0), text, font=self.font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Calculate the position to center the text
        position = ((self.width - text_width) // 2, (self.height - text_height) // 2)
        draw.text(position, text, font=self.font, fill=self.text_color)

        return image

    def generate_and_save_images(self, text_list):
        # Generate and save an image for each text in the list
        image_paths = []  # List to store the paths of the generated images

        for text in text_list:
            # Generate the image for the current text
            image = self.generate_image(text)

            # Save the image with the text as the filename
            filename = f"{text}.png"
            image.save(filename)

            # Store the filename in the list
            image_paths.append(filename)

            # Optionally display the image (for debugging)
            image.show()

        return image_paths  # Return a list of filenames


