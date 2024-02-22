# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinsreg(RPackage):
	"""Binscatter Estimation and Inference

	Provides tools for statistical analysis using the binscatter methods developed by Cattaneo, Crump, Farrell and Feng (2023a) <arXiv:1902.09608>, Cattaneo, Crump, Farrell and Feng (2023b) <https://nppackages.github.io/references/Cattaneo-Crump-Farrell-Feng_2023_NonlinearBinscatter.pdf> and Cattaneo, Crump, Farrell and Feng (2023c) <arXiv:1902.09615>. Binscatter provides a flexible way of describing the relationship between two variables based on partitioning/binning of the independent variable of interest. binsreg(), binsqreg() and binsglm() implement binscatter least squares regression, quantile regression and generalized linear regression respectively, with particular focus on constructing binned scatter plots. They also implement robust (pointwise and uniform) inference of regression functions and derivatives thereof. binstest() implements hypothesis testing procedures for parametric functional forms of and nonparametric shape restrictions on the regression function. binspwc() implements hypothesis testing procedures for pairwise group comparison of binscatter estimators. binsregselect() implements data-driven procedures for selecting the number of bins for binscatter estimation. All the commands allow for covariate adjustment, smoothness restrictions and clustering.
	"""
	
	cran = "binsreg" 

	version("1.0", md5="e21532f7766c1183f0ec14fbec099f3d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
