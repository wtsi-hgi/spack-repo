# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcfactorstan(RPackage):
	"""Stan Models for the Paired Comparison Factor Model

	Provides convenience functions and pre-programmed
    Stan models related to the paired comparison factor model. Its purpose
    is to make fitting paired comparison data using Stan easy. This
    package is described in Pritikin (2020) <doi:10.1016/j.heliyon.2020.e04821>.
	"""
	
	homepage = "https://github.com/jpritikin/pcFactorStan"
	cran = "pcFactorStan" 

	version("1.5.4", md5="d8d13c58efeef7e1c7238c2230530e55")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.2:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
