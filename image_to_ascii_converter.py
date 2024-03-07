from PIL import Image


_DEFAULT_PALETTE = ""


class ImageToASCIIConverter:
    def __init__(self, save_folder_path: str, palette: str = None):
        if not palette:
            self._palette = _DEFAULT_PALETTE
        else:
            self._palette = palette

        self._save_folder_path = save_folder_path

    def convert(self, image_path: str) -> None:
        image = Image.open(image_path)

        print(image)
