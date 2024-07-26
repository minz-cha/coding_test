from collections import Counter
import sys
input = sys.stdin.read()

def word_study(N, M, words):
    word_count = Counter(words)
    filtered_words = [
        (word, count) for word, count in word_count.items()
        if (len(word) >= M)
    ]
    
    filtered_words.sort(key = lambda x: (-x[1], -len(x[0]), x[0]))
    
    for word, _ in filtered_words:
        print(word)
        
data = input.split()
N = int(data[0])
M = int(data[1])
words = data[2:]

word_study(N, M, words)