import time
from typing import List


class HighResolutionPhoto:
    def __init__(self,file_name):
        self.__file_name=file_name
        self.__image_data=None
        self.load_from_disk()

    def load_from_disk(self):
        time.sleep(1)
        self.__image_data=f"[[Loaded image data of {self.__file_name}]]"
        print(f"Loaded {self.__file_name} from disk")
    def display(self):
        print(f"{self.__file_name} has an image data of {self.__image_data}\n")

class PhotoGallery:
    def __init__(self):
        self.__images:List[HighResolutionPhoto]=[]

    def add_image(self,file_name):
        image = HighResolutionPhoto(file_name)
        self.__images.append(image)

    def display_gallery(self):
        for image in self.__images:
            image.display()


photo_gallery = PhotoGallery()
photo_gallery.add_image("image1.png")
photo_gallery.add_image("image2.png")
photo_gallery.add_image("image3.png")
photo_gallery.add_image("image4.png")