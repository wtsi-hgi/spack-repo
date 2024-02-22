# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCandisc(RPackage):
	"""Visualizing Generalized Canonical Discriminant and Canonical
Correlation Analysis

	Functions for computing and visualizing 
	generalized canonical discriminant analyses and canonical correlation analysis
	for a multivariate linear model.
	Traditional canonical discriminant analysis is restricted to a one-way 'MANOVA'
	design and is equivalent to canonical correlation analysis between a set of quantitative
	response variables and a set of dummy variables coded from the factor variable.
	The 'candisc' package generalizes this to higher-way 'MANOVA' designs
	for all factors in a multivariate linear model,
	computing canonical scores and vectors for each term. The graphic functions provide low-rank (1D, 2D, 3D) 
	visualizations of terms in an 'mlm' via the 'plot.candisc' and 'heplot.candisc' methods. Related plots are
	now provided for canonical correlation analysis when all predictors are quantitative.
	"""
	
	cran = "candisc" 

	version("0.8-6", md5="b14d0d39d7273570c4c77006d53c52ab")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-heplots@0.8.6:", type=("build", "run"))
