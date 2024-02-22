# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimsimplex(RPackage):
	"""R Port of the 'Scilab' Optimsimplex Module

	Provides a building block for optimization algorithms
        based on a simplex. The 'optimsimplex' package may be used in the
        following optimization methods: the simplex method of Spendley
        et al. (1962) <doi:10.1080/00401706.1962.10490033>, the method of 
        Nelder and Mead (1965) <doi:10.1093/comjnl/7.4.308>, Box's algorithm for
        constrained optimization (1965) <doi:10.1093/comjnl/8.1.42>, the 
        multi-dimensional search by Torczon (1989) 
        <https://www.cs.wm.edu/~va/research/thesis.pdf>, etc...
	"""
	
	cran = "optimsimplex" 

	version("1.0-8", md5="05f4199170d3021f99b0f2ca87bd664f")

	depends_on("r-optimbase@1.0.8:", type=("build", "run"))
