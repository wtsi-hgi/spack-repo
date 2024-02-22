# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REntropart(RPackage):
	"""Entropy Partitioning to Measure Diversity

	Measurement and partitioning of diversity, based on Tsallis entropy, following Marcon and Herault (2015) <doi:10.18637/jss.v067.i08>.
  'entropart' provides functions to calculate alpha, beta and gamma diversity of communities, including phylogenetic and functional diversity.
  Estimation-bias corrections are available.
	"""
	
	homepage = "https://github.com/EricMarcon/entropart"
	cran = "entropart" 

	version("1.6-13", md5="9446825cad22e93c7977ffd1196d0375")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r-entropyestimation", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
