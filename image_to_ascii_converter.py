import os

from PIL import Image

_DEFAULT_PALETTE = "@%#*+=-:. "


class ImageToASCIIConverter:
    def __init__(
        self,
        save_folder_path: str,
        palette: str = None,
        width: int = 30,
    ):
        self._image_width = width

        if not palette:
            self._palette = _DEFAULT_PALETTE
        else:
            self._palette = palette

        self._palette_light_unit = 255 // len(self._palette)

        self._save_folder_path = save_folder_path
        self._ensure_directory_exists()

    def convert(self, image_path: str, image_name: str) -> None:
        image = Image.open(image_path)

        image_width, image_height = image.size
        result_image_width, result_image_height = (
            self._image_width,
            int(image_height / image_width * self._image_width / 1.3),
        )

        image = image.convert("L")

        image = image.resize((result_image_width, result_image_height))

        image_data = image.getdata()

        with open(
            os.path.join(self._save_folder_path, image_name + ".txt"), "w"
        ) as image_text_file:
            for y in range(result_image_height):
                for x in range(result_image_width):
                    pixel_brightness = image_data[y * result_image_width + x - 1]
                    char = self._palette[
                        pixel_brightness // self._palette_light_unit - 1
                    ]

                    image_text_file.write(char)
                image_text_file.write("\n")

        with open(
            os.path.join(self._save_folder_path, image_name + ".txt"), "r"
        ) as image_text_file:
            lines = image_text_file.readlines()

            for line in lines:
                print(line, end="")

    def _ensure_directory_exists(self) -> None:
        if os.path.exists(self._save_folder_path):
            if os.path.isfile(self._save_folder_path):
                raise ValueError(
                    f"Path {self._save_folder_path} exists and it is not a directory"
                )
        else:
            os.mkdir(self._save_folder_path)
