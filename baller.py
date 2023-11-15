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
        :return:
        """
        guess = input("What is your guess?: ")
        print(f"Your guess is {guess}")
        guess = [int(x) for x in guess]
        return guess

    def check_guess(self, player_guess):
        """check user guess and give a hint"""
        hint = ""
        for i in range(len(self.answer)):
            if player_guess[i] == self.answer[i]:
                hint += "*"
            elif player_guess[i] in self.answer:
                hint += "o"
        return hint

    def comp_ans_to_guess(self, player_guess):
        if self.answer == player_guess:
            return False
        else:
            pass


