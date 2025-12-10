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

    Bending Stress Formula _[E]
    σ1 = M1 / S1 _[A]

    """)

# %% values
rv.V("""Loads and Geometry 

    Beam Loads and Properties _[T]
    D_1 := 3.8*psf | psf, kPA, 2 | joists DL         
    D_2 := 2.1*psf | psf, kPA, 2 | plywood DL          
    D_3 := 10.0*psf | psf, kPA, 2 | partitions DL       
    D_4 := 2*0.5*klf |klf, kN_m , 2 | fixed machinery  DL
    L_1 := 40*psf | psf, kPA, 2 | ASCE7-O5 LL 
    
    | VALUES | beam1-v.csv | Beam Geometry _[T]

    Uniform Distributed Loads
    dl_1 <= 1.2 * (W_1 *(D_1 + D_2 + D_3) + D_4) | klf, kN_m, 2 | dead load : ASCE7-05 2.3.2  _[E]

    ll_1 <= 1.6 * W_1 * L_1 | klf, kN_m, 2 | live load : ASCE7-05 2.3.2 _[E]
    
    omega_1 <= dl_1 + ll_1 | klf, kN_m, 2 | total load : ASCE7-05 2.3.2 _[E]

    """)

# %% section
rv.V("""Beam Section Properties

    | PYTHON | sectionprop.py | rivt, nodocstring

    section_1 <= rectsect(10*inch, 18*inch) | in3, cm3, 2 | rectangular section modulus _[E]

    inertia_1 <= rectinertia(10*inch, 18*inch) | in4, cm4, 1 | rectangular moment of inertia _[E]

    """)

rv.V("""Force and Stress
        
        m_1 <= omega_1 * S_1**2 / 8 | ftkips, mkN, 2 | mid-span UDL moment _[E]

        fb_1 <= m_1 / section_1 | psi, MPA, 1 | bending stress _[E]
    
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

rv.D("""Publish Doc 

    _[[LAYOUT]]
    rv_docnameS = "Beam Moment"
    rv_headerL = ["date", "time", "file", "version"]
    _[[END]]
    

    | PUBLISH | rivt | html


    """)
