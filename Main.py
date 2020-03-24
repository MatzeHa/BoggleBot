# BoggleBot - Search words in a 4*4 square of letters #

import string
import random

LETTERS_str = string.ascii_uppercase[0:27]
LETTERS = [x for x in LETTERS_str]

DIRECTIONS = [(-1, -1), (0, -1), (1, -1),
              (-1, 0), (1, 0),
              (-1, 1), (0, 1), (1, 1)]

if __name__ == "__main__":
    '''
    class Game:
        def __init__(self):
            self.dice = []
            self.board = [["", "", "", ""],
                          ["", "", "", ""],
                          ["", "", "", ""],
                          ["", "", "", ""]]

        def create_dice(self):
            dice = []
            for j in range(16):
                _dice = []
                for i in range(6):
                    _dice.append(random.choice(LETTERS))
                dice.append(_dice)
            self.dice = dice

        def roll(self):
            for index_r, row in enumerate(self.board):
                for index_c, col in enumerate(row):
                    self.board[index_r][index_c] = random.choice(self.dice[index_c + index_r])


    class BoggleBot:
        def __init__(self):
            self.results = []

        def search_for_words(self, board):
            # für jede Zeile
            for index_r, row in enumerate(board):
                # für jeden Würfel
                for index_c, start_letter in enumerate(row):            # 1
                    letter_exhausted = False
                    try_word = start_letter

                    visited = [(index_c, index_r)]

                    while not letter_exhausted:
                        # für jede Richtung
                        for d in DIRECTIONS:
                            search_next = (index_c + d[0], index_r + d[1])
                            if 0 <= search_next[0] < 4 and 0 <= search_next[1] < 4:
                                try_word = "".join((try_word, board[search_next[0]][search_next[1]]))
                                visited.append(search_next)






    game = Game()
    game.create_dice()
    game.roll()

    bb = BoggleBot()
    bb.search_for_words(game.board)
    '''



    class WebChecker:
        def __init__(self):
            from selenium import webdriver
            from selenium.webdriver.firefox.options import Options
            # from selenium.webdriver.common.keys import Keys

            options = Options()
            # options.add_argument('--headless')
            # options.add_argument('--disable-gpu')  # Last I checked this was necessary.[sic]

            self.search = ""

            self.driver = webdriver.Firefox(options=options)
            self.driver.get("http://www.duden.de")

            #assert "duden" in self.driver.title  # checkt ob "Duden" im Titel steht, wirft exception

        def search_word(self, word):
            # wollte cookiebutton ausstellen...
            # elem = driver.find_element_by_xpath(".//*[@class='button']") #eigentlcih egal für meinezwecke
            # elem.click()

            elem = self.driver.find_element_by_name("search_api_fulltext")
            elem.clear()
            elem.send_keys(word)
            self.search = word

        def find_suggestions(self):
            elem = self.driver.find_elements_by_class_name("form-asap__guess-title")
            words = []
            for word in elem:
                print(word.text)
                words.append(self.clean_words(word.text))
            words = [x for x in words if x]
            print(words)
            # assert "No results found." not in driver.page_source
            # driver.close()

        def clean_words(self, messed):
            messed = messed.lower()
            cleaned = messed.replace("­", "")

            if cleaned.startswith(self.search):
                return cleaned


    web_check = WebChecker()
    web_check.search_word("erlebt")
    import time
    time.sleep(.5)
    web_check.find_suggestions()

    while True:
        check_word = input()
        web_check.search_word(check_word)
        time.sleep(.5)
        web_check.find_suggestions()
