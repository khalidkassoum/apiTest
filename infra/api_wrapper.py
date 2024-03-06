import requests


class DeckOfCardsAPI:
    BASE_URL = 'https://deckofcardsapi.com/api/deck'

    def new_deck(self, shuffle=False):
        path = '/new/' + ('shuffle/' if shuffle else '')
        return requests.get(f'{self.BASE_URL}{path}')

    def draw_cards(self, deck_id, count=1):
        return requests.get(f'{self.BASE_URL}/{deck_id}/draw/?count={count}')

    def shuffle_deck(self, deck_id):
        return requests.get(f'{self.BASE_URL}/{deck_id}/shuffle/')

    def reshuffle_deck(self, deck_id):
        return requests.get(f'{self.BASE_URL}/{deck_id}/shuffle/')

    def get_deck(self, deck_id):
        return requests.get(f'{self.BASE_URL}/{deck_id}/')