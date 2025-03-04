from random import randint


class Robot:
    def __init__(self):
        self._X, self._Y = randint(0, 100), randint(0, 100)
        self._path = [(self._X, self._Y)]

    def move(self, moveString: str):
        moveString = moveString.lower()

        for char in moveString:
            if char == "e":
                self._path.append((self._path[-1][0] + 1, self._path[-1][1]))
            elif char == "w":
                self._path.append((self._path[-1][0] - 1, self._path[-1][1]))
            elif char == "n":
                self._path.append((self._path[-1][0], self._path[-1][1] + 1))
            elif char == "s":
                self._path.append((self._path[-1][0], self._path[-1][1] - 1))
        return self._path[-1]

    def path(self):
        return self._path

move = "nsew"
moves = ""
for i in range(10):
    moves += move[randint(0,3)]

robot = Robot()
robot.move(moves)
print(robot.path())