#!/usr/bin/python3

import argparse
import re
import os

patterns = ["/static/js/chunk.js","/main.chunk.js","/_next/static/cunks/","/config.js","/env.js","/sw.js","/service-worker.js","main.js.map","/_/firebase/init.js","/intercom.js","/livechat.js","/analytics.js",".mjs""/cdn-cgi/","/cloudflare-assets/","/assets/js/","/vendor.js","/app.js","/bundle.js"]

def lookup(file_name, patterns,output_file=None, verbose=None):
    results = []
    working_dir = os.getcwd()
    try:
        with open(f"{working_dir}/{file_name}", 'r') as file:      
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

    parser = argparse.ArgumentParser(description="jsLookup is a simple Python tool for searching patterns in JavaScript (or any text) files. It scans a target file for matching lines.")
    parser.add_argument('-f','--file',type=str,help='file name',required=True,metavar="")
    parser.add_argument('-o',type=str,help='save output into file',metavar="file name")
    parser.add_argument('-v',help='verbose output',action='store_true')

    args = parser.parse_args()

    file_name = args.file
    output_file = args.o
    verbose = args.v

    
    lookup(file_name, patterns,output_file,verbose)


if __name__ == "__main__":
    main()