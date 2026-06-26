from abc import ABC,abstractmethod
from typing import List

class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self):
        pass

class File(FileSystemComponent):
    def __init__(self, name: str):
        self.__name = name

    def show_details(self):
        return f"File : {self.__name}"


class Folder(FileSystemComponent):
    def __init__(self, name: str):
        self.__name = name
        self.__components: List[FileSystemComponent] = []

    def add(self, component: FileSystemComponent):
        self.__components.append(component)

    def show_details(self):
        print(f"Folder name: {self.__name}")
        for component in self.__components:
            print(component.show_details())

file1 = File("image.png")
file2 = File("ppt")
file3 = File("word.exe")

sub_folder = Folder("sub folder")
sub_folder.add(file1)
sub_folder.add(file2)
sub_folder.add(file3)

image_file = File("imaaageeee")
movie = File("krissh")
main_folder = Folder("main folder")
main_folder.add(image_file)
main_folder.add(movie)
main_folder.add(sub_folder)

main_folder.show_details()