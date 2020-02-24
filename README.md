# md2mla

This is a script which converts a Markdown file to a PDF in MLA format,
including citations.

This script accepts the names of Markdown files as arguments, and generates a
PDF in the same directory for each Markdown file.

Each Markdown file must start with a YAML front matter block. This is a format
understood by Pandoc and other Markdown processors for specifying document
metadata.

Here is an example markdown document:

```
---
firstname: Harrier
lastname: Du Bois
professor: Kim Kitsuragi
course: HDB-041
title: The Conquest of Revachol
date: 15 October 2019
bibliography: revachol.bib
---

This is the first paragraph of the essay.
```

The `bibliography` key is optional and allows for specifying the name of the
BibTeX file containing references. If this key is included, an MLA-style
bibliography will automatically be generated at the end of the document.
In-text citations can be added using [Pandoc's Markdown citation
syntax](https://pandoc.org/MANUAL.html#citations). Most reference management
software (like Zotero) supports exporting references as a BibTeX file.

## Dependencies
- `pandoc`
- `latexmk`
- `biber`
- `texlive-latex-recommended`
- `texlive-latex-extra`
