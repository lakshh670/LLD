from abc import ABC,abstractmethod
from typing import List,Optional


class Song:
    def __init__(self,name):
        self.__name = name
    def get_title(self):
        return self.__name

class Iterator(ABC):
    @abstractmethod
    def is_next(self)->bool:
        pass
    def next(self)->Song:
        pass
class PlaylistIterator(Iterator):
    def __init__(self,songs:List[Song]):
        self.__position = 0
        self.__songs = songs
    def is_next(self) ->bool:
        return self.__position < len(self.__songs)
    def next(self):
        while self.is_next():
            song = self.__songs[self.__position]
            self.__position += 1
            return song



        return None
class Playlist():
    def __init__(self):
        self._songs:List[Song] = []

    def add_song(self,song:Song):
        self._songs.append(song)
    def create_iterator(self):
        return PlaylistIterator(self._songs)
playlist1 = Playlist()
playlist1.add_song(Song("Saiyarra"))
playlist1.add_song(Song("Starboy"))
iterator=playlist1.create_iterator()
print(iterator.next().get_title())
print(iterator.next().get_title())




