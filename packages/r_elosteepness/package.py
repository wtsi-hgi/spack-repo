# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElosteepness(RPackage):
	"""Bayesian Dominance Hierarchy Steepness via Elo Rating and
David's Scores

	Obtain Bayesian posterior distributions of dominance hierarchy steepness (Neumann and Fischer (2023) <doi:10.1111/2041-210X.14021>). Steepness estimation is based on Bayesian implementations of either Elo-rating or David's scores. 
	"""
	
	homepage = "https://github.com/gobbios/EloSteepness"
	cran = "EloSteepness" 

	version("0.5.0", md5="3a3e65062b52356de4278f9b74385c13")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-elorating", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-anidom", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
