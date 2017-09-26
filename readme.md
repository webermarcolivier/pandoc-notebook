This script uses pandoc to convert a Jupyter notebook or a markdown file to three different formats:
- PDF using xelatex
- Self-contained HTML with custom CSS style and images (no additional files required to load to HTML). Equations are rendered by MathJax.
- Wordpress post. It applies filters to adapt and correct HTML tags (code highlighting, figure captions, etc) to the wordpress environment and wordpress plugins, and uploads the document as a new post to the wordpress server.

The script handles citations using the pandoc-citeproc filter, and figure numbering using the pandoc-fignos filter.

For the self-contained HTML, I used the package [MegaType](https://github.com/StudioThick/megatype) (SCSS template) to define all font sizes and line heights of the different elements in order to create a vertical rhythm, aligning the text baseline on a baseline grid

Filters for wordpress:
- images with wordpress fullsize class and link to open image in lightbox
- correct figure captions
- code highlighting with Crayon plugin
- latex tags with QuickLatex plugin
- table of contents plugin (optional)

For more extensive information see the example jupyter notebook in the Example folder.

Tested with:
+ pandoc 1.16.0.2
+ MegaType 1.1.2
+ MathJax 2.7
+ wordpress 4.7.6
+ wordpress plugins:
  + WP QuickLaTeX 3.8.4
  + Crayon 2.8.4
  + Table of Contents Plus 1601
