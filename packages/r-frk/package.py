# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrk(RPackage):
	"""Fixed Rank Kriging

	A tool for spatial/spatio-temporal modelling and prediction with large datasets. The approach models the field, and hence the covariance function, using a set of basis functions. This fixed-rank basis-function representation facilitates the modelling of big data, and the method naturally allows for non-stationary, anisotropic covariance functions. Discretisation of the spatial domain into so-called basic areal units (BAUs) facilitates the use of observations with varying support (i.e., both point-referenced and areal supports, potentially simultaneously), and prediction over arbitrary user-specified regions. `FRK` also supports inference over various manifolds, including the 2D plane and 3D sphere, and it provides helper functions to model, fit, predict, and plot with relative ease. Version 2.0.0 and above also supports the modelling of non-Gaussian data (e.g., Poisson, binomial, negative-binomial, gamma, and inverse-Gaussian) by employing a generalised linear mixed model (GLMM) framework.  Zammit-Mangion and Cressie <doi:10.18637/jss.v098.i04> describe `FRK` in a Gaussian setting, and detail its use of basis functions and BAUs, while Sainsbury-Dale et al. <arXiv:2110.02507> describe `FRK` in a non-Gaussian setting; two vignettes are available that summarise these papers and provide additional examples.
	"""
	
	homepage = "https://andrewzm.github.io/FRK/"
	cran = "FRK" 

	version("2.2.2", md5="49133e06f44b1f25312338be8efb7157")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hmisc@4.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spacetime", type=("build", "run"))
	depends_on("r-sparseinv", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
