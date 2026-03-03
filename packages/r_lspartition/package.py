# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLspartition(RPackage):
	"""Nonparametric Estimation and Inference Procedures using
Partitioning-Based Least Squares Regression

	Tools for statistical analysis using partitioning-based least squares regression as described in Cattaneo, Farrell and Feng (2019a, <arXiv:1804.04916>) and Cattaneo, Farrell and Feng (2019b, <arXiv:1906.00202>): lsprobust() for nonparametric point estimation of regression functions and their derivatives and for robust bias-corrected (pointwise and uniform) inference; lspkselect() for data-driven selection of the IMSE-optimal number of knots; lsprobust.plot() for regression plots with robust confidence intervals and confidence bands; lsplincom() for estimation and inference for linear combinations of regression functions from different groups.
	"""
	
	cran = "lspartition" 

	version("0.4", md5="80f971851448f9a66c7d82c02b1daefa")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
