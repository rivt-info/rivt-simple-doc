#! python
# %% Start
import rivtlib.rvapi as rv

rv.M("""Meta Data
    
    rv_authD = {
        "authors": "rholland",
        "version": "0.5.1",
        "email": "rod.h.holland@gmail.com",
        "repo": "https://github.com/rivt-info/rivt-simple-single-doc",
        "license": "https://opensource.org/license/mit/",
        "fork1": ["", "", "", ""],
        }
    
    rv_headerL = ["date", "time", "file", "version"]
    
    """)

rv.I("""Load Combinations and Geometry 

    Dead and live load contributions to beam UDL.

    ASCE 7-05 Load Effects _[T]

    =============   ==============================================
    Equation No.    Load Combination
    =============   ==============================================
    16-1            1.4(D+F)
    16-2            1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R)
    16-3            1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W)
    =============   ==============================================

    | IMG | rvlocal | beam.png | 0.5, Beam Geometry _[F]
    """)

# %%
rv.V("""Loads and Geometry 

    _[[V]] Dead and Live Loads
    D_1 = 3.8 | PSF, KPA, 2 | joists          
    D_2 = 2.1 | PSF, KPA, 2 | plywood          
    D_3 = 10.0 | PSF, KPA, 2 | partitions       
    D_4 = 2 * 0.5 | KLF, KNLM, 2 | fixed machinery  
    L_1 = 40  | PSF, KPA, 2 | ASCE7-O5  
    _[[Q]]

    _[[V]] Beam tributary width and span
    w_1 = 2 | FT, M, 2 | beam spacing  
    l_1 = 14 | FT, M, 2 | beam span 
    _[[Q]]
    """)

rv.V("""Calculate UDL Beam Moment

    Maximum bending moment

    Total UDL factored dead load  _[E]
    DL_1 = 1.2 * (w_1 *(D_1 + D_2 + D_3) + D_4) |

    Total UDL factored live load  _[E]
    LL_1 = 1.6 * w_1 * L_1
    omega_1 = DL_1 + LL_1

    Bending moment at mid-span    _[E]
    M_1 = omega_1 * l_1**2 / 8
    """)

# %%
rv.D("""Publish Doc

    | DOC | rstpdf | rivtdoc1.ini 
    """)
