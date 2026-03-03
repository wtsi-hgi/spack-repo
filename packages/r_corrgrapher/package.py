# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrgrapher(RPackage):
	"""Explore Correlations Between Variables in a Machine Learning
Model

	When exploring data or models we often examine variables one by one. 
  This analysis is incomplete if the relationship between these variables is 
  not taken into account. The 'corrgrapher' package facilitates simultaneous 
  exploration of the Partial Dependence Profiles and the correlation between 
  variables in the model.
  The package 'corrgrapher' is a part of the 'DrWhy.AI' universe.
	"""
	
	homepage = "https://modeloriented.github.io/corrgrapher/"
	cran = "corrgrapher" 

	version("1.0.4", md5="f87e3d62bff6dca84da433fbdc5e9b46")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-ingredients", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
