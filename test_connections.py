import unittest
from collections import Counter
import connections  # Imports your main game file

class TestConnectionsGame(unittest.TestCase):
    """
    Gold Standard Test Suite for Connections Game.
    Verifies data integrity and game logic simulation.
    """

    def setUp(self):
        """Runs before every test. Loads the game data."""
        self.categories = connections.GameData.get_categories()
        
        # Flatten the data for easier testing
        self.all_words = []
        for key, data in self.categories.items():
            for word in data["words"]:
                self.all_words.append(word)

    # --- DATA INTEGRITY TESTS ---
    
    def test_total_word_count(self):
        """Verify there are exactly 16 words in total."""
        self.assertEqual(len(self.all_words), 16, "Game must have exactly 16 words.")

    def test_category_structure(self):
        """Verify there are exactly 4 categories with 4 words each."""
        self.assertEqual(len(self.categories), 4, "Must have 4 difficulty categories.")
        for cat_name, data in self.categories.items():
            self.assertEqual(len(data['words']), 4, f"Category '{cat_name}' must have exactly 4 words.")

    def test_word_length_constraint(self):
        """Verify strict rule: Words must be at least 3 letters long."""
        for word in self.all_words:
            self.assertTrue(len(word) >= 3, f"Word '{word}' violates the 3-letter minimum rule.")

    def test_uniqueness_constraint(self):
        """Verify strict rule: Words must not be repeated across categories."""
        word_counts = Counter(self.all_words)
        duplicates = [word for word, count in word_counts.items() if count > 1]
        self.assertEqual(len(duplicates), 0, f"Found duplicate words: {duplicates}")

    # --- LOGIC SIMULATION TESTS ---

    def helper_calculate_closeness(self, selected_words):
        """
        Helper function that replicates the game's submission logic 
        to test the 'One Off' / 'Two Off' algorithms without needing the GUI.
        """
        category_counts = {}
        for word in selected_words:
            # Find which category this word belongs to
            found = False
            for key, data in self.categories.items():
                if word in data["words"]:
                    category_counts[key] = category_counts.get(key, 0) + 1
                    found = True
                    break
        
        if not category_counts:
            return 0
            
        return max(category_counts.values())

    def test_logic_winner(self):
        """Simulate selecting 4 words from the 'Easy' category."""
        selection = ["COD", "BASS", "TUNA", "PERCH"]
        max_matches = self.helper_calculate_closeness(selection)
        self.assertEqual(max_matches, 4, "Should identify 4 matching words.")

    def test_logic_one_off(self):
        """
        Simulate 'One Off' scenario:
        3 words from Easy (COD, BASS, TUNA) + 1 from Hard (WAR).
        """
        selection = ["COD", "BASS", "TUNA", "WAR"]
        max_matches = self.helper_calculate_closeness(selection)
        self.assertEqual(max_matches, 3, "Logic should detect 'One Off' (3 matches).")

    def test_logic_two_off(self):
        """
        Simulate 'Two Off' scenario:
        2 words from Easy (COD, BASS) + 2 from Hard (WAR, GIN).
        """
        selection = ["COD", "BASS", "WAR", "GIN"]
        max_matches = self.helper_calculate_closeness(selection)
        self.assertEqual(max_matches, 2, "Logic should detect 'Two Off' (2 matches).")

if __name__ == '__main__':
    unittest.main()
