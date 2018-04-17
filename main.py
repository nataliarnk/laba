from deck import Deck
from pyramid import PyramidBoard



class Game:
    def __init__(self):
        self.__deck = Deck()
        self.__pyramid = PyramidBoard()
        self.__number_of_open_cards = 1
        self.__number_of_decks = 1
        self.__size = "small"
        self.__hard_suit = False

    def new_game(self, number_of_open_cards=1, number_of_decks=1, size="small", hard=False):
        self.__number_of_decks = number_of_decks
        self.__number_of_open_cards = number_of_open_cards

        self.__deck.new_deck(number_of_open_cards=number_of_open_cards, number_of_decks=number_of_decks)
        self.__deck.shuffle()

        if size == "small":
            self.__size = 7
            self.__pyramid.create_pyramid(self.__deck.create_pyramid(self.__size), "small")


        self.__hard_suit = hard

    def show_game(self):
        self.__pyramid.show()
        print()
        for i in range(self.__number_of_open_cards):
            print(self.__deck.get_open_card(i), end=' '*5)
        print()
        

    def open_cards(self):
        self.__deck.open_cards()

    def delete_cards_pyr(self, i1, j1, i2, j2):
        i1 -= 1
        i2 -= 1
        j1 -= 1
        j2 -= 1
        print(self.__pyramid.get_card(i1, j1).value + self.__pyramid.get_card(i2,j2).value)
        if (self.__pyramid.usability_card(i1, j1) != -1 and
            self.__pyramid.usability_card(i2, j2) != -1 and
                self.__pyramid.get_card(i1, j1).value + self.__pyramid.get_card(i2, j2).value == 13):
            if self.__hard_suit:
                if self.__pyramid.get_card(i1, j1).suit == self.__pyramid.get_card(i2, j2).suit:
                    self.__pyramid.delete_card(i1, j1)
                    self.__pyramid.delete_card(i2, j2)
            else:
                self.__pyramid.delete_card(i1, j1)
                self.__pyramid.delete_card(i2, j2)

    def delete_cards_pye_deck(self, i1, j1, i):
        i1 -= 1
        j1 -= 1
        i -= 1
        if (self.__pyramid.usability_card(i1, j1) and
                self.__pyramid.get_card(i1, j1).value + self.__deck.get_open_card(i).value == 13):
            if self.__hard_suit:
                if self.__pyramid.get_card(i1, j1).suit == self.__deck.get_open_card(i).suit:
                    self.__pyramid.delete_card(i1, j1)
                    self.__deck.take_open_card(i)
            else:
                self.__pyramid.delete_card(i1, j1)
                self.__deck.take_open_card(i)

    def delete_one_card(self, i, j):
        i -= 1
        j -= 1
        if self.__pyramid.get_card(i, j).value == 13:
            self.__pyramid.delete_card(i, j)

    def collect_deck(self):
        self.__deck.collect_deck()

if __name__ == "__main__":
    game = Game()
    while True:
        number_of_open_cards = 1
        number_of_decks = 1
        size = "small"
        hard = False
        game.new_game(number_of_open_cards, number_of_decks, size, hard)
        while True:
            game.show_game()
            choice = int(input('1 - open Deck\n'
                               '2 - choice Cards in Pyramid\n'
                               '3 - choice Cards in Pyramid and Deck\n'
                               '4 - choice one Card in Pyramid\n'
                               '5 - collect Deck\n'
                               '0 - New game\n'
                               'Your choice: '))
            if choice == 1:
                game.open_cards()
            elif choice == 2:
                i1 = int(input("Line first card: "))
                j1 = int(input("Number first card: "))
                i2 = int(input("Line second card: "))
                j2 = int(input("Number second card: "))
                game.delete_cards_pyr(i1, j1, i2, j2)
            elif choice == 3:
                i1 = int(input("Line card in pyr: "))
                j1 = int(input("Number card in pyr: "))
                i = 1
                game.delete_cards_pye_deck(i1, j1, i)
            elif choice == 4:
                i = int(input("Line card in pyr: "))
                j = int(input("Number card in pyr: "))
                game.delete_one_card(i, j)
            elif choice == 5:
                game.collect_deck()
            elif choice == 0:
                break
