# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpsurv(RPackage):
	"""Bernstein Polynomial Based Semiparametric Survival Analysis

	A set of reliable routines to ease semiparametric survival regression modeling based on Bernstein polynomials. 'spsurv' includes proportional hazards, proportional odds and accelerated failure time frameworks for right-censored data. RV Panaro (2020) <arXiv:2003.10548>.
	"""
	
	cran = "spsurv" 

	version("1.0.0", md5="bc399d9038dee8938d50ada7a337985e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival@2.44.1.1:", type=("build", "run"))
	depends_on("r-loo@2.1:", type=("build", "run"))
	depends_on("r-coda@0.19.3:", type=("build", "run"))
	depends_on("r-mass@7.3.51.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@1.5.1:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
