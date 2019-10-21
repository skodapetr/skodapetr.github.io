#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import typing
import time


# region Functions

def modulo_plus_hash(value: int, plus: int, size: int) -> int:
    return (value + plus) % size


def modulo_shift_hash(value: int, shift: int, size: int) -> int:
    return (value >> shift) % size


# endregion


class LarsonKalja:

    def __init__(
            self,
            page_count=5,
            page_size=3,
            sep_max=7,
            hash_fnc=modulo_plus_hash,
            sep_fnc=modulo_shift_hash):
        self._hash_fnc = hash_fnc
        self._sep_fnc = sep_fnc
        self._separators = [sep_max] * page_count
        self._page_size = page_size
        self._pages = [
            []
            for _ in range(page_count)
        ]
        self._sep_max = sep_max

    def __str__(self):
        output = ""
        for index, (separator, page) in \
                enumerate(zip(self._separators, self._pages)):
            output += "Page: {:>3} separator: {:>3}\n".format(
                index, str(self._separators[index]))
            for value in page:
                if value is None:
                    output += "\n"
                    continue
                output += "    {:>6}\n".format(value)
        return output

    def find(self, value):
        try_counter = 0
        while True:
            page_index = self._hash_fnc(value, try_counter, len(self._pages))
            sep = self._sep_fnc(value, try_counter, self._sep_max)
            if sep < self._separators[page_index]:
                return page_index
            try_counter += 1

    def insert(self, new_value):
        values_to_insert = [new_value]
        while len(values_to_insert) > 0:
            try_counter = 0
            value = values_to_insert.pop()
            logging.info("Inserting: %s", value)
            while True:
                page = self._hash_fnc(value, try_counter, len(self._pages))
                sep = self._sep_fnc(value, try_counter, self._sep_max)
                # Inserting may result into kicking some values off the page.
                inserted, reinsert = self._insert_into_page(value, sep, page)
                values_to_insert.extend(reinsert)
                if reinsert:
                    logging.debug(
                        " %s %s reinsert: %s",
                        inserted, try_counter, str(reinsert))
                    # We may still fit inside a page let's try it again.
                    continue
                if inserted:
                    # Value has been inserted.
                    break
                try_counter += 1
                if try_counter > 3:
                    exit()

    def _insert_into_page(self, value, value_sep, page_index):
        if value_sep >= self._separators[page_index]:
            return False, []
        page = self._pages[page_index]
        if len(page) < self._page_size:
            page.append(value)
            return True, []
        # There is no space, decrease separator and everybody out.
        self._separators[page_index] -= 1
        self._pages[page_index] = []
        logging.debug(
            "Decreasing sep for %s to %s",
            page_index, self._separators[page_index])
        return False, page


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] - %(message)s",
    datefmt="%H:%M:%S")


def help():
    print("""HELP:
lk = larson_kalja.LarsonKalja()
lk.insert(10)
lk.insert(20)
lk.insert(30)
lk.insert(32)
lk.insert(37)
lk.insert(42)
lk.insert(51)
lk.insert(61)
# Reinsert.
lk.insert(40)
# Chain reinsert.
lk.insert(41)
print(lk)
print(lk.find(41))
    """)
