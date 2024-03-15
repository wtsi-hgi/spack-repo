# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarkets(RPackage):
	"""Estimation Methods for Markets in Equilibrium and Disequilibrium

	Provides estimation methods for markets in equilibrium and
    disequilibrium. Supports the estimation of an equilibrium and
    four disequilibrium models with both correlated and independent shocks.
    Also provides post-estimation analysis tools, such as aggregation,
    marginal effect, and shortage calculations. See Karapanagiotis (2024)
    <doi:10.18637/jss.v108.i02> for an overview of the functionality 
    and examples. The estimation methods are based on full information
    maximum likelihood techniques given in
    Maddala and Nelson (1974) <doi:10.2307/1914215>. They are implemented
    using the analytic derivative expressions calculated in
    Karapanagiotis (2020) <doi:10.2139/ssrn.3525622>. Standard
    errors can be estimated by adjusting for heteroscedasticity or clustering.
    The equilibrium estimation constitutes a case of a system of linear,
    simultaneous equations. Instead, the disequilibrium models replace the
    market-clearing condition with a non-linear,
    short-side rule and allow for different specifications of price dynamics. 
	"""
	
	homepage = "https://github.com/pi-kappa-devel/markets/"
	cran = "markets" 

	version("1.1.5", md5="b0c58415cc672332b460f1a1c804b09e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr@0.7.6:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-mass@7.3.50:", type=("build", "run"))
	depends_on("r-rlang@0.2.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppgsl", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
