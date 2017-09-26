#!/usr/bin/env python3

import argparse
import re
from pathlib import Path

argParser = argparse.ArgumentParser()
argParser.add_argument('filename', type=str)
args = argParser.parse_args()

with Path(args.filename).open('r') as f:
    htmlText = f.read()

htmlMatch = re.search(r'^' + re.escape('<!DOCTYPE html><html><head><meta charset="utf-8"><style>@font-face {') +
                      r'.*?\}' + r'(.*?)</style>' + r'.*?<body>' +
                      r'(.*?)</body></html>',
                      htmlText, re.DOTALL)

CSSText = htmlMatch.group(1)
htmlText = htmlMatch.group(2)

# Introduce the class attribute to the <pre> tag to disable Crayon Syntax highlighter in wordpress
htmlText = re.sub(r'<pre>', r'<pre class="crayon:false">', htmlText, flags=re.DOTALL)

# When writing in markdown a single line code snippet but with the triple quotes ```
# the sublime markdown preview parser translate it into <pre><code></code></pre>
# which result in weird separation between lines of code.
# Any code block should be enclosed only in <pre></pre> tags.
htmlText = re.sub(r'<pre(.*?)><code>', r'<pre\1>', htmlText)
htmlText = re.sub(r'</code></pre>', r'</pre>', htmlText)

# Remove the styling of the body width and box style
CSSText = re.sub(r'\* \{.*box-sizing.*?\}', r'', CSSText, flags=re.DOTALL)
CSSText = re.sub(r'body \{.*width.*?\}', r'', CSSText, flags=re.DOTALL)
CSSText = re.sub(r'body \.markdown-body\{.*?\}', r'', CSSText, flags=re.DOTALL)

with Path(args.filename + '.body').open('w') as f:
    f.write(htmlText)

with Path(args.filename + '.css').open('w') as f:
    f.write(CSSText)

