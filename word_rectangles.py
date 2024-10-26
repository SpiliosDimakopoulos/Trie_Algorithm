import sys
from collections import defaultdict

# Trie Node Definition
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end_of_word = False

# Trie Implementation
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    # Check if prefix exists in the Trie
    def starts_with(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True  #it exists

    # Print the trie, marking leaf node with '0'
    def print_trie(self, current_node=None, prefix=""):
        if current_node is None:
            current_node = self.root

        if current_node.is_end_of_word:
            print(f"{prefix}")

        if not current_node.children:
            print(f"{prefix} -> 0")
        else:
            for char, child_node in current_node.children.items():
                self.print_trie(child_node, prefix + char)

# Load words from file
def read_words_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            words = [line.strip().upper() for line in file.readlines()]
        return words
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

# Populate Trie from file
def populate_trie_from_file(trie, file_path):
    words = read_words_from_file(file_path)
    for word in words:
        trie.insert(word)

# Print the word rectangle
def print_rectangle(rectangle):
    for row in rectangle:
        print("".join(row))
    print()  # New line

# Check if a word can form a valid prefixes in the columns
def can_form_rectangle(trie_vertical, rectangle, word, n_cols):
    new_rectangle = [row[:] for row in rectangle] + [[ch for ch in word]]
    for col_idx in range(n_cols):
        col_prefix = ''.join(row[col_idx] for row in new_rectangle)
        if not trie_vertical.starts_with(col_prefix):
            return False
    return True

# Recursive search to find word rectangles
def search(rectangle, trie_horizontal, trie_vertical, words_horizontal, n_cols, n_rows):
    if len(rectangle) == n_rows:
        print("Found rectangle:")
        print_rectangle(rectangle)
        return False  #continue searching

    for word in words_horizontal:
        if len(rectangle) > 0 and word == "".join(rectangle[-1]):
            continue
        if can_form_rectangle(trie_vertical, rectangle, word, n_cols):
            new_rectangle = rectangle + [[ch for ch in word]]
            if search(new_rectangle, trie_horizontal, trie_vertical, words_horizontal, n_cols, n_rows):
                return True
    return False

# Find word rectangles, given horizontal & vertical words
def find_rectangles(words_horizontal, words_vertical, n_cols):
    n_rows = n_cols  # forming square rows = cols
    trie_horizontal = Trie()
    trie_vertical = Trie()

    for word in words_horizontal:
        trie_horizontal.insert(word)

    for word in words_vertical:
        trie_vertical.insert(word)

    print("Searching for word rectangles...")
    search([], trie_horizontal, trie_vertical, words_horizontal, n_cols, n_rows)

# Command argument handling
def handle_commands():
    if len(sys.argv) < 3:
        print("Usage:")
        print("python word_rectangles.py print_trie <file1>")
        print("python word_rectangles.py find_rectangles <file1> <file2> <n_cols>")
        return

    command = sys.argv[1]
    try:
        if command == "print_trie" and len(sys.argv) == 3:
            file1 = sys.argv[2]
            trie = Trie()
            populate_trie_from_file(trie, file1)
            trie.print_trie()
        elif command == "find_rectangles" and len(sys.argv) == 5:
            file1 = sys.argv[2]
            file2 = sys.argv[3]
            n_cols = int(sys.argv[4])
            words_horizontal = read_words_from_file(file1)
            words_vertical = read_words_from_file(file2)
            if not words_horizontal or not words_vertical:
                print("Error: Could not load word files.")
                return
            find_rectangles(words_horizontal, words_vertical, n_cols)
        else:
            print("Invalid command or number of arguments.")
    except ValueError:
        print("Please ensure the number of columns is an integer.")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == '__main__':
    handle_commands()
