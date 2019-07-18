# python3

import random

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def poly_hash(s, prime, x):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % prime
    return ans

def precompute_hashes(text, pattern_len, p, x):
    H = [0] * (len(text) - pattern_len + 1)
    s = text[-pattern_len:]
    H[len(text)-pattern_len] = poly_hash(s, p, x)
    y = 1
    for i in range(1, pattern_len+1):
        y = (y * x) % p
    for i in reversed(range(len(text) - pattern_len)):
        pre_hash = x * H[i + 1] + ord(text[i]) - y * ord(text[i + pattern_len])
        while(pre_hash < 0):
            pre_hash += p
        H[i] = pre_hash % p
    return H

def get_occurrences(pattern, text):
    p = 1000000007
    x = random.randint(1, p)
    text_len = len(text)
    pattern_len = len(pattern)
    phash = poly_hash(pattern, p, x)
    H = precompute_hashes(text, pattern_len, p, x)
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if phash == H[i] and text[i:i + len(pattern)] == pattern
    ]

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))