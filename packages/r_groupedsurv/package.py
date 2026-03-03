# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGroupedsurv(RPackage):
	"""Efficient Estimation of Grouped Survival Models Using the Exact
Likelihood Function

	These 'Rcpp'-based functions compute the efficient score statistics for grouped time-to-event data (Prentice and Gloeckler, 1978), with the optional inclusion of baseline covariates. Functions for estimating the parameter of interest and nuisance parameters, including baseline hazards, using maximum likelihood are also provided. A parallel set of functions allow for the incorporation of family structure of related individuals (e.g., trios). Note that the current implementation of the frailty model (Ripatti and Palmgren, 2000) is sensitive to departures from model assumptions, and should be considered experimental. For these data, the exact proportional-hazards-model-based likelihood is computed by evaluating multiple variable integration. The integration is accomplished using the 'Cuba' library (Hahn, 2005), and the source files are included in this package. The maximization process is carried out using Brent's algorithm, with the C++ code file from John Burkardt and John Denker (Brent, 2002).
	"""
	
	cran = "groupedSurv" 

	version("1.0.5.1", md5="5decb2dd09c6c9ce8b35f9a522a05202")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
