from image_to_ascii_converter import ImageToASCIIConverter


def main():
    converter = ImageToASCIIConverter("converted_images")

    converter.convert("images/mega.png")


if __name__ == "__main__":
    main()
