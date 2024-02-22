# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepolr(RPackage):
	"""Repeated Measures Proportional Odds Logistic Regression

	Fits linear models to repeated ordinal scores using GEE methodology.
	"""
	
	cran = "repolr" 

	version("3.4", md5="18c76e074fdbbd54bb21966baabacb80")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
