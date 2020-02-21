import sys
import struct
import os, platform
from ctypes import windll, create_string_buffer

with open(sys.argv[1], 'r') as text_file:
    lines = [line.strip().split('\n') for line in text_file]


pagesize = 20
pages = {}
pageIndex = 0

buffer = []
buffer.append(lines[0][0]) 
for i in range(1, len(lines)):
    buffer.append(lines[i][0]) 

    if  i % pagesize == 0:
        # print(buffer)
        pages[pageIndex] = buffer
        pageIndex = pageIndex + 1
        buffer = []

currentIndex = 0

while True:
    inpt = input()
    if inpt == 'q':
        exit(0)
    elif inpt == 'b':
        if currentIndex != 0:
            currentIndex -= 1
    elif inpt == 'f':
        if currentIndex < len(pages):
            currentIndex += 1

    for i in range(len(pages[currentIndex])):
        print(pages[currentIndex][i])