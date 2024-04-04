#!/usr/bin/env python3

from pathlib import Path
from bs4 import BeautifulSoup, NavigableString


def remove_newlines(soup):
    if isinstance(soup, NavigableString):
        soup.string.replace_with(soup.replace('\n', ' '))
    if soup.name == 'pre' or soup.name is None:
        return
    for child in soup.children:
        remove_newlines(child)


def normalize_html(s: str):
    soup = BeautifulSoup(s, 'html.parser')
    remove_newlines(soup)
    return soup.prettify()


def main():
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Normalize HTML files in place')
    parser.add_argument('fns', type=Path, nargs='+', help='files to normalize')
    args = parser.parse_args()

    for fn in args.fns:
        s0 = fn.read_text()
        s = normalize_html(s0)
        fn.write_text(s)


if __name__ == '__main__':
    main()
