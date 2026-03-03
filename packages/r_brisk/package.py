# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrisk(RPackage):
	"""Bayesian Benefit Risk Analysis

	Quantitative methods for benefit-risk analysis help to condense
    complex decisions into a univariate metric describing the overall benefit
    relative to risk.  One approach is to use the multi-criteria decision
    analysis framework (MCDA), as in Mussen, Salek, and Walker
    (2007) <doi:10.1002/pds.1435>.  Bayesian benefit-risk
    analysis incorporates uncertainty through posterior distributions which are
    inputs to the benefit-risk framework.  The brisk package provides functions
    to assist with Bayesian benefit-risk analyses, such as MCDA.
    Users input posterior samples, utility functions, weights, and the package
    outputs quantitative benefit-risk scores.  The posterior of the benefit-risk
    scores for each group can be compared.  Some plotting capabilities are also
    included.
	"""
	
	homepage = "https://rich-payne.github.io/brisk/"
	cran = "brisk" 

	version("0.1.0", md5="e5bc36a811f21942d4d3a350091e5f84")

	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ellipsis@0.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-hitandrun@0.5:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
