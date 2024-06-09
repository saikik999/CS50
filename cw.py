import nltk
import random
import string

nltk.download('words')
from nltk.corpus import words

def create_empty_grid(size):
    return [[' ' for _ in range(size)] for _ in range(size)]

def print_grid(grid):
    for row in grid:
        print(' '.join(row))
    print()

def get_random_word_list(max_length):
    word_list = [word.lower() for word in words.words() if len(word) <= max_length]
    random.shuffle(word_list)
    return word_list

def fit_word_in_grid(grid, word, row, col, direction):
    if direction == 'horizontal':
        for i in range(len(word)):
            grid[row][col + i] = word[i]
    elif direction == 'vertical':
        for i in range(len(word)):
            grid[row + i][col] = word[i]

def can_fit_word(grid, word, row, col, direction):
    if direction == 'horizontal':
        if col + len(word) > len(grid[0]):
            return False
        for i in range(len(word)):
            if grid[row][col + i] != ' ' and grid[row][col + i] != word[i]:
                return False
    elif direction == 'vertical':
        if row + len(word) > len(grid):
            return False
        for i in range(len(word)):
            if grid[row + i][col] != ' ' and grid[row + i][col] != word[i]:
                return False
    return True

def generate_crossword(size, max_word_length):
    grid = create_empty_grid(size)
    word_list = get_random_word_list(max_word_length)
    
    for word in word_list:
        placed = False
        attempts = 0
        while not placed and attempts < 100:
            direction = random.choice(['horizontal', 'vertical'])
            row = random.randint(0, size - 1)
            col = random.randint(0, size - 1)
            if can_fit_word(grid, word, row, col, direction):
                fit_word_in_grid(grid, word, row, col, direction)
                placed = True
            attempts += 1
    
    return grid

crossword_size = 10
max_word_length = 7

crossword = generate_crossword(crossword_size, max_word_length)
print_grid(crossword)