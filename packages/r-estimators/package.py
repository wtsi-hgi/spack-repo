# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REstimators(RPackage):
	"""Parameter Estimation

	Implements estimation methods for parameters of common
    distribution families. The common d, p, q, r function family for each
    distribution is enriched with the ll, e, and v counterparts, computing
    the log-likelihood, performing estimation, and calculating the asymptotic
    variance - covariance matrix, respectively. Parameter estimation is
    performed analytically whenever possible.
	"""
	
	homepage = "https://thechibo.github.io/estimators/"
	cran = "estimators" 

	version("0.7.3", md5="fe39a3af50e7d9abcbe06df47e945691")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-distr", type=("build", "run"))
	depends_on("r-ggh4x", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
