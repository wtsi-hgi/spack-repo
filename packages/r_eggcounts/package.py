# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REggcounts(RPackage):
	"""Hierarchical Modelling of Faecal Egg Counts

	An implementation of Bayesian hierarchical models
    for faecal egg count data to assess anthelmintic
    efficacy. Bayesian inference is done via MCMC sampling using 'Stan' <https://mc-stan.org/>.
	"""
	
	homepage = "https://www.math.uzh.ch/pages/eggcount/"
	cran = "eggCounts" 

	version("2.4", md5="ca9859e3aa07f596d90d87e1ad328028")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@1.0.7:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.3.1:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-bh@1.75:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.9.1:", type=("build", "run"))
	depends_on("r-rcppparallel@5.1.4:", type=("build", "run"))
