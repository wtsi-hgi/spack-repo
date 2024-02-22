# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSubselect(RPackage):
	"""Selecting Variable Subsets

	A collection of functions which (i) assess the quality of variable subsets as surrogates for a full data set, in either an exploratory data analysis or in the context of a multivariate linear model, and (ii) search for subsets which are optimal under various criteria. Theoretical support for the heuristic search methods and exploratory data analysis criteria is in Cadima, Cerdeira, Minhoto (2003, <doi:10.1016/j.csda.2003.11.001>). Theoretical support for the leap and bounds algorithm and the criteria for the general multivariate linear model is in Duarte Silva (2001, <doi:10.1006/jmva.2000.1920>). There is a package vignette "subselect", which includes additional references.
	"""
	
	cran = "subselect" 

	version("0.15.5", md5="fa298c59774887ec12fc70072bc8fdd3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-iswr", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
