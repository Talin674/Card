class Card(object):
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]
    def __init__(self, rank, suit, face_up=True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up
    def __str__(self):
        if self.is_face_up:
            ret = self.rank + self.suit
        else:
            ret = "XX"
        return ret
    def flip(self):
        self.is_face_up = not self.is_face_up

class Hand(object):
    def __init__(self):
        self.cards = []
    def __str__(self):
        ret = ""
        if self.cards:
            for card in self.cards:
                ret += str(card) + " "
        else:
            ret = "пусто"
        return ret
    def add(self, card):
        self.cards.append(card)
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)
    def clear(self):
        self.cards = []

class Deck(Hand):
    def populate(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self, hands, per_hand=1):
        for r in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print('Нет карт')


if __name__ == "__main__":
    print('Это модуль с описание класса карты')
    print("Проверка")
