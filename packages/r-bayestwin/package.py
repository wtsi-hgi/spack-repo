# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayestwin(RPackage):
	"""Bayesian Analysis of Item-Level Twin Data

	Bayesian analysis of item-level hierarchical twin data using an integrated item response theory model. Analyses are based on Schwabe & van den Berg (2014) <doi:10.1007/s10519-014-9649-7>, Molenaar & Dolan (2014) <doi:10.1007/s10519-014-9647-9>, Schwabe, Jonker & van den Berg (2016) <doi:10.1007/s10519-015-9768-9> and Schwabe, Boomsma & van den Berg (2016) <doi:10.1016/j.lindif.2017.01.018>.
	"""
	
	homepage = "http://www.ingaschwabe.com"
	cran = "BayesTwin" 

	version("1.0", md5="2039696c53cf9e620fa1c7879d9b4512")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
