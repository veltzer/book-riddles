#!/usr/bin/env python

"""
Check that every riddle is categorized: each riddle is a \\section whose title
ends with its category in parentheses, as in

    \\section{Monty Hall Problem (Probability)}

rsconstruct runs it as a checker with the .tex files as arguments.
"""

import re
import sys

SECTION = re.compile(r"\\section\s*\{(?P<title>.*)\}\s*$")
CATEGORIZED = re.compile(r".+ \([A-Z][^()]*\)$")


def main():
    """ main entry point """
    # rsconstruct doctor probes every configured command with --version
    if sys.argv[1:] == ["--version"]:
        print("check_categories.py 1")
        return
    errors = False
    for path in sys.argv[1:]:
        with open(path, encoding="utf-8") as stream:
            for number, line in enumerate(stream, start=1):
                match = SECTION.match(line)
                if match and not CATEGORIZED.match(match["title"]):
                    print(f"{path}:{number}: riddle without a category in parentheses: {match['title']}")
                    errors = True
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
