import argparse
import re

def pattern(pattern_file):
    patterns = []
    try:
        with open(pattern_file, 'r') as file:
            for lines in file:
                patterns.append(lines.strip())
        return patterns
    except FileNotFoundError:
        print("[!] Pattern file are missing")

def lookup(file_name, patterns,output_file=None, verbose=None):
    results = []
    try:
        with open(file_name, 'r') as file:      
            lines = file.readlines()
            for pat in patterns:
                for line in lines:
                    if re.search(pat, line):
                        if verbose:
                            result = f"[#] pattern: {pat} :\t{line.strip()}\n"
                            results.append(result)
                        else:
                            result = f"{line.strip()}\n"
                            results.append(result)

        if output_file:
            with open(output_file, 'w') as out:
                out.writelines(results)
        else:
            for result in results:
                print(result, end='')
    except FileNotFoundError as e:
        print(f"[!] {e}")


def main():

    pattern_file = 'pattern.txt'

    parser = argparse.ArgumentParser(description="jsParser")
    parser.add_argument('--file','-f',type=str,help='file name',required=True)
    parser.add_argument('-o',type=str,help='save output into file')
    parser.add_argument('-v',help='verbose output',action='store_true')

    args = parser.parse_args()

    file_name = args.file
    output_file = args.o
    verbose = args.v

    patterns = pattern(pattern_file)
    lookup(file_name, patterns,output_file,verbose)


if __name__ == "__main__":
    main()