# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSentinmixt(RPackage):
	"""Parsimonious Mixtures of MSEN and MTIN Distributions

	Implements parsimonious mixtures of MSEN and MTIN distributions via expectation-
    maximization based algorithms for model-based clustering. For each mixture
    component, parsimony is reached via the eigen-decomposition of the scale 
    matrices and by imposing a constraint on the tailedness parameter. This produces
    a family of 28 parsimonious mixture models for each distribution.
	"""
	
	cran = "SenTinMixt" 

	version("1.0.0", md5="5cb2d0d3d7b0d8f763f792cdf7cc80f4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-tsdist", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-expint", type=("build", "run"))
	depends_on("r-zipfr", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
