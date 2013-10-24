import os
from os.path import isdir
from sys import argv
from random import choice, randrange as rand

p_empty = 10
p_good = 30
letters = [chr(c) for c in range(ord('a'), ord('z') + 1)]
chars = letters + [str(c) for c in range(10)] + [' ']
dir = argv[1] if len(argv) > 1 else '.'
if not isdir(dir):
    os.mkdir(dir)
os.chdir(dir)
for i in range(100):
    filename = ''.join([choice(letters) for t in range(10)])
    f = open(filename, 'x')
    if rand(100) >= p_empty:
        n_str = rand(500, 3000)
        for s in range(n_str):
            if rand(100) < p_good:
                next_str = str(rand(1 << 31))
            else:
                next_str = ''.join([choice(chars) for t in range(100)])
            next_str = ' ' * rand(30) + next_str + ' ' * rand(30) + '\n'
            f.write(next_str)
