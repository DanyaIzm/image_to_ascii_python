from image_to_ascii_converter import ImageToASCIIConverter


def main():
    converter = ImageToASCIIConverter("converted_images", width=60)

    converter.convert("images/cc.png", "cc")
    converter.convert("images/cr.jpg", "cr")
    converter.convert("images/mega.png", "mega")


if __name__ == "__main__":
    main()
