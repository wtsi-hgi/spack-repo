# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBws(RPackage):
	"""Bayesian Weighted Sums

	An interface to the Bayesian Weighted Sums model implemented in 'RStan'.
    It estimates the summed effect of multiple, often moderately to highly correlated,
    continuous predictors. Its applications can be found in analysis of exposure mixtures.
    The model was proposed by Hamra, Maclehose, Croen, Kauffman, and
    Newschaffer (2021) <doi:10.3390/ijerph18041373>.
    This implementation includes an extension to model binary outcome.
	"""
	
	cran = "bws" 

	version("0.1.0", md5="ec554366a542e18d8332aeb505dabd5b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
