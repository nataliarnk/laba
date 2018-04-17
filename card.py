class Card(object):
    """
    Class for representing a card.

    The class describing the card: suit, rank, value.

    """
    def __init__(self, rank, suit, type_card='english'):
        """
        Give the card its attributes.

        :param rank: card rank
        :param suit: card suit
        :param type_cards: card type

        """
        type_card = 'english'
        self.__card_type = type_card
        suits = None
        ranks = None

        if self.__card_type == 'english':
            suits = ['spades', 'clubs', 'hearts', 'diamonds']
            ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']


        assert suit in suits, 'wrong suit'
        assert rank in ranks, 'wrong rank'

        self.__rank = rank
        self.__suit = suit

        self.__value = 0
        for i in range(len(ranks)):
            if self.__rank == ranks[i]:
                self.__value = i + 1
                break

    @property
    def card_type(self):
        """
        :return: card type
        """
        return self.__card_type

    @property
    def rank(self):
        """
        :return: card rank
        """
        return self.__rank

    @property
    def suit(self):
        """
        :return: card suit
        """
        return self.__suit

    @property
    def value(self):
        """
        :return: card value
        """
        return self.__value

    def __str__(self):
        return str(self.__rank) + " " + str(self.__suit)
