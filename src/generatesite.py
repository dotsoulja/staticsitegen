import os
import shutil


def extract_title(markdown):
    """"
    Extracts the h1 title from a markdown file (string), stripping the # and any leading/trailing whitespace."
    if no h1 title is found, raise an exception."
    """
    lines = markdown.split("\n")
    if not lines[0].startswith("# "):
        raise ValueError("No h1 title found")
    title = lines[0][2:].strip()
    print(f"{title}")
    return title
    