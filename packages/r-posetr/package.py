# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPosetr(RPackage):
	"""Partially Ordered Sets in R

	Provides a set of basic tools for generating, analyzing, summarizing and visualizing finite partially ordered sets. In particular, it implements flexible and very efficient algorithms for the extraction of linear extensions and for the computation of mutual ranking probabilities and other user-defined functionals, over them. The package is meant as a computationally efficient "engine", for the implementation of data analysis procedures, on systems of multidimensional ordinal indicators and partially ordered data, in the spirit of Fattore, M. (2016) "Partially ordered sets and the measurement of multidimensional ordinal deprivation", Social Indicators Research <DOI:10.1007/s11205-015-1059-6>, and Fattore M. and Arcagni, A. (2018) "A reduced posetic approach to the measurement of multidimensional ordinal deprivation", Social Indicators Research <DOI:10.1007/s11205-016-1501-4>.
	"""
	
	cran = "POSetR" 

	version("1.1.4", md5="fe220d655911c89a755bd2b87b37e53f")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
