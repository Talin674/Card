import cards, games
class BJ_Card(cards.Card):
    #Карта для игры в блэк джек
    ACE_VALUE = 1
    @property
    def value(self):
        if self.is_face_up: 
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
                print("D")
        else:
            v = None
        return v

class BJ_Deck(cards.Deck):
    #колода
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))
class BJ_Hand(cards.Hand):
    #рука игрока
    def __init__(self, name):
        self.name = name
        super(BJ_Hand, self).__init__()
    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        for card in self.cards:
            t += card.value
        containse_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                containse_ace = True
        if containse_ace and t <= 11:
            t += 10
        return t
    def is_buasted(self):
        return self.total > 21

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

class BJ_Player(BJ_Hand):
    #игрок
class BJ_Diler(BJ_Hand):
    #дилер
class BJ_Game(object):
    #игра блэк джек

