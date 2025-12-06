#! python
import rivtlib.rvapi as rv

# rv_localB=True

# %% loads

rv.I("""Load Combinations

    ASCE 7-05 Load Effects _[T]

    =============   ==============================================
    Equation No.    Load Combination
    =============   ==============================================
    16-1            1.4(D+F)
    16-2            1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R)
    16-3            1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W)
    =============   ==============================================

    | IMAGE | beam.png | 0.35, Beam Geometry _[I]

    """)

# %% values
rv.V("""UDL and Beam Geometry

    Beam Loads and Properties _[T]
    D_1 := 3.8*PSF | PSF, kPA, 2 | joists DL         
    D_2 := 2.1*PSF | PSF, kPA, 2 | plywood DL          
    D_3 := 10.0*PSF | PSF, kPA, 2 | partitions DL       
    D_4 := 1.1*KIP__FT | KIP__FT, kN__M, 2 | fixed machinery  DL
    L_1 := 40*PSF | PSF, kPA, 2 | ASCE7-O5 LL 
    
    | VALUES | beam1-v.csv | Beam Geometry _[T]

    Total UDL factored dead load  _[E]
    dl_1 <= 1.2 * (W_1 *(D_1 + D_2 + D_3) + D_4) | KIP__FT, kN__M, 2 | ASCE7-05 Eq. 16-2

    Total UDL factored live load  _[E]
    ll_1 <= 1.6 * W_1 * L_1 | KIP__FT, kN__M, 2 | ASCE7-05 Eq. 16-2
    
    Total Load  _[E]
    omega_1 <= dl_1 + ll_1 | KIP__FT, kN__M, 2 | ASCE7-05 Eq. 16-2

    Bending moment at mid-span  _[E]
    m_1 <= omega_1 * S_1**2 / 8 | KIP_FT, kN_M, 2 | mid-span UDL moment 

    | PYTHON | sectionprop.py | rivt, nodocstring

    Calculate section modulus from function _[E]
    section_1 <= rectsect(10*IN, 18*IN) | IN3, CM3, 2 | rectangular section modulus

    Calculate moment of inertia from function _[E]
    inertia_1 <= rectinertia(10*IN, 18*IN) | IN4, CM4, 1 | rectangular moment of inertia

    """)

# %% tool
rv.S("""Metadata

    
    _[[PYTHON]] Author data
    rv_authD = {
    "authors": ["rholland"],
    "version": "0.7.1",
    "email": "rod.h.holland@gmail.com",
    "repo": "https://github.com/rivt-info/rivt-simple-single-doc",
    "license": "https://opensource.org/license/mit/",
    "fork1": ["author", "version", "email", "repo"],
    "fork2": [],
    }
    _[[END]]

    """)

rv.S("""Publish Doc 

    _[[LAYOUT]]
    rv_docnameS = "Beam Moment"
    rv_headerL = ["date", "time", "file", "version"]
    _[[END]]
    
    | PUBLISH | simpledoc.txt | text

    """)
