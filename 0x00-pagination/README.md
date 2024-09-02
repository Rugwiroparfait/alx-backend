# Pagination Project - README

## Project Overview

This project involves the implementation of various pagination techniques using Python. The goal is to efficiently paginate a dataset and ensure resilience against deletion of records. The dataset used for this project is the **Popular_Baby_Names.csv** file.

## Learning Objectives

By the end of this project, you should be able to:

- Implement simple pagination using page and page_size parameters.
- Integrate hypermedia metadata into pagination.
- Develop deletion-resilient pagination methods.

## Requirements

- **Python Version**: 3.7
- **OS**: Ubuntu 18.04 LTS
- **Coding Style**: All Python files must adhere to `pycodestyle` (version 2.5.*).
- **Documentation**: All modules and functions must include appropriate docstrings.
- **Type Annotations**: All functions and coroutines must be type-annotated.

## Setup

The project uses the **Popular_Baby_Names.csv** file as the dataset. Ensure this file is available in your working directory before executing any tasks.

## Tasks

### Task 0: Simple Helper Function

**File**: `0-simple_helper_function.py`

**Objective**: Implement a function `index_range` that calculates the start and end index for pagination.

- **Parameters**: 
  - `page` (int): The current page number.
  - `page_size` (int): The number of items per page.
- **Returns**: 
  - A tuple `(start, end)` indicating the range of indexes for the current page.

### Task 1: Simple Pagination

**File**: `1-simple_pagination.py`

**Objective**: Implement a method `get_page` in the `Server` class to paginate the dataset using `index_range`.

- **Parameters**:
  - `page` (int): The current page number (default is 1).
  - `page_size` (int): The number of items per page (default is 10).
- **Validations**:
  - Both `page` and `page_size` must be integers greater than 0.
  - If the arguments are out of range, return an empty list.

### Task 2: Hypermedia Pagination

**File**: `2-hypermedia_pagination.py`

**Objective**: Implement a method `get_hyper` in the `Server` class to provide pagination with hypermedia metadata.

- **Returns**: A dictionary with the following keys:
  - `page_size`: Length of the current page.
  - `page`: Current page number.
  - `data`: The paginated dataset.
  - `next_page`: Next page number (or `None` if there is no next page).
  - `prev_page`: Previous page number (or `None` if there is no previous page).
  - `total_pages`: Total number of pages in the dataset.

### Task 3: Deletion-Resilient Hypermedia Pagination

**File**: `3-hypermedia_del_pagination.py`

**Objective**: Implement a deletion-resilient pagination method `get_hyper_index` in the `Server` class.

- **Parameters**:
  - `index` (int): The start index for pagination (default is `None`).
  - `page_size` (int): The number of items per page (default is 10).
- **Returns**: A dictionary with the following keys:
  - `index`: The current start index of the returned page.
  - `next_index`: The next index to query.
  - `page_size`: The current page size.
  - `data`: The paginated dataset.
- **Behavior**:
  - If rows are deleted between queries, the user will not miss items when navigating pages.

## Repository Structure

- **GitHub Repository**: `alx-backend`
- **Directory**: `0x00-pagination`

## How to Run the Project

1. Ensure that the **Popular_Baby_Names.csv** file is available in your project directory.
2. Execute each Python script to test the functionality.
3. Use the provided main files (e.g., `0-main.py`, `1-main.py`, etc.) to validate your implementation.

## License

This project is licensed under the terms of the ALX program.
