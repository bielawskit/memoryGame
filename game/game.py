import time
from board.board import Board
import random
from score.score import Score


class Game(Board, Score):
    def __init__(self, matrix_x_size, matrix_y_size, number_of_attempts, game_type):
        super().__init__(matrix_x_size, matrix_y_size)
        self.number_of_attempts = number_of_attempts
        self.filename = f'users_{game_type}.json'

    words = []
    chosen_words = []
    word_place = {}
    start_time = time.time()
    guess_words = []
    guess_word = {}

    def load_words(self):
        # open and load file content to list "words"
        with open("game.txt", "r") as file:
            for line in file:
                for word in line.split():
                    self.words.append(word)
        file.close()
        random.shuffle(self.words)

    def random_words(self):
        # choose random words, mixing and doubling
        for word in self.words:
            if len(self.chosen_words) < (self.matrix_x_size * self.matrix_y_size) // 2:
                if word not in self.chosen_words:
                    self.chosen_words.append(random.choice(word))
        self.chosen_words = self.chosen_words * len(self.num)
        random.shuffle(self.chosen_words)
        # print(f"Chosen words : {self.chosen_words}")

    def hide_words(self):
        # iterate over the columns, rows and hide words 
        counter = 0
        for letter in self.letters:
            for number in self.num:
                self.word_place[f"{letter}{number}"] = self.chosen_words[counter]
                counter += 1

        # print(self.word_place)

    def start_game(self):
        while True:
            if self.number_of_attempts >= 0:
                if '_' not in [cell for row in self.matrix_size for cell in row]:
                    print("Contragulation. You won. ;)")
                    self.end_time = time.time()
                    self.add_person()
                    break

                print(f"Number of attemps: {self.number_of_attempts}")
                move_1 = input("Give us the location (np. A1): ")

                if self.word_place[move_1] in self.guess_words:
                    print("This place is not available. Give different location.")
                    move_1 = input("Give us the location (np. A1): ")

                # guess the word
                if move_1 in self.word_place.keys():
                    self.matrix_size[int(move_1[1])][self.letters.index(move_1[0])] = self.word_place[move_1]
                    self.drawn_board()

                # guess the second word
                move_2 = input("Give us the location (np. A2): ")
                if move_2 != move_1:

                    if move_1 in self.word_place.keys() and move_2 in self.word_place.keys():
                        # checking if two words are the same
                        self.matrix_size[int(move_2[1])][self.letters.index(move_2[0])] = self.word_place[move_2]
                        self.guess_words.append(self.word_place[move_2])
                        self.drawn_board()

                        if self.word_place[move_1] == self.word_place[move_2]:
                            print("Correct. Good job.")

                        else:
                            self.matrix_size[int(move_1[1])][self.letters.index(move_1[0])] = "_"
                            self.matrix_size[int(move_2[1])][self.letters.index(move_2[0])] = "_"
                            print("Maybe next time.")
                            print('*' * 20)
                            print('*' * 20)
                            print('*' * 20)
                            print('*' * 20)
                            print('*' * 20)

                            self.drawn_board()
                        self.number_of_attempts -= 1
                else:
                    print("Two times the same location. Try one more.")
            else:
                print(f"Number of attempts: {self.number_of_attempts}. Try one more. ;)")
                break
