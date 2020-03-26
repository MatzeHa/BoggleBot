# BoggleBot - Search words in a 4*4 square of letters #

import string
import random
import datetime

LETTERS_str = string.ascii_uppercase[0:27]
LETTERS = [x for x in LETTERS_str]

DIRECTIONS = [(-1, -1), (0, -1), (1, -1),
              (-1, 0), (1, 0),
              (-1, 1), (0, 1), (1, 1)]

# preparing List of Words
open_dict = open("Util/created_dict.txt", encoding="UTF-8")
DICTIONARY = open_dict.read()
DICTIONARY = DICTIONARY.split("\n")
to_delete = []
for index, word in enumerate(DICTIONARY):
    if len(word) < 3:
        to_delete.append(index)
to_delete.reverse()
for i in to_delete:
    del DICTIONARY[i]
DICTIONARY = [word.upper() for word in DICTIONARY]


class Dictionary:
    def __init__(self):
        pass


class Game:
    def __init__(self):
        self.dice = []
        self.board = [["A", "B", "C", "D"],
                      ["E", "F", "G", "H"],
                      ["I", "J", "K", "L"],
                      ["M", "N", "O", "P"]]

    def create_dice(self):
        dice = []
        for _j in range(16):
            _dice = []
            for _i in range(6):
                _dice.append(random.choice(LETTERS))
            dice.append(_dice)
        self.dice = dice

    def roll(self):
        for index_r, row in enumerate(self.board):
            for index_c, col in enumerate(row):
                self.board[index_r][index_c] = random.choice(self.dice[index_c + index_r])


# TRIES = []
RESULTS = []


class BoggleBot:
    def __init__(self, board, dictionary):
        self.board = board
        self.dictionary = dictionary

    def is_in_dict(self, word_in_dict):
        start_letter = word_in_dict[0]
        if word_in_dict in getattr(self.dictionary, start_letter):
            return True

    def words_start_with(self, w):
        start_letter = w[0]
        if len(list(filter(lambda x: x.startswith(w), getattr(self.dictionary, start_letter)))):
            return True
        else:
            return False

    def search_next_letter(self, start_letter, start_pos, visited, nr_tried_letters=0):
        current_word = start_letter
        current_pos = start_pos
        last_pos = current_pos

        for d in DIRECTIONS:
            next_pos = (current_pos[0] + d[1], current_pos[1] + d[0])
            if 0 <= next_pos[0] < 4 and 0 <= next_pos[1] < 4:
                if next_pos not in visited:                    # wenn die nächste poition noch nicht durchsucht wurde
                    visited.append(next_pos)
                    current_word = current_word + self.board[next_pos[0]][next_pos[1]]

                    if self.is_in_dict(current_word):               # Hänge wort an die Results an
                        RESULTS.append(current_word)
                    if not self.words_start_with(current_word):     # wenn kein wort damit anfängt
                        current_word = current_word[:-1]       # gehe einen schritt zurück
                        visited = visited[:-1]

                        continue                               # und versuche es mit der nächsten richtung
                    else:                                      # wenn ein wort damit anfängt
                        self.search_next_letter(current_word, (next_pos[0], next_pos[1]), visited, nr_tried_letters)
                        to_del = len(visited) - len(current_word) + 1
                        visited = visited[:-to_del]
                        current_word = current_word[:-1]

                    current_pos = last_pos

    def search_for_words(self):
        # für jede Zeile
        for index_r, row in enumerate(self.board):
            # für jeden Würfel
            for index_c, start_letter in enumerate(row):

                visited = [(index_r, index_c)]
                self.search_next_letter(start_letter, (index_r, index_c), visited)


if __name__ == "__main__":
    start_time = datetime.datetime.now()

    diction = Dictionary()
    for i in range(0, 26):
        letter = string.ascii_uppercase[i]
        print(letter)
        new_list = [x for x in DICTIONARY if x.startswith(letter)]

        setattr(diction, letter, new_list)

    game = Game()
    game.create_dice()
    game.roll()

    bb = BoggleBot(game.board, diction)
    bb.search_for_words()
    print(RESULTS)
    end_time = datetime.datetime.now()

    print("Dauer: " + str(end_time - start_time))
