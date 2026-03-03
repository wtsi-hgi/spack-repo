# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAorsf(RPackage):
	"""Accelerated Oblique Random Forests

	Fit, interpret, and compute predictions with oblique random
    forests. Includes support for partial dependence, variable importance,
    passing customized functions for variable importance and identification
    of linear combinations of features. Methods for the oblique random 
    survival forest are described in Jaeger et al., (2023)
    <DOI:10.1080/10618600.2023.2231048>.
	"""
	
	homepage = "https://github.com/ropensci/aorsf"
	cran = "aorsf" 

	version("0.1.3", md5="1701ee0f1dd9c00ec15ce40446d0413e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-collapse", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
