# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIgcop(RPackage):
	"""Computational Tools for the IG and IGL Copula Families

	Compute distributional quantities for an
    Integrated Gamma (IG) or Integrated Gamma Limit (IGL) copula, such
    as a cdf and density. Compute corresponding conditional quantities
    such as the cdf and quantiles. Generate
    data from an IG or IGL copula. See the vignette for formulas,
    or for a derivation, see Coia, V (2017) "Forecasting of Nonlinear 
    Extreme Quantiles Using Copula Models." PhD Dissertation, 
    The University of British Columbia.
	"""
	
	cran = "igcop" 

	version("1.0.2", md5="e15ab6ef239ddf35c7c6920aadc4dbd4")

	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
