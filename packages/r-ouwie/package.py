# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROuwie(RPackage):
	"""Analysis of Evolutionary Rates in an OU Framework

	Estimates rates for continuous character evolution under Brownian motion and a new set of Ornstein-Uhlenbeck based Hansen models that allow both the strength of the pull and stochastic motion to vary across selective regimes. Beaulieu et al (2012).
	"""
	
	homepage = "https://github.com/thej022214/OUwie"
	cran = "OUwie" 

	version("2.10", md5="65650bd6dc7b8d3ba0df1c4dd66f6c8d")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-geiger", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-paleotree", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
	depends_on("r-interp", type=("build", "run"))
	depends_on("r-phylolm", type=("build", "run"))
