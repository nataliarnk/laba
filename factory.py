from card import Card
from abc import ABCMeta, abstractmethod


class ABSFactory(metaclass=ABCMeta):

    @abstractmethod
    def create_deck(self):
        raise NotImplementedError


class CreateEnglishDeck(ABSFactory):

    def create_deck(self, n=1):
        ranks_list = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
        suits_list = ['spades', 'clubs', 'hearts', 'diamonds']
        deck = []

        for k in range(n):
            for i in suits_list:
                for j in ranks_list:
                    deck.append(Card(j, i))

        return deck


