# jsLookup

**jsLookup** is a simple Python tool for searching patterns in JavaScript (or any text) files.  
It reads patterns from a `pattern.txt` file and scans a target file for matching lines.

## Features

- Search for multiple patterns in a file
- Print matching lines to the console
- Save results to an output file (`-o`)
- Verbose mode (`-v`) shows matched pattern with each line

## Usage

```bash
python jsLookup.py --file target.js
```

**Optional arguments:**

- `-o output.txt` &nbsp;&nbsp;&nbsp;&nbsp; Save results to `output.txt`
- `-v` &nbsp;&nbsp;&nbsp;&nbsp; Verbose output. (shows pattern with each line)

**Example:**

```bash
python jsLookup.py --file target.js -o results.txt -v
```

## Requirements

- Python 3.x
