# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpbayessurv(RPackage):
	"""Bayesian Modeling and Analysis of Spatially Correlated Survival
Data

	Provides several Bayesian survival models for spatial/non-spatial survival data: proportional hazards (PH), accelerated failure time (AFT), proportional odds (PO), and accelerated hazards (AH), a super model that includes PH, AFT, PO and AH as special cases, Bayesian nonparametric nonproportional hazards (LDDPM), generalized accelerated failure time (GAFT), and spatially smoothed Polya tree density estimation. The spatial dependence is modeled via frailties under PH, AFT, PO, AH and GAFT, and via copulas under LDDPM and PH. Model choice is carried out via the logarithm of the pseudo marginal likelihood (LPML), the deviance information criterion (DIC), and the Watanabe-Akaike information criterion (WAIC). See Zhou, Hanson and Zhang (2020) <doi:10.18637/jss.v092.i09>. 
	"""
	
	cran = "spBayesSurv" 

	version("1.1.7", md5="fe850bfe8f90e5454990a3e3bc76d9bf")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.8.500:", type=("build", "run"))
