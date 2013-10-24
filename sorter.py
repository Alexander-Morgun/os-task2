import os
from os.path import isdir
from sys import argv


def make_bad(f, p=10, message=''):
    from random import randrange as rand
    if message == '':
        message = 'Error at ' + f.__name__
    def wrapper(*args, **kwargs):
        if rand(100) < p:
            raise Exception(message)
        else:
            return f(*args, **kwargs)
    return wrapper

@make_bad
def append(array, element):
    array.append(element)

@make_bad
def read_line(file):
    return file.__next__()


open = make_bad(open)
os.chdir = make_bad(os.chdir)
os.listdir = make_bad(os.listdir)
isdir = make_bad(isdir)

arr = []
dir = argv[1] if len(argv) > 1 else '.'
try:
    if not isdir(dir):
        dir = '.'
    os.chdir(dir)
    for file_name in os.listdir('.'):
        try:
            with open(file_name, 'r') as f:
                while True:
                    try:
                        line = read_line(f)
                        append(arr, int(line))
                    except StopIteration:
                        break
                    except ValueError:
                        print('Bad string in input file')
                    except Exception as e:
                        print(e)
        except Exception as e:
            print(e)
except Exception as e:
        print(e)
print(sorted(arr))
print(len(arr))