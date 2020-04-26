from abc import ABC, abstractmethod


class MazeGame(ABC):
    '''Creator'''

    def __init__(self) -> None:
        self.rooms = []
        self._prepare_rooms()

    def _prepare_rooms(self) -> None:
        room1 = self.make_room()
        room2 = self.make_room()

        room1.connect(room2)
        self.rooms.append(room1)
        self.rooms.append(room2)

    def play(self) -> None:
        print(f"Playing using {self.rooms[0]}")

    @abstractmethod
    def make_room(self):
        '''factory method'''
        raise NotImplementedError("You should implement this.")


class MagicMazeGame(MazeGame):
    '''Concrete Creator'''

    def make_room(self):
        '''factory method: reutrn concrete product'''
        return MagicRoom()


class OrdinaryMazeGame(MazeGame):
    '''Concrete Creator'''

    def make_room(self):
        '''factory method: reutrn concrete product'''
        return OrdinaryRoom()


class Room(ABC):
    '''Product'''

    def __init__(self) -> None:
        self.connected_rooms = []

    def connect(self, room) -> None:
        self.connected_rooms.append(room)


class MagicRoom(Room):
    '''Concrete Product'''

    def __str__(self):
        return "Magic Room"


class OrdinaryRoom(Room):
    '''Concrete Product'''

    def __str__(self):
        return "Ordinary Room"


if __name__ == "__main__":
    ordinaryGame = OrdinaryMazeGame()
    ordinaryGame.play()

    magicGame = MagicMazeGame()
    magicGame.play()
