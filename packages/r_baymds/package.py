# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaymds(RPackage):
	"""Bayesian Multidimensional Scaling and Choice of Dimension

	Bayesian approach to multidimensional scaling. The package consists of implementations of the methods of Oh and Raftery (2001)  <doi:10.1198/016214501753208690>. 
	"""
	
	cran = "bayMDS" 

	version("2.0", md5="c45b0bdc56d225e744ccb94733720e84")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
