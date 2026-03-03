# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNonnormvtdist(RPackage):
	"""Multivariate Lomax (Pareto Type II) and Its Related
Distributions

	Implements calculation of probability density function, cumulative distribution function, equicoordinate quantile function and survival function, and random numbers generation for the following multivariate distributions: Lomax (Pareto Type II), generalized Lomax, Mardia’s Pareto of Type I, Logistic, Burr, Cook-Johnson’s uniform, F and Inverted Beta. See Tapan Nayak (1987) <doi:10.2307/3214068>.
	"""
	
	cran = "NonNorMvtDist" 

	version("1.0.2", md5="b4b1aeb4de1edd50d589d88673529b1a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
