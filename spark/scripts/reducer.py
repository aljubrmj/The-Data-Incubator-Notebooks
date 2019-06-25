#!/usr/bin/env python3

from itertools import groupby
from operator import itemgetter
import sys

def read_input(file, encoding='utf-8'):
    for line in file:
        yield line.decode(encoding)

def write_line(line, encoding='utf-8'):
    sys.stdout.buffer.write((line + '\n').encode(encoding))

def main(separator='\t'):
    data = map(lambda line: line.split(separator, 1), read_input(sys.stdin.buffer))
    for current_word, group in groupby(data, itemgetter(0)):
        total_count = sum(int(count) for _, count in group)
        write_line("%s%s%d" % (current_word, separator, total_count))

if __name__ == "__main__":
    main()
