Example Pandoc Filter for Translating Unicode to LaTeX
------------------------------------------------------
LaTeX markup sucks, so tools like pandoc are great, since they let us write in 
something more sensible like markdown, then use a template to export to latex.
However, special unicode characters or Greek letters still require crap like 
`\Omega`, despite the fact that it's easier than ever to type unicode or 
foreign symbols in this the Year Of Our Lord 2016. 

I wrote this pandoc filter as a proof of concept (it's very incomplete and 
probably broken in some cases). It lets you just write unicode literals in 
markdown, then translates the symbols to the equivalent markup when outputting 
to LaTeX or pdf.

Features
--------
Works transparently in math mode:
- `$Λ$CDM`
- `$Ω_Μ=0.3$`

Automatically converts space-delimited tokens to math mode if needed:
- `z≠3` becomes `$z\ne{}3$`
- `z ≠ 3` becomes `z $\ne{}$ 3`

Needs
-----
- python (probably 3)
- panflutes

Run
---
- pandoc test.md --filter test_filter.py -t latex -o test.tex
- pandoc test.md --filter test_filter.py -t latex -o test.pdf
