import argparse
import re
import os

#def pattern(pattern_file):
patterns = ["/static/js/chunk.js","/main.chunk.js","/_next/static/cunks/","/config.js","/env.js","/sw.js","/service-worker.js","main.js.map","/_/firebase/init.js","/intercom.js","/livechat.js","/analytics.js",".mjs""/cdn-cgi/","/cloudflare-assets/","/assets/js/","/vendor.js","/app.js","/bundle.js"]
  #  try:
   #     with open(pattern_file, 'r') as file:
   #         for lines in file:
   #             patterns.append(lines.strip())
   #     return patterns
   # except FileNotFoundError:
   #     print("[!] Pattern file are missing")

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

    #pattern_file = 'pattern.txt'

    parser = argparse.ArgumentParser(description="jsParser")
    parser.add_argument('--file','-f',type=str,help='file name',required=True,)

    args = parser.parse_args()

    file_name = args.file

    
    lookup(file_name, patterns)


if __name__ == "__main__":
    main()