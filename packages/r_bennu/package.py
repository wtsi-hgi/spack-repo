# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBennu(RPackage):
	"""Bayesian Estimation of Naloxone Kit Number Under-Reporting

	Bayesian model and associated tools for generating estimates of 
    total naloxone kit numbers distributed and used from naloxone kit orders 
    data. Provides functions for generating simulated data of naloxone kit use
    and functions for generating samples from the posterior.
	"""
	
	homepage = "https://sempwn.github.io/bennu/"
	cran = "bennu" 

	version("0.3.0", md5="67a1943f92eb87039191938dfe4faf8a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.2:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tidybayes", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
