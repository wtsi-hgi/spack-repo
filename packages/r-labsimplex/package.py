# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLabsimplex(RPackage):
	"""Simplex Optimization Algorithms for Laboratory and Manufacturing
Processes

	Simplex optimization algorithms as firstly proposed by Spendley
    et al. (1962) <doi:10.1080/00401706.1962.10490033> and later modified by 
    Nelder and Mead (1965) <doi:10.1093/comjnl/7.4.308> for laboratory and 
    manufacturing processes. The package also provides tools for graphical 
    representation of the simplexes and some example response surfaces that 
    are useful in illustrating the optimization process.
	"""
	
	cran = "labsimplex" 

	version("0.1.2", md5="57755fab82936807c5ebe73f29fe4915")

	depends_on("r-scatterplot3d@0.3.41:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
