# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROlsrr(RPackage):
	"""Tools for Building OLS Regression Models

	Tools designed to make it easier for users, particularly beginner/intermediate R users 
    to build ordinary least squares regression models. Includes comprehensive regression output, 
    heteroskedasticity tests, collinearity diagnostics, residual diagnostics, measures of influence, 
    model fit assessment and variable selection procedures.
	"""
	
	homepage = "https://olsrr.rsquaredacademy.com/"
	cran = "olsrr" 

	version("0.6.0", md5="13e5ee47f191fbd45d1d59839caf498a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-goftest", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-xplorerr", type=("build", "run"))
