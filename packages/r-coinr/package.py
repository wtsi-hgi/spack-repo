# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoinr(RPackage):
	"""Composite Indicator Construction and Analysis

	A comprehensive high-level package, for composite indicator construction and analysis. It is a "development environment"
    for composite indicators and scoreboards, which includes utilities for construction (indicator selection, denomination, imputation,
    data treatment, normalisation, weighting and aggregation) and analysis (multivariate analysis, correlation plotting, short cuts for
    principal component analysis, global sensitivity analysis, and more). A composite indicator is completely encapsulated inside a single
    hierarchical list called a "coin". This allows a fast and efficient work flow, as well as making quick copies, testing methodological variations and making comparisons.
    It also includes many plotting options, both statistical (scatter plots, distribution plots) as well as for presenting results.
	"""
	
	homepage = "https://bluefoxr.github.io/COINr/"
	cran = "COINr" 

	version("1.1.7", md5="b32bf8514f698a1e1036d5668d8e5183")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-openxlsx@4.2.3:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.3:", type=("build", "run"))
	depends_on("r-readxl@1.3.1:", type=("build", "run"))
