import unittest
import pytest
from logic.deck_logic import deckLogic

class test_decks(unittest.TestCase):

 deckk=deckLogic()
 def test_create_and_draw_from_deck(self):

    num_cards_to_draw = 2
    deck = self.deckk.create_new_shuffled_deck()
    deck_id = deck['deck_id']
    draw_response = deckLogic.draw_from_deck(deck_id, num_cards_to_draw)
    assert deck['success'] is True
    assert deck['shuffled'] is True
    assert draw_response['success'] is True
    assert len(draw_response['cards']) == num_cards_to_draw



 def test_shuffle_existing_deck(self):

    deck = self.deckk.create_new_shuffled_deck()
    deck_id = deck['deck_id']
    shuffled_deck = deckLogic.shuffle_existing_deck(deck_id)
    assert shuffled_deck['success'] is True
    assert shuffled_deck['shuffled'] is True

 def test_draw_specific_number_of_cards(self):

    num_cards_to_draw = 3
    deck = self.deckk.create_new_shuffled_deck()
    deck_id = deck['deck_id']
    cards_drawn = deckLogic.draw_specific_number_of_cards(deck_id, num_cards_to_draw)
    assert cards_drawn['success'] is True
    assert len(cards_drawn['cards']) == num_cards_to_draw



 def test_reshuffle_deck(self):

    deck = self.deckk.create_new_shuffled_deck()
    deck_id = deck['deck_id']
    deckLogic.draw_from_deck(deck_id, 5)
    reshuffled_deck = deckLogic.reshuffle_deck(deck_id)
    assert reshuffled_deck['success'] is True
    assert reshuffled_deck['shuffled'] is True
    assert reshuffled_deck['remaining'] == 52, "Reshuffled deck should have all cards."

 def test_get_deck_info(self):

    deck = self.deckk.create_new_shuffled_deck()
    deck_id = deck['deck_id']
    deck_info = deckLogic.get_deck_info(deck_id)
    assert deck_info['success'] is True
    assert deck_info['deck_id'] == deck_id
    assert 'shuffled' in deck_info
    assert 'remaining' in deck_info

 @pytest.mark.parametrize("num_cards_to_draw", [1, 2, 3])
 def test_draw_multiple_cards(self, num_cards_to_draw):
    deck = self.deckk.create_new_shuffled_deck()
    deck_id = deck['deck_id']
    draw_response = deckLogic.draw_from_deck(deck_id, num_cards_to_draw)
    assert draw_response['success'] is True
    assert len(draw_response['cards']) == num_cards_to_draw

