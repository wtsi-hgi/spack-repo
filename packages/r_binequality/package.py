# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinequality(RPackage):
	"""Methods for Analyzing Binned Income Data

	Methods for model selection, model averaging, and calculating metrics, such as the Gini, Theil, Mean Log Deviation, etc, on binned income data where the topmost bin is right-censored.  We provide both a non-parametric method, termed the bounded midpoint estimator (BME), which assigns cases to their bin midpoints; except for the censored bins, where cases are assigned to an income estimated by fitting a Pareto distribution. Because the usual Pareto estimate can be inaccurate or undefined, especially in small samples, we implement a bounded Pareto estimate that yields much better results.  We also provide a parametric approach, which fits distributions from the generalized beta (GB) family. Because some GB distributions can have poor fit or undefined estimates, we fit 10 GB-family distributions and use multimodel inference to obtain definite estimates from the best-fitting distributions. We also provide binned income data from all United States of America school districts, counties, and states.
	"""
	
	cran = "binequality" 

	version("1.0.4", md5="3f6f2f867ad4a1988daa3c5e50a0df23")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gamlss@4.2.7:", type=("build", "run"))
	depends_on("r-gamlss-cens@4.2.7:", type=("build", "run"))
	depends_on("r-gamlss-dist@4.3:", type=("build", "run"))
	depends_on("r-survival@2.37.7:", type=("build", "run"))
	depends_on("r-ineq@0.2.11:", type=("build", "run"))
