# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXplorerr(RPackage):
	"""Tools for Interactive Data Exploration

	Tools for interactive data exploration built using 'shiny'. Includes apps for descriptive 
    statistics, visualizing probability distributions, inferential statistics, linear regression, 
    logistic regression and RFM analysis.
	"""
	
	homepage = "https://github.com/rsquaredacademy/xplorerr"
	cran = "xplorerr" 

	version("0.1.2", md5="c13d22593748d9319d146c1c6c081b78")

	depends_on("r@3.2.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
