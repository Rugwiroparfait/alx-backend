# 0x01. Caching

## Project Overview

This project focuses on implementing various caching algorithms using Python. Each task requires the creation of a caching system that inherits from a base class, `BaseCaching`, and implements specific caching strategies like FIFO, LIFO, LRU, and MRU.

## Requirements

- All Python scripts must be compatible with Python 3.7 and run on Ubuntu 18.04 LTS.
- Scripts must adhere to the `pycodestyle` (version 2.5) guidelines.
- Every file should be executable and include a shebang (`#!/usr/bin/env python3`).
- Each module, class, and function should have comprehensive documentation.

## Tasks

### Task 0: Basic Dictionary
- **File**: `0-basic_cache.py`
- **Class**: `BasicCache`
- **Description**: Implement a caching system without a limit. The `put` method stores items in a dictionary, while the `get` method retrieves them.

### Task 1: FIFO Caching
- **File**: `1-fifo_cache.py`
- **Class**: `FIFOCache`
- **Description**: Implement a caching system that follows the FIFO (First-In, First-Out) policy. When the cache exceeds its limit, the oldest item is discarded.

### Task 2: LIFO Caching
- **File**: `2-lifo_cache.py`
- **Class**: `LIFOCache`
- **Description**: Implement a caching system that follows the LIFO (Last-In, First-Out) policy. When the cache exceeds its limit, the most recently added item is discarded.

### Task 3: LRU Caching
- **File**: `3-lru_cache.py`
- **Class**: `LRUCache`
- **Description**: Implement a caching system that follows the LRU (Least Recently Used) policy. When the cache exceeds its limit, the least recently accessed item is discarded.

### Task 4: MRU Caching
- **File**: `4-mru_cache.py`
- **Class**: `MRUCache`
- **Description**: Implement a caching system that follows the MRU (Most Recently Used) policy. When the cache exceeds its limit, the most recently accessed item is discarded.

## Repository Structure

- **GitHub Repository**: `alx-backend`
- **Directory**: `0x01-caching`
- **Files**: Each task corresponds to a specific Python file as outlined above.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/alx-backend.git
   cd alx-backend/0x01-caching
   ```

2. Run the provided test files to see the caching system in action:
   ```bash
   ./0-main.py
   ./1-main.py
   ./2-main.py
   ./3-main.py
   ./4-main.py
   ```

Each test file demonstrates the behavior of the implemented caching strategy.

## Documentation

- **Modules**: Include a detailed description at the beginning of each Python file.
- **Classes and Functions**: Document the purpose and behavior of each class and function. Use Python docstrings for this purpose.


