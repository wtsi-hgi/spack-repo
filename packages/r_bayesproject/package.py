# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesproject(RPackage):
	"""Fast Projection Direction for Multivariate Changepoint Detection

	Implementations in 'cpp' of the BayesProject algorithm (see G. Hahn, P. Fearnhead, I.A. Eckley (2020) <doi:10.1007/s11222-020-09966-2>) which implements a fast approach to compute a projection direction for multivariate changepoint detection, as well as the sum-cusum and max-cusum methods, and a wild binary segmentation wrapper for all algorithms.
	"""
	
	cran = "BayesProject" 

	version("1.0", md5="cf0475a404e2a847f1378555e2263160")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
