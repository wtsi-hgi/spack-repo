# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMomtrunc(RPackage):
	"""Moments of Folded and Doubly Truncated Multivariate
Distributions

	It computes arbitrary products moments (mean vector and variance-covariance matrix), for some double truncated (and folded) multivariate distributions. These distributions belong to the family of selection elliptical distributions, which includes well known skewed distributions as the unified skew-t distribution (SUT) and its particular cases as the extended skew-t (EST), skew-t (ST) and the symmetric student-t (T) distribution. Analogous normal cases unified skew-normal (SUN), extended skew-normal (ESN), skew-normal (SN), and symmetric normal (N) are also included. Density, probabilities and random deviates are also offered for these members.
	"""
	
	cran = "MomTrunc" 

	version("6.0", md5="685edec28fbd1c5dea4935784902bce0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp@1.0.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-tlrmvnmvt@1.1:", type=("build", "run"))
	depends_on("r-hypergeo", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
