
   .. header:: 
      2025-12-17 - 12:28AM  |  rholland  |  rv000-single-doc  v0.7.1     

[ 1i ] Load Combinations
-------------------------------------------------------------------------------- 

**Table 1**: ASCE 7-05 Load Effects

============= ================================================
Equation No.    Load Combination
============= ================================================
16-1           1.4(D+F)
16-2           1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R)
16-3           1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W)
============= ================================================
 


.. image:: C:/git/rivt-single-doc-git/s-beam.png
   :width: 65 %
   :align: center


.. class:: center 

    Beam Geometry

 
.. raw:: html

   <p align="right">Bending Stress Formula [Eq 1]</p> 


.. code:: 

             M₁
     σ₁ = ──
          S₁


 
 

[ 2v ] Loads and Geometry
-------------------------------------------------------------------------------- 

**Table 2**: Beam Loads and Properties

==========  =========  ==========  ===================
variable        value     [value]  description
==========  =========  ==========  ===================
D_1          3.80 psf    0.18 kPA  joists DL
D_2          2.10 psf    0.10 kPA  plywood DL
D_3         10.00 psf    0.48 kPA  partitions DL
D_4          1.00 klf  14.59 kN_m  fixed machinery  DL
L_1         40.00 psf    1.92 kPA  ASCE7-O5 LL
==========  =========  ==========  =================== 

**Table 3**: Beam Geometry [file: s-beam1-v.csv]

==========  ========  =========  =============
variable       value    [value]  description
==========  ========  =========  =============
W_1          2.00 ft     0.61 m  beam spacing
S_1         14.00 ft     4.27 m  beam span
==========  ========  =========  =============

 
 
Uniform Distributed Loads


.. raw:: html

   <p align="right">dead load : ASCE7-05 2.3.2   [Eq 2]</p> 


.. code:: 

    dl₁ = 1.2⋅D₄ + 1.2⋅W₁⋅(D₁ + D₂ + D₃)

========  ==========  ===  ========  =====  =======  =========  ========
 dl_1      [dl_1 ]     |     D_2      D_4     W_1       D_3       D_1
========  ==========  ===  ========  =====  =======  =========  ========
1.24 klf  18.07 kN_m   |   2.10 psf   klf   2.00 ft  10.00 psf  3.80 psf
========  ==========  ===  ========  =====  =======  =========  ========
 


.. raw:: html

   <p align="right">live load : ASCE7-05 2.3.2  [Eq 3]</p> 


.. code:: 

    ll₁ = 1.6⋅L₁⋅W₁

========  =========  ===  =========  =======
 ll_1      [ll_1 ]    |      L_1       W_1
========  =========  ===  =========  =======
0.13 klf  1.87 kN_m   |   40.00 psf  2.00 ft
========  =========  ===  =========  =======
 


.. raw:: html

   <p align="right">total load : ASCE7-05 2.3.2  [Eq 4]</p> 


.. code:: 

    dl₁ = -ll₁ + ω₁

==========  ============  ===  ========  =============
 omega_1     [omega_1 ]    |     dl_1        ll_1
==========  ============  ===  ========  =============
 1.37 klf    19.94 kN_m    |   1.24 klf  128.00 ft·psf
==========  ============  ===  ========  =============
 
 

[ 3v ] Beam Section Properties
-------------------------------------------------------------------------------- 
**[Python file read:** s-sectprop.py **]**



 


.. raw:: html

   <p align="right">function: rect sect modulus  [Eq 5]</p> 


.. code:: 

    section₁ = rectsect(10⋅inch, 18⋅inch)

============  ==============  ===  ======
 section_1     [section_1 ]    |    inch
============  ==============  ===  ======
 540.00 in3    8849.01 cm3     |    inch
============  ==============  ===  ======
 


.. raw:: html

   <p align="right">function: rect moment inertia  [Eq 6]</p> 


.. code:: 

    inertia₁ = rectinertia(10⋅inch, 18⋅inch)

============  ==============  ===  ======
 inertia_1     [inertia_1 ]    |    inch
============  ==============  ===  ======
 4860.0 in4    202288.5 cm4    |    inch
============  ==============  ===  ======
 
 

[ 4v ] Force and Stress
-------------------------------------------------------------------------------- 


.. raw:: html

   <p align="right">mid-span UDL moment  [Eq 7]</p> 


.. code:: 

           2   
         S₁ ⋅ω₁
    m₁ = ──────
           8   

===========  =========  ===  =========  ========
   m_1        [m_1 ]     |    omega_1     S_1
===========  =========  ===  =========  ========
33.47 ftkip  45.38 mkN   |   1.37 klf   14.00 ft
===========  =========  ===  =========  ========
 


.. raw:: html

   <p align="right">bending stress  [Eq 8]</p> 


.. code:: 

             m₁   
    fb₁ = ────────
          section₁

=========  =========  ===  ===========  ============
  fb_1      [fb_1 ]    |    section_1       m_1
=========  =========  ===  ===========  ============
743.8 psi   5.1 MPA    |   540.0 inch3  33.5 ft2·klf
=========  =========  ===  ===========  ============
 
 

