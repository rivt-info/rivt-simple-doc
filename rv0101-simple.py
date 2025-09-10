#! python
# %% Start
import rivtlib.rvapi as rv

# %% Project
rv.I("""Project Summary 

    This report **describes** the structural design of a solar canopy that
    covers a residential patio located in the City of Larkspur, California. It
    includes the design of a concrete slab and *stem* wall, steel tube frame,
    and clip attachments of solar panels to the frame.

    center this text _[C]

    |TABLE| i01/project-data.csv | Title of table, 40, l, [] _[T]
    """)

# %% Overview
rv.I("""Overview and Codes 

    This report describes the **structural** design of a solar canopy
    *covering* a residential patio located in the City of Larkspur, California.
    It includes the design of a concrete slab and *stem* wall, steel tube
    frame, and clip attachments of solar panels to the frame.

    |IMG| i01/rivt01.png | Wind Load 1, 30 _[F]

    some text between

    |IMG| i01/site01.png | Wind Load 2, 30 _[F]

    text followed by an equation

    wt2 = (1/sin(x)) + 4 + a2 * dl2 / 2   _[S]

    New Table _[T]

    ======= ======== ======
    col1     col2    col3
    ======= ======== ======
    A1       23       10
    B1       11.1     15.0
    ======= ======== ======

    |TEXT| i01/example1.txt | preformat, red
    """)

rv.I("""--code tables 
    **Building Codes and Jurisdiction**

    - City of Larkspur, California
    - 2019 California Building Code[CBC]
    - 2019 California Residential Code[CRC]

    ==========

    |TABLE| i01/cbc2019A_stds.csv | My Table, 53, l, [], _[T]

    Design load combinations are from *California Building and Residential*
    *Codes* and are summarized in the following tables.

    |TABLE| i01/load_types01.csv | Another Table Title, 40, l, [], _[T]

    # this is a comment

    |TABLE| i01/asce7_load_comb.csv | Load Combinations 2, 55, c, [], _[T]
    """)

# %% Gravity
rv.V("""Gravity Loads and Seismic Mass

    Dimensions for the first floor structural layout.

    First Floor Dimensions _[[V]]
    area1 := 10700 * SF |  SF, SM, 2 | roof area
    area2 := 10000 * FT * 10 * FT | SF, SM , 2| floor area
    area3 := 5 * FT * 5 * FT | SF, SM, 2| floor area
    ht1 := 9.0 * FT | FT, M, 2 | wall height 
    len1 := 110 * FT | FT, M, 2 | interior wall length 
    len2 := 155 * FT  | FT, M, 2| exterior wall length
    udl1 := 12.2 * PSF  | PSF, PA, 2 | dead load 1
    udl2 := 22.2 * PSF  | PSF, PA, 2 | dead load 2
    _[[Q]]

    Additional values from a file.

    |VALUE| v01/test1.csv | Another values table _[T]

    Floor and wall areas _[E]
    
    ========== 
    
    wt2 := area2 * udl1  | KIPS, N, 2, 2 | ACI-315-05

    wt3 := area3 * udl2 * 30/40 | LBF, N, 1, 2 | ACI-315 - 05 

    |VALUE| v01/test2.csv | Exterior wall - total area load _[T]
    """)

# %% Abbreviations
rv.S("""Abbreviations and References 

    **Reference Standards**

    |TEXT| i02/references.txt | plain

    **Drawing List**

    |TEXT| i02/drawing_list.txt | plain

    **Abbreviations**

    |TEXT| i01/abbrev_terms.tex | latex

    **Abbreviations - Math**

    |TEXT| i01/abbrev_math.tex | latex
    """)

# %% Publish
rv.P("""Publish 

    |DOC| rstpdf | rivtdoc1.ini 

    |ATTACH| attach/test1.pdf | a pdf title
    
    # |DOC| text | rivtdoc1.ini | cover1.txt
    
    # |DOC| rst2pdf | rivtdoc1.ini
    """)
