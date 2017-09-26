This document is a template for academic writing, science notebook records and reports. It is written in the Markdown format: it’s plain text, human-readable, and can easily be translated into other formats. It allows to write easily structured text with figures, mathematical formulas and bibliographic references without bothering about formatting. One of the biggest advantage is that by separating writing from formatting, I can keep a single source file in a lightweight text format and generate several different output documents in an automatic fashion. These output, for the moment, are: 
+ PDF document generated by LaTeX.
+ stand-alone (self-contained) HTML with integrated images with custom CSS style. Equations are rendered by MathJax.
+ Wordpress post on my personal website. It applies filters to adapt and correct HTML tags (code highlighting, figure captions, etc) to the wordpress environment and wordpress plugins, and uploads the document as a new post to the wordpress server.

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
