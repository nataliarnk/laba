from card import Card


class PyramidBoard():
    """
    Class for representing the pyramid structure.

    Class describes the structure of the pyramid and its functional:
    Create pyramid.
    Show pyramid.
    Checking the presence, obtaining, deleting cards.

    """
    def __init__(self):
        """
        Description of attributes deck.

        """
        self.__pyramid = []
        self.__size = 0
        self.__skeleton = []

    def create_pyramid(self, pyramid, size="small"):
        """
        Create pyramid.

        :param pyramid: pyramid for copy.
        :param size: size pyramid: big = 9, small = 7

        """
        sizes = ['small', 'big']
        assert size in sizes, 'wrong size'
        if size == "small":
            self.__size = 7
        elif size == 'big':
            self.__size = 9
        self.__pyramid = [[None] * (i + 1) for i in range(0, self.__size)]
        for i in range(self.__size):
            for j in range(i+1):
                self.__pyramid[i][j] = pyramid[i][j]

    def card_contains(self, i, j):
        """
        Check the availability of a card.

        :param i: line in pyramid
        :param j: column in pyramid
        :return: 1 if the card is found, 0 if the map location is None, -1 if the coordinates are outside the pyramid

        """
        if i > self.__size - 1 or i < 0 or j > i or j < 0:
            return -1
        if type(self.__pyramid[i][j]) == Card:
            return 1
        else:
            return 0

    def get_card(self, i, j):
        """
        Return card.

        :param i: line in pyramid
        :param j: column in pyramid
        :return: Card if card is found, -1 else

        """
        if self.card_contains(i, j) == 1:
            return self.__pyramid[i][j]
        else:
            return -1

    def usability_card(self, i , j):
        """
        Check for openness of the card.

        :param i: line in pyramid
        :param j: column in pyramid
        :return: Card if card is usability, 0 else

        """
        if self.card_contains(i, j) == 1 and ((i < self.__size - 1 and type(self.__pyramid[i + 1][j]) != Card and
                type(self.__pyramid[i + 1][j + 1]) != Card) or (i == self.__size - 1)):
            return 1
        else:
            return 0

    def delete_card(self, i, j):
        """
        Delete card.

        :param i: line in pyramid
        :param j: column in pyramid
        :return: Card if can remove the card, None else

        """
        if self.usability_card(i, j):
            card_ = self.__pyramid[i][j]
            self.__pyramid[i][j] = None
            return card_
        return None

    def show(self):
        for i in range(self.__size):
            for j in range(i+1):
                if type(self.__pyramid[i][j]) == Card:
                    print('[' + self.__pyramid[i][j].rank + ' ' + self.__pyramid[i][j].suit + ']', end=' ')
                else:
                    print('[None]', end=' ')
            print()
