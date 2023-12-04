#!/usr/bin/env python

import requests
import sys
import os
import urllib

# inspirehep docs: https://github.com/inspirehep/rest-api-doc
USAGE = "./makebibsfromarxivs <urlfile.txt>"


def getinput():
    if len(sys.argv) < 2:
        print("No arguments were given.", file=sys.stderr)
        print(USAGE, file=sys.stderr)
        exit(1)
    return sys.argv[1]


def load_ids_from_file(filename: str):
    if not os.path.isfile(filename):
        print(f"{filename} does not exists.", file=sys.stderr)
        exit(1)
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]


def main():
    arxivfile = getinput()
    arxivids = load_ids_from_file(arxivfile)
    for arxivid in arxivids:
        r = requests.get(
            f"https://inspirehep.net/api/arxiv/{arxivid.strip()}?format=bibtex"
        )
        if r.status_code >= 300:
            print("From HEP", r.text, file=sys.stderr)
            print("Could not file URL for", arxivid, file=sys.stderr)
            continue
        print(r.text)


if __name__ == "__main__":
    main()
