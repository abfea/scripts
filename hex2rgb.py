#!/bin/python
# -*- coding: utf-8 -*-
import sys

def hex2rgb(hex_color:str):
    rgb = [hex_color.lstrip('#')[i:i+2] for i in range(0, 6, 2)]
    for i in rgb:
        print(int(i, base=16))

def main():
    a = ['#123456', '#654321', '#987654', '#456789']
    for i in a:
        hex2rgb(i)
        print()

if __name__ == "__main__":
    main()
