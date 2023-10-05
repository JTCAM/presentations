(TeX-add-style-hook
 "pres2023_169"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("textpos" "absolute" "overlay") ("beamerthemeboxes" "footheight=1em")))
   (TeX-run-style-hooks
    "graphicx"
    "beamerprosper"
    "xmpmulti"
    "array"
    "pgf"
    "wasysym"
    "pxfonts"
    "xspace"
    "marvosym"
    "textpos"
    "lscape"
    "float"
    "amssymb"
    "amsmath"
    "euscript"
    "beamerthemeboxes")
   (TeX-add-symbols
    '("beq" 1)
    '("eq" 1)
    '("figh" 2)
    '("fig" 2)
    '("titleframe" 1)
    '("myref" 1)
    '("mref" 1)
    '("alertref" 1)
    '("alertb" 1)
    '("green" 1)
    '("eqc" 1)
    "ds"))
 :latex)

