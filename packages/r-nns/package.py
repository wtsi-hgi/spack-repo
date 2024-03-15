# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNns(RPackage):
	"""Nonlinear Nonparametric Statistics

	Nonlinear nonparametric statistics using partial moments.  Partial moments are the elements of variance and asymptotically approximate the area of f(x).  These robust statistics provide the basis for nonlinear analysis while retaining linear equivalences.  NNS offers: Numerical integration, Numerical differentiation, Clustering, Correlation, Dependence, Causal analysis, ANOVA, Regression, Classification, Seasonality, Autoregressive modeling, Normalization, Stochastic dominance and Advanced Monte Carlo sampling.  All routines based on: Viole, F. and Nawrocki, D. (2013), Nonlinear Nonparametric Statistics: Using Partial Moments (ISBN: 1490523995).
	"""
	
	cran = "NNS" 

	version("10.7", md5="5428bf51ee3ec2f05a49accd65a6f628")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-meboot", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
