#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import copy
import pickle
import typing
import logging

SECONDARY_STORAGE_SPEED = 4

DATA_BLOCK_SIZE = 3

INDEX_BLOCK_SIZE = 5


# region Interface

class Block:
    def __init__(self):
        self.data = []

    def __str__(self):
        return "    Data\n      " + \
               "\n      ".join(str(item) for item in self.data)

    def is_empty(self):
        return len(self.data) == 0


class SecondaryMemory:

    def __init__(self):
        self.blocks = []

    def allocate_block(self):
        self.blocks.append(Block())
        return len(self.blocks) - 1

    def load_block(self, index):
        assert 0 <= index < len(self.blocks)
        time.sleep(SECONDARY_STORAGE_SPEED)
        return copy.deepcopy(self.blocks[index])

    def store_block(self, index, block):
        assert 0 <= index < len(self.blocks)
        time.sleep(SECONDARY_STORAGE_SPEED)
        self.blocks[index] = copy.deepcopy(block)
        return index

    def __str__(self):
        result = "Secondary memory dump\n"
        for index, block in enumerate(self.blocks):
            result += "  Block: %i \n %s \n" % (index, str(block))
        result += "\n"
        return result

    def _store_new_block(self, block):
        index = self.allocate_block()
        return self.store_block(index, block)

    def _save(self, file="./02_file_organizations.dump"):
        with open(file, "wb") as stream:
            pickle.dump(self.blocks, stream)

    def _load(self, file="./02_file_organizations.dump"):
        if not os.path.exists(file):
            return
        with open(file, "rb") as stream:
            self.blocks = pickle.load(stream)


# endregion

# region Create data

def create_data_file(
        storage: SecondaryMemory,
        number_of_records: int):
    block = Block()
    for index in range(number_of_records):
        data_record = {"id": index, "name": "Gen#" + str(index)}
        block.data.append(data_record)
        if len(block.data) == DATA_BLOCK_SIZE:
            storage.store_block(
                storage.allocate_block(),
                block)
            block = Block()
    if not block.is_empty():
        storage.store_block(
            storage.allocate_block(),
            block)

# endregion

# region Full scan search

def full_scan_search(
        memory: SecondaryMemory,
        start_block: int,
        number_of_block: int,
        matcher: typing.Callable):
    result = []
    for index in range(start_block, start_block + number_of_block):
        block = memory.load_block(index)
        for item in block.data:
            if matcher(item):
                result.append(item)
    return result

# endregion

# region Primary index build

def create_primary_index(
        memory: SecondaryMemory,
        start_block: int,
        number_of_block: int):
    index_level_blocks = create_zero_level_primary_index(
        memory, start_block, number_of_block)
    # Generate additional levels.
    height = 1
    while len(index_level_blocks) > 1:
        height += 1
        index_level_blocks = create_next_level_primary_index(
            memory, index_level_blocks)
    # Return the top of the index.
    return index_level_blocks[0], height


def create_zero_level_primary_index(
        memory: SecondaryMemory,
        start_block: int,
        number_of_block: int):
    index_level_blocks = []
    index_block = Block()
    for index in range(start_block, start_block + number_of_block):
        data_block = memory.load_block(index)
        index_block.data.append({
            "id": data_block.data[0]["id"],
            "block": index
        })
        if len(index_block.data) == INDEX_BLOCK_SIZE:
            index_level_blocks.append(memory._store_new_block(index_block))
            index_block = Block()
    if not index_block.is_empty():
        index_level_blocks.append(memory._store_new_block(index_block))
    return index_level_blocks


def create_next_level_primary_index(
        memory: SecondaryMemory,
        previous_index_blocks: typing.List[int]):
    index_level_blocks = []
    index_block = Block()
    for index in previous_index_blocks:
        previous_index_block = memory.load_block(index)
        index_block.data.append({
            "id": previous_index_block.data[0]["id"],
            "block": index
        })
        if len(index_block.data) == INDEX_BLOCK_SIZE:
            index_level_blocks.append(memory._store_new_block(index_block))
            index_block = Block()
    if not index_block.is_empty():
        index_level_blocks.append(memory._store_new_block(index_block))
    return index_level_blocks

# endregion

# region Primary index search

def search_using_primary_index(
        memory: SecondaryMemory,
        index_root: int,
        index_height: int,
        id: int):
    data_index = search_using_primary_index_find_leaf(
        memory, index_root, index_height, id)
    return search_using_primary_index_scan_data(memory, data_index, id)


def search_using_primary_index_find_leaf(
        memory: SecondaryMemory, index: int, height: int, id: int):
    next_index = index
    for _ in range(height):
        block = memory.load_block(next_index)
        for item in block.data:
            if item["id"] >= id:
                continue
            next_index = item["block"]
    return next_index


def search_using_primary_index_scan_data(
        memory: SecondaryMemory, index: int, id: int):
    block = memory.load_block(index)
    for item in block.data:
        if item["id"] == id:
            return item
    return None


# endregion

def main():
    secondary_memory = SecondaryMemory()
    secondary_memory._load()
    showcase(secondary_memory)
    logging.info("All done :)")
    secondary_memory._save()


def showcase(secondary_memory):
    # print(secondary_memory)
    # return

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # logging.info("Creating data block ...")
    # print("> Creating data block ...")
    # data_block = Block()
    # data_block.data.append({"id": 0, "name": "Petr"})
    # secondary_memory.store_block(
    #     secondary_memory.allocate_block(),
    #     data_block)
    # print(secondary_memory)
    # return

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # logging.info("Generating content ...")
    # create_data_file(secondary_memory, 17)
    # print(secondary_memory)
    # return

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # logging.info("Creating a metadata block ...")
    # metadata_block = Block()
    # metadata_block.data.append({
    #     "start": 0,
    #     "end": 6
    # })
    # secondary_memory.store_block(
    #     secondary_memory.allocate_block(),
    #     metadata_block
    # )
    # print(secondary_memory)
    # return

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    logging.info("Loading metadata ...")
    METADATA_BLOCK = 6
    metadata_block = secondary_memory.load_block(METADATA_BLOCK)
    metadata = metadata_block.data[0]
    print("Metadata:", metadata)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    logging.info("Full scan search ...")
    result = full_scan_search(
        secondary_memory, metadata["start"], metadata["end"],
        lambda item: item["id"] == 7
    )
    print("Search result:", result)
    logging.info("Full scan search ... done")
    # return

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # logging.info("Creating primary index ...")
    # index_root, index_root_height = create_primary_index(
    #     secondary_memory, metadata["start"], metadata["end"])
    # logging.info("Creating primary index ... done")
    # # Update metadata.
    # metadata["primary-index"] = index_root
    # metadata["primary-index-height"] = index_root_height
    # secondary_memory.store_block(METADATA_BLOCK, metadata_block)
    # print(secondary_memory)
    # return

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    logging.info("Primary index search ...")
    result = search_using_primary_index(
        secondary_memory,
        metadata["primary-index"],
        metadata["primary-index-height"],
        7)
    print("Search result:", result)
    logging.info("Primary index search ... done")
    return


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] - %(message)s",
        datefmt="%H:%M:%S")
    main()
