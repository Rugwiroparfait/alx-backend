#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple

index_range = __import__("0-simple_helper_function").index_range


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page of the dataset."""
        # Validate input parameters
        assert isinstance(page, int), "page must be an integer"
        assert page > 0, "page must be a positive integer"
        assert isinstance(page_size, int), "page_size must be an integer"
        assert page_size > 0, "page_size must be a positive integer"
        # Calculate start and end indices
        start_index, end_index = index_range(page, page_size)

        # Get the dataset
        dataset = self.dataset()

        # Return the appropriate slice of the dataset
        if start_index >= len(dataset):
            return []  # If start_index is out of range, return an empty list

        return dataset[start_index:end_index]
