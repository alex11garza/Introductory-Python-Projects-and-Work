import random


class Card:
    def __init__(self, s, v):
        self.suit = s
        self.value = v

    def __str__(self):
        if self.value < 11:
            val = str(self.value)
        elif self.value == 11:
            val = 'Jack'
        elif self.value == 12:
            val = 'Queen'
        elif self.value == 13:
            val = 'King'
        elif self.value == 14:
            val = 'Ace'
        return val + ' of ' + self.suit

    def get_value(self):
        if self.value < 11:
            score = self.value
        elif 11 <= self.value <= 13:
            score = 10
        elif self.value == 14:
            score = 11
        return score


class DeckOfCards:
    def __init__(self):
        self.deck = []
        suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
        for s in suits:
            for i in range(2, 15):
                self.deck.append(Card(s, i))

    def print(self):
        for card in self.deck:
            print(card)

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop(0)


class Dealer:
    def __init__(self):
        self.name = 'Dealer'
        self.hand = []

    def __str__(self):
        return self.name + ': ' + str(self.hand[0]) + '; ' + str(self.hand[1])

    def get_hand_value(self):
        return sum([card.get_value() for card in self.hand])

    def add_card(self, card):
        self.hand.append(card)


class Player:
    def __init__(self, name, starting_money):
        self.name = name
        self.money = starting_money
        self.hand = []

    def __str__(self):
        return self.name + ': ' + str(self.hand[0]) + '; ' + str(self.hand[1])

    def add_card(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        hand_value = sum([card.get_value() for card in self.hand])
        if hand_value > 21 and any([card.value == 14 for card in self.hand]):
            hand_value -= 10
        return hand_value


def deal_round(players, dealer, card_deck):
    dealer.hand = []
    for player in players:
        player.hand = []
    for player in players:
        i = 0
        while i < 2:
            player.add_card(card_deck.draw_card())
            i += 1
    t = 0
    while t < 2:
        dealer.add_card(card_deck.draw_card())
        t += 1
    print(dealer)
    for player in players:
        print(player)


def get_winners(players, dealer):
    dealer_score = dealer.get_hand_value()
    for player in players:
        player_score = player.get_hand_value()
        if player_score < dealer_score:
            player.money -= 5
        elif player_score == dealer_score:
            player.money = player.money
        elif player_score > dealer_score:
            player.money += 5
        print(player.name, player.money)


def play_game():
    deck = DeckOfCards()
    deck.shuffle()
    players = [Player('Sonia', 100), Player('Alex', 50), Player('Alex G', 200), Player('David', 200), Player('Lorena', 200),
               Player('Anh-Thu', 200)]

    dealer = Dealer() 
    deal_round(players, dealer, deck)
    get_winners(players, dealer)
    
def main():
    play_game()

if __name__ == '__main__':
    main()

