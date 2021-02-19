#!/bin/python

def ascii_color():
    '''
    tty环境会乱码
    '''
    for i in range(0, 11):
        for j in range(0, 10):
            n = 10*i + j
            if (n >= 108): break
            print("\033[{}m{}\033[m ".format(n, n),  end='')
        print()

def setBG(r:int, g:int, b:int):
    print('\033[48:2:{}:{}:{}m'.format(r, g, b), end=' ')

def reset():
    print('\033[0m', end='')

def rainbowColor(c:int):
    h = c//43
    f = c - 43*h
    t = f * 255//43
    q = 255 - t

    if (h == 0):
        return 255, t, 0
    elif (h == 1):
        return q, 255, 0
    elif (h == 2):
        return 0, 255, t
    elif (h == 3):
        return 0, q, 255
    elif (h == 4):
        return t, 0, 255
    elif (h == 5):
        return 255, 0, q
    else:
        return 0, 0, 0

for i in range(0, 127):
    setBG(i, 0, 0)
reset()
print()

for i in  range(0, 127):
    setBG(0, i, 0)
reset()
print()

for i in  range(0, 127):
    setBG(0, 0, i)
reset()
print()

for i in  range(255, 128):
    setBG(i, 0, 0)
reset()

for i in  range(255, 128):
    setBG(0, i, 0)
reset()

for i in  range(255, 128):
    setBG(0, 0, i)
reset()

for i in range(0, 127):
    setBG(*rainbowColor(i))
reset()
print()

for i in range(255, 128):
    setBG(*rainbowColor(i))
reset()
