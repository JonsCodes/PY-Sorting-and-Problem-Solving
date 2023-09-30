# Write your solution for algorithm 4 below
def sort_words_in_string(s):
    words = s.split()
    sorted_words = sorted(words, key=lambda word: word.lower())
    return sorted_words

sample_input = 'I love software engineering'
print(sort_words_in_string(sample_input))  # Expected output: ['engineering', 'I', 'love', 'software']
