# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCglasso(RPackage):
	"""Conditional Graphical LASSO for Gaussian Graphical Models with
Censored and Missing Values

	Conditional graphical lasso estimator is an extension of the graphical lasso proposed to estimate the conditional dependence structure of a set of p response variables given q predictors. This package provides suitable extensions developed to study datasets with censored and/or missing values. Standard conditional graphical lasso is available as a special case. Furthermore, the package provides an integrated set of core routines for visualization, analysis, and simulation of datasets with censored and/or missing values drawn from a Gaussian graphical model. Details about the implemented models can be found in Augugliaro et al. (2023) <doi: 10.18637/jss.v105.i01>, Augugliaro et al. (2020b) <doi: 10.1007/s11222-020-09945-7>, Augugliaro et al. (2020a) <doi: 10.1093/biostatistics/kxy043>, Yin et al. (2001) <doi: 10.1214/11-AOAS494> and Stadler et al. (2012) <doi: 10.1007/s11222-010-9219-7>.
	"""
	
	cran = "cglasso" 

	version("2.0.7", md5="6a56aba54b487b27d1b739b195421620")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
