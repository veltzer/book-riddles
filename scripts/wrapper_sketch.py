#!/usr/bin/env python

"""
This is a script that wraps the execution of "sketch".

Why?
- too noisy on the command line when everything is right.
- does not cleanly separate warning and errors (stdout vs stderr).
"""

import os
import subprocess
import sys
import tempfile

# Parameters
DEBUG = False
REMOVE_TMP = True

def printout(filename):
    """Print to stderr the content of a file."""
    if DEBUG:
        print(f"printing [{filename}]")
    with open(filename, encoding="utf8") as file:
        for line in file:
            print(line, end="", file=sys.stderr)

def unlink_check(file, check):
    """Remove a file and optionally die if there is a problem."""
    if DEBUG:
        print(f"unlinking [{file}]")
    try:
        os.unlink(file)
    except OSError as e:
        if check:
            raise RuntimeError(f"problem unlinking file [{file}]: {e}") from e

def chmod_check(file, check):
    """Change file permissions and optionally die if there is a problem."""
    if DEBUG:
        print(f"chmodding [{file}]")
    try:
        os.chmod(file, 0o444)
    except OSError as e:
        if check:
            raise RuntimeError(f"problem chmodding file [{file}]: {e}") from e

def main():
    """ main entry point """
    # rsconstruct doctor probes every configured command with --version
    if sys.argv[1:] == ["--version"]:
        print("wrapper_sketch.py 1")
        return
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if DEBUG:
        print(f"input is [{input_file}]")
        print(f"output is [{output_file}]")

    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_fname = tmp_file.name

    cmd = ["sketch", input_file, "-o", output_file]

    if DEBUG:
        print(f"cmd is {cmd}")

    # First remove the output (if it exists)
    if os.path.exists(output_file):
        unlink_check(output_file, True)

    # Run the sketch command
    try:
        subprocess.run(cmd, check=True, stderr=subprocess.PIPE, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        # Error path
        with open(tmp_fname, "wb") as f:
            f.write(e.stderr)
        printout(tmp_fname)
        if REMOVE_TMP:
            unlink_check(tmp_fname, True)
        if os.path.exists(output_file):
            unlink_check(output_file, True)
        sys.exit(e.returncode)
    else:
        # Everything is ok
        if REMOVE_TMP:
            unlink_check(tmp_fname, True)
        # Change the output to be unchangeable (but only in the second time!)
        chmod_check(output_file, True)

if __name__ == "__main__":
    main()
