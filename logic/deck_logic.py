from infra.api_wrapper import DeckOfCardsAPI

class deckLogic(DeckOfCardsAPI):

 def create_new_shuffled_deck(self):
    api = DeckOfCardsAPI()
    response = api.new_deck(shuffle=True)
    return response.json()

 def draw_from_deck(deck_id, num_cards):
    api = DeckOfCardsAPI()
    response = api.draw_cards(deck_id, num_cards)
    return response.json()


 def shuffle_existing_deck(deck_id):
    api = DeckOfCardsAPI()
    response = api.shuffle_deck(deck_id)
    return response.json()

 def draw_specific_number_of_cards(deck_id, num_cards):
    api = DeckOfCardsAPI()
    response = api.draw_cards(deck_id, num_cards)
    return response.json()


 def reshuffle_deck(deck_id):
    api = DeckOfCardsAPI()
    response = api.reshuffle_deck(deck_id)
    print(response.json())
    return response.json()

 def get_deck_info(deck_id):
    api = DeckOfCardsAPI()
    response = api.get_deck(deck_id)
    return response.json()