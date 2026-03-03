# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWqspt(RPackage):
	"""Permutation Test for Weighted Quantile Sum Regression

	Implements a permutation test method for the weighted quantile sum (WQS) regression, building off the 'gWQS' package (Renzetti et al. (2021) <https://CRAN.R-project.org/package=gWQS>). Weighted quantile sum regression is a statistical technique to evaluate the effect of complex exposure mixtures on an outcome (Carrico et al. (2015) <doi:10.1007/s13253-014-0180-3>). The model features a statistical power and Type I error (i.e., false positive) rate trade-off, as there is a machine learning step to determine the weights that optimize the linear model fit. This package provides an alternative method based on a permutation test that should reliably allow for both high power and low false positive rate when utilizing WQS regression (Day et al. (2022) <doi:10.1289/EHP10570>).
	"""
	
	cran = "wqspt" 

	version("1.0.1", md5="f5f4871d364aeb062b4fab331b2b1965")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-gwqs", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
