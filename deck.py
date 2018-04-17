import random
import factory


def singleton(cls):
    instances = {}

    def get_instance(*arg):
        if cls not in instances:
            instances[cls] = cls(*arg)
        return instances[cls]
    return get_instance


@singleton
class Deck:
    """
    Class Deck for Pyramid.

    Implements the functional of the deck:
    Create new deck.
    Shuffle deck.
    Open/get/delete cards.
    Allocation of a card for a pyramid.

    """
    def __init__(self):
        """
        Description of attributes deck.

        """
        self.__deck = []
        self.__number_of_open_cards = 0
        self.__stack_open_cards = [[]]

    def new_deck(self, number_of_open_cards=1, number_of_decks=1, type_card='english'):
        """
        Create deck and stacks for open cards.

        :param number_of_open_cards: the number of cards opened at once
        :param number_of_decks: the number of collections cards used
        :param type_card: type card

        """
        
        if type_card == 'english':
            self.__deck = factory.CreateEnglishDeck().create_deck(number_of_decks)

        self.__number_of_open_cards = number_of_open_cards

        self.__stack_open_cards = [[] for i in range(self.__number_of_open_cards)]

    def shuffle(self):
        """
        Shuffle deck.

        """
        random.shuffle(self.__deck)

    def open_cards(self):
        """
        Opens cards from deck.

        :return: 1 if the cards were opened 0 otherwise

        """
        if len(self.__deck) == 0:
            return 0
        for i in range(self.__number_of_open_cards):
            if len(self.__deck) == 0:
                break
            current_card = self.__deck.pop()
            self.__stack_open_cards[i].append(current_card)
        return 1

    def get_open_card(self, number_stack):
        """
        Returns the card face of said stack.

        :param number_stack: indicates stack
        :return: card or None

        """
        if len(self.__stack_open_cards[number_stack]) > 0:
            return self.__stack_open_cards[number_stack][-1]
        return None

    def take_open_card(self, number_stack):
        """
        Deletes the card face of said stack.

        :param number_stack: indicates stack
        :return: card or None

        """
        if len(self.__stack_open_cards[number_stack]) > 0:
            return self.__stack_open_cards[number_stack].pop()
        return None

    def collect_deck(self):
        """
        Collects a deck of stacks

        """
        if len(self.__deck) == 0:
            max_cards = -1
            for i in range(self.__number_of_open_cards):
                if len(self.__stack_open_cards[i]) > max_cards:
                    max_cards = len(self.__stack_open_cards[i])
            while max_cards:
                for i in range(self.__number_of_open_cards - 1, -1, -1):
                    if len(self.__stack_open_cards[i]) > 0:
                        self.__deck.append(self.__stack_open_cards[i].pop())
                max_cards -= 1

    def create_pyramid(self, size):
        """
        Allocation of card for the structure of the pyramid.

        :param size: pyramid size
        :return: list with cards

        """
        pyramid = [[None for j in range(0, i + 1)] for i in range(0, size)]
        for i in range(size):
            for j in range(i+1):
                pyramid[i][j] = self.__deck.pop()
        return pyramid

    def __str__(self):
        s = ''
        for i in self.__deck:
            s = s + str(i.rank)+ ' ' + str(i.suit)+'\n'
        return s
