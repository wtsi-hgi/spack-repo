# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBernadette(RPackage):
	"""Bayesian Inference and Model Selection for Stochastic Epidemics

	Bayesian analysis for stochastic extensions of non-linear
    dynamic systems using advanced computational algorithms. Described in Bouranis, L., 
    Demiris, N., Kalogeropoulos, K., and Ntzoufras, I. (2022) <arXiv:2211.15229>.
	"""
	
	homepage = "https://bernadette-eu.github.io/"
	cran = "Bernadette" 

	version("1.1.5", md5="c718933218be6b7e134750e2e2386bab")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp@1.0.8.3:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstantools", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-bh@1.78.0.0:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.9.1:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
