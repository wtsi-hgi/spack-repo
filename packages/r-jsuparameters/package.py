# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJsuparameters(RPackage):
	"""Estimate Parameters of the Best-Fitting JohnsonSU Distribution

	Uses least squares optimisation to estimate the parameters of the best-fitting JohnsonSU distribution for a given dataset, with the possibility of the distributions corresponding to the limiting cases of the JohnsonSU distribution. The code for the Golden Section Search used in the optimisation has been adapted from E. Cai. This package has been created as an extension of my Master's thesis. E. Cai (2013, "Scripts and Functions: Using R to Implement the Golden Section Search Method for Numerical Optimization", <https://chemicalstatistician.wordpress.com/2013/04/22/using-r-to-implement-the-golden-bisection-method/>).
	"""
	
	cran = "JSUparameters" 

	version("1.0.0", md5="ea8c849e1769c8a5e808709433461ace")

