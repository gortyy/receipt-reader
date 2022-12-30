import cv2
import pytesseract


class Reader:
    def __init__(
        self, image_file_path: str, tesseract_config: str = f"--oem 3 --psm 3 -l pol"
    ):
        self.image_file_path = image_file_path
        self._tesseract_config = tesseract_config

    def read_image(self) -> str:
        img = cv2.imread(self.image_file_path)
        img = self._threshold(self._grayscale(img))
        return pytesseract.image_to_string(img, config=self._tesseract_config)

    @classmethod
    def _grayscale(cls, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    @classmethod
    def _threshold(cls, image):
        return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
