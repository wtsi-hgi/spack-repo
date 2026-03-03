# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixedlsr(RPackage):
	"""Mixed, Low-Rank, and Sparse Multivariate Regression on
High-Dimensional Data

	Mixed, low-rank, and sparse multivariate regression ('mixedLSR') provides tools for performing mixture regression when 
  the coefficient matrix is low-rank and sparse. 'mixedLSR' allows subgroup identification by alternating optimization 
  with simulated annealing to encourage global optimum convergence. This method is data-adaptive, automatically 
  performing parameter selection to identify low-rank substructures in the coefficient matrix. 
	"""
	
	homepage = "https://alexanderjwhite.github.io/mixedLSR/"
	cran = "mixedLSR" 

	version("0.1.0", md5="e9849a1710547f688277a624cdf3f713")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-grpreg", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
