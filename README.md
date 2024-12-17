# Word Rectangles Finder

This Python project contains functionality to find word rectangles from horizontal and vertical word lists. It uses a Trie data structure to efficiently check for word prefixes both horizontally and vertically to form a valid word rectangle.

## Features

- **Trie Data Structure**: Implements a Trie to store words and check prefixes efficiently.
- **Word Rectangle Search**: Searches for valid word rectangles where words align both horizontally and vertically.
- **Command Line Interface**: Supports two main commands:
  - `print_trie <file>`: Loads a file with words and prints the Trie structure.
  - `find_rectangles <file1> <file2> <n_cols>`: Finds word rectangles given two word lists (one horizontal, one vertical) and a specified number of columns for the rectangle.

## Requirements

- Python 3.x

### Usage

#### Print Trie
To print the Trie structure of words from a file, use:

```bash
python word_rectangles.py print_trie <file_path>
Find Word Rectangles
To find word rectangles, use:

bash
Copy code
python word_rectangles.py find_rectangles <file1> <file2> <n_cols>
file1: Path to the file containing horizontal words.
file2: Path to the file containing vertical words.
n_cols: The number of columns for the word rectangle (an integer).
How It Works
Trie Node: Each TrieNode contains a dictionary of children and a boolean flag is_end_of_word to mark the end of a word.
Trie Class: Manages the insertion of words and prefix checking.
Word Rectangle Search: Searches for all possible word rectangles based on the given words and the Trie structure.
Example
For horizontal and vertical word lists:

vbnet
Copy code
horizontal: ["WORD", "RECT", "SQUARE"]
vertical: ["WORD", "RECT", "SQUARE"]
n_cols: 4
The script will search for all valid 4x4 word rectangles.

Error Handling
If files are not found, an error will be printed.
If there are issues with word formats or column sizes, the script will notify the user.
