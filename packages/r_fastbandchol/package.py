# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastbandchol(RPackage):
	"""Fast Estimation of a Covariance Matrix by Banding the Cholesky
Factor

	Fast and numerically stable estimation of a covariance matrix by banding the Cholesky factor using a modified Gram-Schmidt algorithm implemented in RcppArmadilo. See <http://stat.umn.edu/~molst029> for details on the algorithm. 
	"""
	
	cran = "FastBandChol" 

	version("0.1.1", md5="611ffb88eabe00cf395c9e0657bed678")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
