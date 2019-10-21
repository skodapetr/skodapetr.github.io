#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import typing


# region Functions

def modulo_hash(value: int, size: int) -> int:
    return value % size


def modulo_shift_hash(value: int, shift: int, size: int) -> int:
    return (value >> shift) % size


# endregion

class CormackDictionaryLine:

    def __init__(self, p, i, r):
        self.p = p
        self.i = i
        self.r = r


class Cormack:

    def __init__(
            self,
            directory_size=7,
            iterations_before_next_r=10,
            directory_hash_function=modulo_hash,
            primary_hash_function=modulo_shift_hash):
        self._iterations_before_next_r = iterations_before_next_r
        self._directory = []
        self._directory_hash_func = directory_hash_function
        self._primary_hash_fun = primary_hash_function
        self._directory = [None] * directory_size
        # Primary file lives in a secondary memory, we have it here
        # just for an illustration.
        self._primary_file = []

    def set_directory_line(self, record, pos):
        self._directory[pos] = record

    def get_directory_line(self, pos):
        return self._directory[pos]

    def __str__(self):
        output = ""
        output += "DIRECTORY\n"
        for index, line in enumerate(self._directory):
            if line is None:
                output += " {:>3}\n".format(index)
                continue
            output += " {:>3} {:>8} {:>8} {:>8}\n" \
                .format(index, line.p, line.i, line.r)
        output += "PRIMARY FILE\n"
        for index, value in enumerate(self._primary_file):
            output += " {:>3} {:>8}\n".format(index, str(value))
        return output

    def find(self, value):
        directory_pos = self._directory_hash_func(value, len(self._directory))
        directory_line = self._directory[directory_pos]
        position = \
            directory_line.p + \
            self._primary_hash_fun(value, directory_line.i, directory_line.r)
        return position

    def insert(self, value):
        directory_pos = self._directory_hash_func(value, len(self._directory))
        directory_line = self._directory[directory_pos]
        values = self._read_all_values_for_line(directory_line) + [value]
        i, r = self._find_hash_function(values)
        p = len(self._primary_file)
        self._expand_primary_file(r)
        self._insert_values(values, p, i, r)
        self._directory[directory_pos] = CormackDictionaryLine(p, i, r)

    def _read_all_values_for_line(self, line: CormackDictionaryLine):
        if line is None:
            return []
        return [
            self._primary_file[index]
            for index in range(line.p, line.p + line.r)
            if self._primary_file[index] is not None
        ]

    def _find_hash_function(self, values) -> typing.Tuple[int, int]:
        logging.info("Searching function for: %s", values)
        i = 0
        r = len(values)
        while not self._is_perfect(values, i, r):
            i += 1
            if i > self._iterations_before_next_r:
                i = 0
                r += 1
                logging.debug("Increasing r")
        return i, r

    def _is_perfect(self, values, i, r) -> bool:
        positions = set()
        for value in values:
            new_position = self._primary_hash_fun(value, i, r)
            if new_position in positions:
                return False
            positions.add(new_position)
        return True

    def _expand_primary_file(self, size):
        self._primary_file.extend([None] * size)

    def _insert_values(self, values, p, i, r):
        for value in values:
            position = p + self._primary_hash_fun(value, i, r)
            self._primary_file[position] = value


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] - %(message)s",
    datefmt="%H:%M:%S")


def help():
    print("""HELP:
c = cormack.Cormack()
c.insert(21)
print(c.find(21))
print(c)
    """)
