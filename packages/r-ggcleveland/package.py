# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgcleveland(RPackage):
	"""Implementation of Plots from Cleveland's Visualizing Data Book

	William S. Cleveland's book 'Visualizing Data' is a classic piece 
	of literature on Exploratory Data Analysis. Although it was written 
	several decades ago, its content is still relevant as it proposes several 
	tools which are useful to discover patterns and relationships among the data 
	under study, and also to assess the goodness of fit o a model.  This package 
	provides functions to produce the 'ggplot2' versions of the visualization tools 
	described in this book and is thought to be used in the context of courses on 
	Exploratory Data Analysis.
	"""
	
	homepage = "https://github.com/mpru/ggcleveland"
	cran = "ggcleveland" 

	version("0.1.0", md5="47e264a78467b5d8872edaa253b52f02")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-egg", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
