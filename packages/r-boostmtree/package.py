# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoostmtree(RPackage):
	"""Boosted Multivariate Trees for Longitudinal Data

	Implements Friedman's gradient descent boosting algorithm for modeling longitudinal response using multivariate tree base learners. Longitudinal response could be continuous, binary, nominal or ordinal.  A time-covariate interaction effect is modeled using penalized B-splines (P-splines) with estimated adaptive smoothing parameter. Although the package is design for longitudinal data, it can handle cross-sectional data as well. Implementation details are provided in Pande et al. (2017), Mach Learn <DOI:10.1007/s10994-016-5597-1>. 
	"""
	
	homepage = "https://ishwaran.org/ishwaran.html"
	cran = "boostmtree" 

	version("1.5.1", md5="f47639bb265de6cd95d84ba016ac83f5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-randomforestsrc@2.9:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
