# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaemspe(RPackage):
	"""Compute MSPE Estimates for the Fay Herriot Model and Nested
Error Regression Model

	We describe a new R package entitled 'saeMSPE' for the well-known Fay Herriot model and nested error regression model in small area estimation. Based on this package, it is possible to easily compute various common mean squared predictive error (MSPE) estimators, as well as several existing variance component predictors as a byproduct, for these two models.
	"""
	
	cran = "saeMSPE" 

	version("1.2", md5="f72b096ec23b3d9d63d5fcbdb3eb520e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-smallarea", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
