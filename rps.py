"""This program plays a game of Rock, Paper, Scissors between two Players,

and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players

in this game"""


class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            print()
            choice = input("Select Your Move Rock , Paper , Scissors ")
            if choice.lower() in moves:
                return choice.lower()
            else:
                print("\nInvalid Choice! Please Select Again")


class ReflectPlayer(Player):
    rem = random.choice(moves)

    def move(self):
        return self.rem

    def learn(self, my_move, their_move):
        self.rem = their_move


class CyclePlayer(Player):
    rem = random.choice(moves)

    def move(self):
        for i in range(0, len(moves)):
            if moves[i] == self.rem:
                if i == len(moves) - 1:
                    return moves[0]
                return moves[i + 1]
        return self.rem

    def learn(self, my_move, their_move):
        self.rem = my_move


def beats(one, two):
    if (one == 'rock' and two == 'scissors') \
        or (one == 'scissors' and two == 'paper') \
            or (one == 'paper' and two == 'rock'):
        print("Player 1 wins!")
        print()
        return True
    elif one == two:
        print("Tie!")
        print()

        return
    elif (two == 'rock' and one == 'scissors') \
        or (two == 'scissors' and one == 'paper') \
            or (two == 'paper' and one == 'rock'):
        print("Player 2 wins!")
        print()

        return False


class Game:

    def __init__(self, p1, p2):

        self.p1 = p1

        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):

        move1 = self.p1.move()

        move2 = self.p2.move()

        print(f"Player 1: {move1}  Player 2: {move2}")

        res = beats(move1, move2)
        if res is True:
            self.p1_score += 1
        elif res is False:
            self.p2_score += 1

        self.p1.learn(move1, move2)

        self.p2.learn(move2, move1)

    def play_game(self):

        print("Game start!")

        for rounds in range(5):
            print(f"Round {rounds}:")

            self.play_round()

        print("Game over!")
        if self.p1_score > self.p2_score:
            print("Player 1 Wins The Game!")
        elif self.p2_score > self.p1_score:
            print("Player 2 Wins The Game!")
        elif self.p2_score == self.p1_score:
            print("The Game Was Draw!")
        print("\nPlayer 1 Scores: ", self.p1_score)
        print("\nPlayer 2 Scores: ", self.p2_score)


if __name__ == '__main__':
    print("\nRandom vs Random Player")
    print("  ********************  ")
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()
    print()
    print("\nRandom vs Human Player")
    print("  ********************  ")
    game1 = Game(RandomPlayer(), HumanPlayer())
    game1.play_game()
    print()
    print("\nReflect vs Random Player")
    print("  ********************  ")
    game2 = Game(RandomPlayer(), HumanPlayer())
    game2.play_game()
    print()
    print("\nCycle vs Random Player")
    print("  ********************  ")
    game3 = Game(RandomPlayer(), HumanPlayer())
    game3.play_game()
