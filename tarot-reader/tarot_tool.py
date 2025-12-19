"""Tarot card drawing tool with complete Rider-Waite tarot deck."""

import random
from typing import Dict, Any

# Complete Rider-Waite Tarot Deck (78 cards)
RIDER_WAITE_DECK = [
    # Major Arcana (22 cards)
    {"name": "The Fool", "suit": "Major Arcana", "number": 0, "meaning": "New beginnings, innocence, spontaneity, a free spirit"},
    {"name": "The Magician", "suit": "Major Arcana", "number": 1, "meaning": "Manifestation, resourcefulness, power, inspired action"},
    {"name": "The High Priestess", "suit": "Major Arcana", "number": 2, "meaning": "Intuition, sacred knowledge, divine feminine, the subconscious mind"},
    {"name": "The Empress", "suit": "Major Arcana", "number": 3, "meaning": "Femininity, beauty, nature, nurturing, abundance"},
    {"name": "The Emperor", "suit": "Major Arcana", "number": 4, "meaning": "Authority, establishment, structure, a father figure"},
    {"name": "The Hierophant", "suit": "Major Arcana", "number": 5, "meaning": "Spiritual wisdom, religious beliefs, conformity, tradition, conformity"},
    {"name": "The Lovers", "suit": "Major Arcana", "number": 6, "meaning": "Love, harmony, relationships, values alignment, choices"},
    {"name": "The Chariot", "suit": "Major Arcana", "number": 7, "meaning": "Control, willpower, success, action, determination"},
    {"name": "Strength", "suit": "Major Arcana", "number": 8, "meaning": "Strength, courage, persuasion, influence, compassion"},
    {"name": "The Hermit", "suit": "Major Arcana", "number": 9, "meaning": "Soul searching, introspection, being alone, inner guidance"},
    {"name": "Wheel of Fortune", "suit": "Major Arcana", "number": 10, "meaning": "Good luck, karma, life cycles, destiny, a turning point"},
    {"name": "Justice", "suit": "Major Arcana", "number": 11, "meaning": "Justice, fairness, truth, cause and effect, law"},
    {"name": "The Hanged Man", "suit": "Major Arcana", "number": 12, "meaning": "Pause, surrender, letting go, new perspectives"},
    {"name": "Death", "suit": "Major Arcana", "number": 13, "meaning": "Endings, change, transformation, transition"},
    {"name": "Temperance", "suit": "Major Arcana", "number": 14, "meaning": "Balance, moderation, patience, purpose"},
    {"name": "The Devil", "suit": "Major Arcana", "number": 15, "meaning": "Shadow self, attachment, addiction, restriction, sexuality"},
    {"name": "The Tower", "suit": "Major Arcana", "number": 16, "meaning": "Sudden change, upheaval, chaos, revelation, awakening"},
    {"name": "The Star", "suit": "Major Arcana", "number": 17, "meaning": "Hope, faith, purpose, renewal, spirituality"},
    {"name": "The Moon", "suit": "Major Arcana", "number": 18, "meaning": "Illusion, fear, anxiety, subconscious, intuition"},
    {"name": "The Sun", "suit": "Major Arcana", "number": 19, "meaning": "Positivity, fun, warmth, success, vitality"},
    {"name": "Judgement", "suit": "Major Arcana", "number": 20, "meaning": "Judgement, rebirth, inner calling, absolution"},
    {"name": "The World", "suit": "Major Arcana", "number": 21, "meaning": "Completion, accomplishment, travel, achievement, fulfillment"},
    
    # Wands (14 cards: Ace-10, Page, Knight, Queen, King)
    {"name": "Ace of Wands", "suit": "Wands", "number": 1, "meaning": "Inspiration, new opportunities, growth, potential"},
    {"name": "Two of Wands", "suit": "Wands", "number": 2, "meaning": "Planning, making decisions, leaving home"},
    {"name": "Three of Wands", "suit": "Wands", "number": 3, "meaning": "Looking ahead, expansion, rapid growth"},
    {"name": "Four of Wands", "suit": "Wands", "number": 4, "meaning": "Celebration, joy, harmony, relaxation"},
    {"name": "Five of Wands", "suit": "Wands", "number": 5, "meaning": "Competition, conflict, tension, diversity"},
    {"name": "Six of Wands", "suit": "Wands", "number": 6, "meaning": "Victory, success, public reward"},
    {"name": "Seven of Wands", "suit": "Wands", "number": 7, "meaning": "Challenge, competition, protection, perseverance"},
    {"name": "Eight of Wands", "suit": "Wands", "number": 8, "meaning": "Rapid action, movement, quick decisions"},
    {"name": "Nine of Wands", "suit": "Wands", "number": 9, "meaning": "Resilience, grit, last stand, persistence"},
    {"name": "Ten of Wands", "suit": "Wands", "number": 10, "meaning": "Accomplishment, responsibility, burden, hard work"},
    {"name": "Page of Wands", "suit": "Wands", "number": 11, "meaning": "Exploration, excitement, free spirit, lack of direction"},
    {"name": "Knight of Wands", "suit": "Wands", "number": 12, "meaning": "Action, adventure, fearlessness, energy"},
    {"name": "Queen of Wands", "suit": "Wands", "number": 13, "meaning": "Courage, confidence, independence, social butterfly"},
    {"name": "King of Wands", "suit": "Wands", "number": 14, "meaning": "Natural-born leader, vision, entrepreneur, honor"},
    
    # Cups (14 cards: Ace-10, Page, Knight, Queen, King)
    {"name": "Ace of Cups", "suit": "Cups", "number": 1, "meaning": "New feelings, spirituality, intuition, creativity"},
    {"name": "Two of Cups", "suit": "Cups", "number": 2, "meaning": "Unified love, partnership, mutual attraction"},
    {"name": "Three of Cups", "suit": "Cups", "number": 3, "meaning": "Friendship, community, happiness, celebrations"},
    {"name": "Four of Cups", "suit": "Cups", "number": 4, "meaning": "Apathy, contemplation, disconnectedness, melancholy"},
    {"name": "Five of Cups", "suit": "Cups", "number": 5, "meaning": "Loss, grief, self-pity, disappointment"},
    {"name": "Six of Cups", "suit": "Cups", "number": 6, "meaning": "Revisiting the past, childhood memories, innocence"},
    {"name": "Seven of Cups", "suit": "Cups", "number": 7, "meaning": "Opportunities, choices, wishful thinking, illusion"},
    {"name": "Eight of Cups", "suit": "Cups", "number": 8, "meaning": "Walking away, disillusionment, leaving behind"},
    {"name": "Nine of Cups", "suit": "Cups", "number": 9, "meaning": "Satisfaction, emotional stability, luxury, happiness"},
    {"name": "Ten of Cups", "suit": "Cups", "number": 10, "meaning": "Divine love, blissful relationships, harmony, alignment"},
    {"name": "Page of Cups", "suit": "Cups", "number": 11, "meaning": "Creative opportunities, intuitive messages, curiosity"},
    {"name": "Knight of Cups", "suit": "Cups", "number": 12, "meaning": "Following the heart, idealist, romantic, charming"},
    {"name": "Queen of Cups", "suit": "Cups", "number": 13, "meaning": "Compassionate, caring, emotionally stable, intuitive"},
    {"name": "King of Cups", "suit": "Cups", "number": 14, "meaning": "Emotional balance, compassion, diplomacy, control"},
    
    # Swords (14 cards: Ace-10, Page, Knight, Queen, King)
    {"name": "Ace of Swords", "suit": "Swords", "number": 1, "meaning": "Breakthrough, clarity, sharp mind, new ideas"},
    {"name": "Two of Swords", "suit": "Swords", "number": 2, "meaning": "Difficult choices, indecision, stalemate"},
    {"name": "Three of Swords", "suit": "Swords", "number": 3, "meaning": "Heartbreak, emotional pain, sorrow, grief"},
    {"name": "Four of Swords", "suit": "Swords", "number": 4, "meaning": "Rest, restoration, contemplation, recuperation"},
    {"name": "Five of Swords", "suit": "Swords", "number": 5, "meaning": "Unbridled ambition, win at all costs, sneakiness"},
    {"name": "Six of Swords", "suit": "Swords", "number": 6, "meaning": "Transition, leaving behind, moving on"},
    {"name": "Seven of Swords", "suit": "Swords", "number": 7, "meaning": "Deception, trickery, tactics, strategy"},
    {"name": "Eight of Swords", "suit": "Swords", "number": 8, "meaning": "Self-imposed restriction, imprisonment, victim mentality"},
    {"name": "Nine of Swords", "suit": "Swords", "number": 9, "meaning": "Anxiety, hopelessness, trauma, nightmares"},
    {"name": "Ten of Swords", "suit": "Swords", "number": 10, "meaning": "Betrayal, backstabbing, endings, rock bottom"},
    {"name": "Page of Swords", "suit": "Swords", "number": 11, "meaning": "New ideas, curiosity, thirst for knowledge, communication"},
    {"name": "Knight of Swords", "suit": "Swords", "number": 12, "meaning": "Action, impulsiveness, defending beliefs, fighting for justice"},
    {"name": "Queen of Swords", "suit": "Swords", "number": 13, "meaning": "Clear boundaries, direct communication, independence"},
    {"name": "King of Swords", "suit": "Swords", "number": 14, "meaning": "Mental clarity, intellectual power, authority, truth"},
    
    # Pentacles (14 cards: Ace-10, Page, Knight, Queen, King)
    {"name": "Ace of Pentacles", "suit": "Pentacles", "number": 1, "meaning": "New opportunity, resource, manifestation"},
    {"name": "Two of Pentacles", "suit": "Pentacles", "number": 2, "meaning": "Balancing priorities, time management, prioritization"},
    {"name": "Three of Pentacles", "suit": "Pentacles", "number": 3, "meaning": "Teamwork, collaboration, learning, implementation"},
    {"name": "Four of Pentacles", "suit": "Pentacles", "number": 4, "meaning": "Security, control, conservatism, scarcity"},
    {"name": "Five of Pentacles", "suit": "Pentacles", "number": 5, "meaning": "Need, poverty, insecurity, isolation"},
    {"name": "Six of Pentacles", "suit": "Pentacles", "number": 6, "meaning": "Giving, receiving, sharing wealth, generosity"},
    {"name": "Seven of Pentacles", "suit": "Pentacles", "number": 7, "meaning": "Hard work, perseverance, diligence, long-term view"},
    {"name": "Eight of Pentacles", "suit": "Pentacles", "number": 8, "meaning": "Skill development, quality, mastery, commitment"},
    {"name": "Nine of Pentacles", "suit": "Pentacles", "number": 9, "meaning": "Fruits of labor, rewards, luxury, self-sufficiency"},
    {"name": "Ten of Pentacles", "suit": "Pentacles", "number": 10, "meaning": "Legacy, culmination, inheritance, family"},
    {"name": "Page of Pentacles", "suit": "Pentacles", "number": 11, "meaning": "Manifestation, financial opportunity, skill development"},
    {"name": "Knight of Pentacles", "suit": "Pentacles", "number": 12, "meaning": "Efficiency, routine, conservatism, responsibility"},
    {"name": "Queen of Pentacles", "suit": "Pentacles", "number": 13, "meaning": "Practicality, creature comforts, financial security, nurturing"},
    {"name": "King of Pentacles", "suit": "Pentacles", "number": 14, "meaning": "Abundance, prosperity, security, achievement"},
]


def draw_tarot_cards(num_cards: int) -> Dict[str, Any]:
    """Draw a specified number of tarot cards from a shuffled Rider-Waite deck.
    
    This function shuffles the complete 78-card Rider-Waite tarot deck and returns
    the requested number of cards from random positions.
    
    Args:
        num_cards: The number of cards to draw (must be between 1 and 78).
        
    Returns:
        A dictionary containing:
        - 'cards': List of drawn card dictionaries, each with 'name', 'suit', 'number', and 'meaning'
        - 'num_drawn': The number of cards drawn
        - 'status': 'success' or 'error'
        - 'message': Status message
        
    Example:
        result = draw_tarot_cards(3)
        # Returns 3 random cards from the deck
    """
    if num_cards < 1 or num_cards > 78:
        return {
            "status": "error",
            "message": f"Number of cards must be between 1 and 78. You requested {num_cards}.",
            "cards": [],
            "num_drawn": 0
        }
    
    # Create a copy of the deck and shuffle it
    shuffled_deck = RIDER_WAITE_DECK.copy()
    random.shuffle(shuffled_deck)
    
    # Draw the requested number of cards
    drawn_cards = shuffled_deck[:num_cards]
    
    return {
        "status": "success",
        "message": f"Successfully drew {num_cards} card(s) from the Rider-Waite tarot deck.",
        "cards": drawn_cards,
        "num_drawn": num_cards
    }

