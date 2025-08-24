import argparse
import re

def pattern(pattern_file):
    patterns = []
    with open(pattern_file, 'r') as file:
        for lines in file:
            patterns.append(lines.strip())
    return patterns

def lookup(file_name, patterns):
    with open(file_name, 'r') as file:
        content = file.read()
        lines = file.readlines()
        for pat in patterns:
            for line in lines:
                if re.search(pat, line):
                    print(f"js Pattern: {pat}\tLine: {line.strip()}\n")


def main():

    pattern_file = 'pattern.txt'

    parser = argparse.ArgumentParser(description="jsParser")
    parser.add_argument('--file','-f',type=str,help='file name',required=True,)

    args = parser.parse_args()

    file_name = args.file

    patterns = pattern(pattern_file)
    lookup(file_name, patterns)


if __name__ == "__main__":
    main()