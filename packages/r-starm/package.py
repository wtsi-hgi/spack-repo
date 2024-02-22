# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStarm(RPackage):
	"""Spatio-Temporal Autologistic Regression Model

	Estimates the coefficients of the two-time centered autologistic regression model based on Gegout-Petit A., Guerin-Dubrana L., Li S. "A new centered spatio-temporal autologistic regression model. Application to local spread of plant diseases." 2019. <arXiv:1811.06782>, using a grid of binary variables to estimate the spread of a disease on the grid over the years. 
	"""
	
	cran = "starm" 

	version("0.1.0", md5="28e08cfe4a33690961f3597d388339e8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
