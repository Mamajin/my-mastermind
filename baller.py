"""This is the MasterMind game"""
import random


class Board:
    def __init__(self, x, y):
        """
        x is range of colors from 1-8 inclusive
        y is number of positions from 1-10 inclusive
        :param x:
        :param y:
        """
        self.x = x
        self.y = y
        self.answer = self.__get_answer()

    # create getters and setter

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    def __get_answer(self):
        """Create the randomized pattern/answer"""
        answer_ls = []
        for i in range(self.y):
            answer_ls.append(random.randint(1, self.x))
        return answer_ls

    @staticmethod
    def get_guess():
        """
        get user guess and return as a list
        staticmethod is put above to say that this method does not require
        attribute in the class
        :return:
        """
        guess = input("What is your guess?: ")
        print(f"Your guess is {guess}")
        guess = [int(x) for x in guess]
        return guess

    def check_guess(self, player_guess):
        """check user guess and give a hint"""
        # [2, 5, 5, 1]
        # What is your guess?: 1331
        # Your guess is 1331
        # o*
        # debug the code above printing only the one with higher truth value
        _hint = ""
        right_pos = 0
        right_num = 0
        for i in range(len(self.answer)):
            if player_guess[i] == self.answer[i]:
                right_pos += 1
            elif player_guess[i] in self.answer:
                right_num += 1
        # create the hint
        for i in range(right_pos):
            _hint += "*"
        for i in range(right_num):
            _hint += "o"
        return _hint

    def comp_ans_to_guess(self, player_guess):
        if self.answer == player_guess:
            return True
        else:
            pass


print("Playing Mastermind with 6 colors and 4 positions")
board = Board(6, 4)
print(board.answer)
game = True
tries = 0
while game:
    guess_ls = board.get_guess()
    hint = board.check_guess(guess_ls)
    print(hint)
    print()
    tries += 1
    if board.comp_ans_to_guess(guess_ls):
        game = False
print(f"You solve it after {tries} rounds")
