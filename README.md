# Kx Connection Script

This script connects to a Kx (KDB+) database, runs a sample query, and logs the results.

## Prerequisites

- Python 3.x
- `qpython` library
- Kx (KDB+) database

## Installation

1. **Clone the repository or download the script.**

2. **Install the required Python packages:**
    ```bash
    pip install qpython
    ```

## Usage

1. **Set up your Kx connection details:**

    Update the following variables in the script with your Kx database details:
    ```python
    kx_host = 'your_kx_host'
    kx_port = 5001  # Replace with your KDB+ port
    kx_username = 'your_username'  # If authentication is required
    kx_password = 'your_password'  # If authentication is required
    ```

2. **Run the script:**
    ```bash
    python connectKX.py
    ```
