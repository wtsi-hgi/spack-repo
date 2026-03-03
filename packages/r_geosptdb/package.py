# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeosptdb(RPackage):
	"""Spatio-Temporal Radial Basis Functions with Distance-Based
Methods (Optimization, Prediction and Cross Validation)

	Spatio-temporal radial basis functions (optimization, prediction and cross-validation), summary statistics from cross-validation, Adjusting distance-based linear regression model and generation of the principal coordinates of a new individual from Gower's distance.
	"""
	
	cran = "geosptdb" 

	version("1.0-1", md5="c26dea2815fddb97f8fa9a129de92aa5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fd", type=("build", "run"))
	depends_on("r-statmatch", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-minqa", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-geospt", type=("build", "run"))
