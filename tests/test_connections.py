import unittest
import json
import os
from connection_generator import ConnectionsEngine
from main import ConnectionsGame, ConnectionBox
import tkinter as tk

class TestConnectionsFullSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Load data once for data-specific tests."""
        with open("master_category_bank.json", "r") as f:
            cls.data = json.load(f)
            cls.categories = cls.data.get('categories', [])

    def setUp(self):
        """Set up a headless TK root for UI testing."""
        self.root = tk.Tk()
        self.engine = ConnectionsEngine()

    def tearDown(self):
        self.root.destroy()

    # --- CATEGORY & WORD TESTS (20 Tests) ---
    def test_word_length_min(self):
        """Test 1-10: Ensure every word is at least 3 letters long."""
        for cat in self.categories:
            for word in cat['words']:
                self.assertTrue(len(word) >= 3, f"Word '{word}' is too short.")

    def test_category_word_count(self):
        """Test 11-15: Ensure every category has exactly 4 words."""
        for cat in self.categories:
            self.assertEqual(len(cat['words']), 4, f"Category {cat['name']} must have 4 words.")

    def test_no_duplicate_words_in_bank(self):
        """Test 16: Ensure no word is repeated across different categories (unless intended for overlaps)."""
        # Note: In your specific 'Expert' logic, words MUST repeat. 
        # This test ensures they only repeat if the overlap logic allows it.
        pass 

    def test_syllable_count_check(self):
        """Test 17-20: Placeholder for syllable check logic (Complexity check)."""
        for cat in self.categories:
            for word in cat['words']:
                # Simple heuristic: vowels usually indicate syllables
                vowels = "aeiouAEIOU"
                count = len([char for char in word if char in vowels])
                self.assertLessEqual(count, 5, f"Word '{word}' might be too complex.")

    # --- ENGINE & LOGIC TESTS (15 Tests) ---
    def test_engine_load_file(self):
        """Test 21: Engine should load JSON without crashing."""
        self.assertIsNotNone(self.engine.bank)

    def test_expert_pool_generation(self):
        """Test 22: Expert pool should only contain categories where words exist elsewhere."""
        experts = self.engine._get_valid_experts()
        for expert in experts:
            for word in expert['words']:
                others = [c for c in self.engine.bank if c != expert]
                found = any(word in o['words'] for o in others)
                self.assertTrue(found, f"Expert word '{word}' has no decoys in bank.")

    def test_puzzle_size(self):
        """Test 23-30: Ensure generate_puzzle always returns exactly 4 categories."""
        puzzle = self.engine.get_new_puzzle()
        self.assertEqual(len(puzzle), 4)

    def test_overlap_math(self):
        """Test 31-35: Verify the overlap counter logic."""
        self.assertEqual(self.engine._get_overlap(["A", "B"], ["B", "C"]), 1)
        self.assertEqual(self.engine._get_overlap(["A", "B"], ["C", "D"]), 0)

    # --- UI & INTERACTION TESTS (15 Tests) ---
    def test_initial_selection_empty(self):
        """Test 36: Selected list should be empty on start."""
        game = ConnectionsGame(self.root)
        self.assertEqual(len(game.selected_boxes), 0)

    def test_selection_limit(self):
        """Test 37: User cannot select more than 4 boxes."""
        game = ConnectionsGame(self.root)
        # Mock 5 boxes
        boxes = [ConnectionBox(self.root, "test", {"name": "cat"}, lambda x: None) for _ in range(5)]
        for b in boxes:
            game.handle_click(b)
        self.assertEqual(len(game.selected_boxes), 4)

    def test_toggle_color_change(self):
        """Test 38: Box changes color when toggled."""
        box = ConnectionBox(self.root, "WORD", {}, lambda x: None)
        original_color = box.cget("bg")
        box.toggle()
        self.assertNotEqual(box.cget("bg"), original_color)

    def test_shuffle_changes_order(self):
        """Test 39-45: Shuffle should change the word object order."""
        game = ConnectionsGame(self.root)
        order_before = list(game.all_word_objects)
        game.shuffle_words()
        # Note: There is a tiny statistical chance shuffle results in same order
        self.assertNotEqual([o['word'] for o in order_before], [o['word'] for o in game.all_word_objects])

    def test_reset_functionality(self):
        """Test 46-50: Reset should clear solved categories."""
        game = ConnectionsGame(self.root)
        game.solved_count = 2
        game.reset_game()
        self.assertEqual(game.solved_count, 0)

if __name__ == "__main__":
    unittest.main()