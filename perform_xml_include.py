#!/usr/bin/env python3.7

import re
from pathlib import Path
from subprocess import check_call
from xml.sax.saxutils import escape

def main():
    fns = list(Path('.').glob('*.xml'))
    def repl(m):
        href, = m.groups()
        s = Path(href).read_text()
        check_call(['git', 'rm', href])
        return escape(s)

    for fn in fns:
        s0 = fn.read_text()
        s = re.sub(r'<xi:include[^>]*href="([^"]+)"[^>]*>', repl, s0)
        fn.write_text(s)

if __name__ == '__main__':
    main()
