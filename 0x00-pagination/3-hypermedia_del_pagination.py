#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self, index: int = None, page_size: int = 10
    ) -> Dict[str, Any]:
        """Return a dictionary containing hypermedia pagination
        data, resilient to deletions."""
        indexed_data = self.indexed_dataset()

        # Assert that the index is within the valid range
        assert isinstance(index, int), "index must be an integer"
        assert index >= 0, "index must be non-negative"
        assert index < len(indexed_data), "index out of range"

        data = []
        next_index = index
        current_count = 0

        # Collect the correct page of data, skipping missing indices
        while current_count < page_size and next_index < len(indexed_data):
            item = indexed_data.get(next_index)
            if item:
                data.append(item)
                current_count += 1
            next_index += 1

        # Return the next index to query, or None if we've reached the end
        next_index = next_index if next_index < len(indexed_data) else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
        }
