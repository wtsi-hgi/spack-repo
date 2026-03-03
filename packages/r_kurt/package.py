# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKurt(RPackage):
	"""Performs Kurtosis-Based Statistical Analyses

	Computes measures of multivariate kurtosis, matrices of fourth-order moments and cumulants, kurtosis-based projection pursuit.
             Franceschini, C. and Loperfido, N. (2018, ISBN:978-3-319-73905-2). "An Algorithm for Finding Projections with Extreme Kurtosis".
             Loperfido, N. (2017,ISSN:0024-3795). "A New Kurtosis Matrix, with Statistical Applications".
	"""
	
	cran = "Kurt" 

	version("1.1", md5="a49f1a84668aefa72fd0fbcd82ad1898")

	depends_on("r-labstatr@1.0.11:", type=("build", "run"))
	depends_on("r-matrixcalc@1.0.5:", type=("build", "run"))
	depends_on("r-polynom@1.4.0:", type=("build", "run"))
	depends_on("r-expm@0.999.6:", type=("build", "run"))
