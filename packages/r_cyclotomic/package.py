# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCyclotomic(RPackage):
	"""The Field of Cyclotomic Numbers

	The cyclotomic numbers are complex numbers that can be
    thought of as the rational numbers extended with the roots of unity. They
    are represented exactly, enabling exact computations. They contain the
    Gaussian rationals (complex numbers with rational real and imaginary
    parts) as well as the square roots of all rational numbers. They also
    contain the sine and cosine of all rational multiples of pi. The
    algorithms implemented in this package are taken from the 'Haskell'
    package 'cyclotomic', whose algorithms are adapted from code by Martin
    Schoenert and Thomas Breuer in the 'GAP' project
    (<https://www.gap-system.org/>). Cyclotomic numbers have applications in
    number theory, algebraic geometry, algebraic number theory, coding 
    theory, and in the theory of graphs and combinatorics. They have 
    connections to the theory of modular functions and modular curves.
	"""
	
	homepage = "https://github.com/stla/cyclotomic"
	cran = "cyclotomic" 

	version("1.3.0", md5="e69f8d12f82dbcdc511ce4f1449c3a86")

	depends_on("r-intmap", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-maybe", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
	depends_on("r-verylargeintegers", type=("build", "run"))
