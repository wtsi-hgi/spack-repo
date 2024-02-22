# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgridge(RPackage):
	"""Graphical Group Ridge

	The Graphical Group Ridge 'GGRidge' package package classifies ridge regression predictors in disjoint groups of conditionally correlated variables and derives different penalties (shrinkage parameters) for these groups of predictors. It combines the ridge regression method with the graphical model for high-dimensional data (i.e. the number of predictors exceeds the number of cases) or ill-conditioned data (e.g. in the presence of multicollinearity among predictors). The package reduces the mean square errors and the extent of over-shrinking of predictors as compared to the ridge method.Aldahmani, S. and Zoubeidi, T. (2020) <DOI:10.1080/00949655.2020.1803320>.
	"""
	
	cran = "GGRidge" 

	version("1.1.0", md5="71765132efc4b1c9c3afdb97aa675b98")

	depends_on("r-grbase", type=("build", "run"))
	depends_on("r-cvglasso", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
