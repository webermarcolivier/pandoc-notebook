#!/usr/bin/env python3

import re
import regex

if __name__ == '__main__':

    with open('wordpress.css', 'r') as f:
        cssContent = f.read()

    # Scaled all rem values to match rootsize of Wordpress theme
    cssContentNew = re.sub(r'([0-9.]+)rem',
                           lambda match: "{:f}rem".format(2.2*float(match.group(1))),
                           cssContent)

    # add parent selector to apply style only to post content
    # 
    cssContentNew = re.sub(r'((([ \-.\d\w\:()]+?,)(?=.*?\{\s*\n))|([ \-.\d\w\:()]+?\s*(?=\{\s*\n)))',
                           r' div.entry-content \1',
                           cssContentNew)

    with open('wordpress.scaled.css', 'w') as f:
        f.write(cssContentNew)
