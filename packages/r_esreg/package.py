# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REsreg(RPackage):
	"""Joint Quantile and Expected Shortfall Regression

	
    Simultaneous modeling of the quantile and the expected shortfall of a response variable given 
    a set of covariates, see Dimitriadis and Bayer (2019) <doi:10.1214/19-EJS1560>.
	"""
	
	cran = "esreg" 

	version("0.6.2", md5="c32c768c1a30ab39e4ab5caf6e625d27")

	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
