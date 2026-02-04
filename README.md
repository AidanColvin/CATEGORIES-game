# Connections Word Game

A Python-based word puzzle game inspired by the popular Connections game. Players must identify groups of four related words from a grid of 16 words across four difficulty categories.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [Category System](#category-system)
- [Word Requirements](#word-requirements)
- [Controls](#controls)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Overview

Connections is a word categorization puzzle where players are presented with 16 words that belong to 4 hidden categories. The objective is to identify all four groups by selecting sets of 4 related words.


""""
Rules

Categories - There are 4 categories, each category has a different level of difficulty (easy, medium, hard, expert)
Category should be related to the words in other categories (e.g. if the category is "animals", the other categories could be "colors", "fruits", "countries", etc.)
Categories should not be related to spelling or grammar (e.g. "verbs", "nouns", "adjectives", etc.)
Categories should not be related to root of words or adding a letter to the end or beginning of a word (e.g. "cat", "cats", "catty", etc.)

Words should be atleast 3 letters long
Words should be related to each other in some way (e.g. they could all be animals, or they could all be colors, etc.)
Words should be related to the category they are in (e.g. if the category is "animals", the words should be related to animals)
Words should be unique and not repeated in other categories (e.g. if the word "cat" is in the "animals" category, it should not be in the "colors" category)
Words should not be over 3 syllables long
Words should be common words that are easily recognizable and not obscure or technical terms (e.g. "cat", "dog", "red", "blue", etc.)

Total of 16 words
4 words in each category
4 categories in total


Words should be displayed in a random order each time the program is run, and the categories should also be displayed in a random order each time the program is run
Each Word should be displayed in its own single box with a border around it
Boxs should be displayed in a grid format with 4 boxes in each row and 4 rows in total

User should be able to click on a box to select the word inside, and the box should change color when clicked
Users should be able to click on a box again to deselect the word inside, and the box should change back to its original color when clicked again
When a user clicks on a box, the word inside should be added to a list of selected words, and when a user clicks on a box again to deselect it, the word should be removed from the list of selected words
When the user has selected 4 words, and presses submit buttom or the return button the program should check if the selected words are all in the same category, and if they are, the program should display the name of the category and all boxs should be changed to the categories color 
The category should be displayed above the boxes in a larger font size.     
If the selected words are not all in the same category, the program should display a message saying # of words off if 3 are corect say one off if 2 correct say 2 off otherwise say try again

Users should be able to reset the game at any time by pressing a reset button, which will clear the list of selected words, reset the colors of all boxes to their original color, and display a new set of words and categories in a random order.
Users should be able to shuffle the words at any time by pressing a shuffle button, which will display a new order of the same words and categories in a random order without resetting the game or clearing the list of selected words.
Users are able to have for submiting their answer by pressing the return button on their keyboard or clicking the submit button.

"""

# Category 1 - Easy (LIGHT SOFT GREEN)
# Genarate a series of 4 words, each word should be 3 letters long, and the words should be related to each other in some way. 

# Category 2 - Medium (LIGHT SOFT BLUE)
# Genarate a series of 4 words, each word should be 3 letters long, and the words should be related to each other in some way. 

# Category 3 - Hard (LIGHT SOFT YELLOW)
# Genarate a series of 4 words, each word should be 3 letters long, and the words should be related to each other in some way.

# Category 4 - Expert (LIGHT SOFT RED)
# Genarate a series of 4 words, each word should be 3 letters long, and the words should be related to each other in some way.

## Features

- **4 Difficulty Levels**: Easy, Medium, Hard, and Expert categories
- **Interactive Grid**: Click to select/deselect words from a 4×4 grid
- **Visual Feedback**: Color-coded categories and selection states
- **Shuffle Functionality**: Randomize word positions without resetting progress
- **Reset Option**: Start a new game at any time
- **Keyboard Support**: Submit answers using Enter/Return key
- **Smart Validation**: Provides helpful feedback when selections are incorrect

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/connections-game.git
cd connections-game

# Install required dependencies
pip install -r requirements.txt

# Run the game
python main.py
```

## Usage

```python
# Basic usage
python main.py

# Run with custom word sets
python main.py --wordset custom_words.json
```

## Game Rules

### Categories
The game consists of 4 color-coded difficulty levels:
* **Easy (Green):** Broad, simple concepts (e.g., Types of Fish).
* **Medium (Blue):** Tangible objects or nature (e.g., Kitchen Items).
* **Hard (Yellow):** Abstract concepts or games (e.g., Card Games).
* **Expert (Red):** Niche groups or specific genres (e.g., Music Genres).

### Word Constraints
* **Length:** Minimum 3 letters.
* **Syllables:** Maximum 3 syllables.
* **Uniqueness:** No repeated words across categories.
* **Relevance:** Words must be commonly recognizable (no obscure technical jargon).
* **Morphology:** No groupings based solely on spelling, roots, or suffixes (e.g., "words ending in Y").

## Features

* **Dynamic Grid:** Words and categories are shuffled every game session.
* **Interactive UI:** Click-to-select interface with hover and selection states.
* **Smart Feedback:**
    * **Success:** Reveals the category name and highlights the row in the category color.
    * **One Off:** Alerts if 3 of 4 words are correct.
    * **Two Off:** Alerts if 2 of 4 words are correct.
* **Controls:**
    * **Shuffle:** Randomizes word positions without resetting progress.
    * **Reset:** Generates a fresh game board.
    * **Submit:** Validates selection (accessible via button or `Enter` key).

### Core Rules

1. **Grid Layout**: 16 words displayed in a 4×4 grid
2. **Categories**: 4 hidden categories, each containing 4 related words
3. **Selection**: Click boxes to select words (maximum 4 selections)
4. **Submission**: Press Submit button or Return/Enter key to check answer
5. **Victory**: Successfully identify all 4 categories to win

### Category Difficulty Levels

| Difficulty | Color | Description |
|------------|-------|-------------|
| Easy | Light Soft Green | Straightforward connections |
| Medium | Light Soft Blue | Moderate difficulty |
| Hard | Light Soft Yellow | Challenging associations |
| Expert | Light Soft Red | Subtle or tricky connections |

### Validation Feedback

- **All Correct**: Category revealed with colored boxes and category name
- **One Off**: "One away!" message (3 out of 4 correct)
- **Two Off**: "Two away!" message (2 out of 4 correct)
- **Otherwise**: "Try again!" message

## Category System

### Category Requirements

Categories must adhere to the following rules:

- ✅ **Thematic Relation**: Categories should be thematically connected
- ✅ **Semantic Groups**: Based on meaning, context, or conceptual relationships
- ❌ **No Spelling/Grammar**: Avoid categories like "verbs", "nouns", "adjectives"
- ❌ **No Word Manipulation**: No root words, prefixes, suffixes (e.g., cat/cats/catty)
- ❌ **No Letter Patterns**: No categories based on letter additions or transformations

### Example Category Sets

```
Easy: Animals → Cat, Dog, Bear, Lion
Medium: Colors → Red, Blue, Pink, Teal
Hard: Fruits → Lime, Plum, Fig, Date
Expert: Gems → Ruby, Jade, Opal, Pearl
```

## Word Requirements

All words in the game must meet these criteria:

| Requirement | Specification |
|-------------|---------------|
| **Minimum Length** | At least 3 letters |
| **Maximum Syllables** | No more than 3 syllables |
| **Uniqueness** | Each word appears only once across all categories |
| **Commonality** | Easily recognizable, non-technical terms |
| **Category Alignment** | Clear relationship to assigned category |
| **Relatedness** | Logical connection to other words in same category |

### Valid Word Examples

✅ Cat, Dog, Red, Blue, Oak, Elm, Jazz, Rock

### Invalid Word Examples

❌ Electroencephalography (too long, too technical)  
❌ Qi (too short, only 2 letters)  
❌ Antidisestablishmentarianism (too many syllables, too obscure)

## Controls

### Mouse Controls

- **Left Click**: Select/deselect a word box
- **Submit Button**: Validate selected words

### Keyboard Controls

- **Enter/Return**: Submit current selection
- **Escape**: Deselect all words (optional)

### Button Functions

| Button | Function |
|--------|----------|
| **Submit** | Check if 4 selected words form a valid category |
| **Shuffle** | Randomize word positions (preserves game state) |
| **Reset** | Clear progress and generate new puzzle |

## Development

### Project Structure

```
connections-game/
├── main.py                 # Entry point
├── game/
│   ├── __init__.py
│   ├── board.py           # Game board logic
│   ├── categories.py      # Category management
│   └── validation.py      # Answer validation
├── ui/
│   ├── __init__.py
│   ├── grid.py            # Grid rendering
│   └── controls.py        # Button and input handling
├── data/
│   └── wordsets.json      # Word and category data
├── tests/
│   ├── test_board.py
│   ├── test_categories.py
│   └── test_validation.py
├── requirements.txt
└── README.md
```

### Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest --cov=game tests/
```

### Code Style

This project follows [PEP 8](https://pep8.org/) style guidelines:

```bash
# Check code style
flake8 game/ ui/

# Format code
black game/ ui/
```

## Contributing

We welcome contributions! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Requirements

- Add tests for new features
- Update documentation as needed
- Follow existing code style
- Ensure all tests pass

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the NYT Connections game
- Built with Python and [your UI framework]
- Community contributors and testers

## Contact

- **Issues**: [GitHub Issues](https://github.com/yourusername/connections-game/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/connections-game/discussions)

---

**Note**: This is an educational project and is not affiliated with or endorsed by The New York Times.
