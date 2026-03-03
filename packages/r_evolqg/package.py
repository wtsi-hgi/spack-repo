# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvolqg(RPackage):
	"""Evolutionary Quantitative Genetics

	Provides functions for covariance matrix comparisons, estimation of repeatabilities in measurements and matrices, and general evolutionary quantitative genetics tools. Melo D, Garcia G, Hubbe A, Assis A P, Marroig G. (2016) <doi:10.12688/f1000research.7082.3>.
	"""
	
	cran = "evolqg" 

	version("0.3-4", md5="a8e5331402e7228b50acef8bd906c57e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-plyr@1.7.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-morpho", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
