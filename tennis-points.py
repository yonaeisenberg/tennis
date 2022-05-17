class Player:
    def __init__(self, name):
        self.name = name
        self.set = Set()

    def __str__(self):
        return self.name + " " + str(self.set)

    def increment(self, other):
        return self.set.increment(other.set)


class Point:
    def __init__(self):
        self.value = 0
        self.advantage = False

    def __str__(self):
        if self.advantage:
            return 'A'
        return str(self.value)

    def increment(self, other):
        if self.advantage:
            return True
        if other.advantage:
            other.advantage = False
            return False
        if self.value == 40 and other.value == 40:
            self.advantage = True
            return False
        if self.value == 40:
            return True
        elif self.value == 30:
            self.value = 40
            return False
        else:
            self.value += 15
            return False


class TieBreakPoint:
    def __init__(self):
        self.value = 0

    def __str__(self):
        return str(self.value)

    def increment(self, other):
        self.value += 1
        if self.value >= 7 and self.value - other.value >= 2:
            return True
        return False


class Game:
    def __init__(self):
        self.value = 0
        self.point = Point()
        self.tie_break = False
        self.tie_break_point = TieBreakPoint()

    def __str__(self):
        if self.tie_break:
            return str(self.value) + " " + str(self.tie_break_point)
        return str(self.value) + " " + str(self.point)

    def increment(self, other):
        if self.tie_break:
            return self.tie_break_point.increment(other.tie_break_point)
        if self.point.increment(other.point):
            self.value += 1
            if self.value == 6 and other.value == 6:
                self.tie_break = True
                other.tie_break = True
                self.tie_break_point = TieBreakPoint()
                other.tie_break_point = TieBreakPoint()
            elif self.value >= 6 and (self.value - other.value) >= 2:
                return True
            else:
                self.point = Point()
                other.point = Point()
                return False


class Set:
    def __init__(self):
        self.value = 0
        self.game = Game()

    def __str__(self):
        return str(self.value) + " " + str(self.game)

    def increment(self, other):
        if self.game.increment(other.game):
            self.value += 1
            if self.value >= 2:
                return True
            self.game = Game()
            other.game = Game()
            return False


def main():
    print("Welcome to a new tennis match!")
    first_player_name = input("Enter name of player number 1:")
    player1 = Player(first_player_name)
    second_player_name = input("Enter name of player number 2:")
    player2 = Player(second_player_name)
    print("Let the match begin!")

    while True:
        print("1.", player1)
        print("2.", player2)
        next_point_winner = input("Enter the number of next point winner (1 or 2):")
        if next_point_winner == '1' and player1.increment(player2):
            print("Game, set and match", player1.name)
            return
        elif next_point_winner == '2' and player2.increment(player1):
            print("Game, set and match", player2.name)
            return


if __name__ == "__main__":
    main()

