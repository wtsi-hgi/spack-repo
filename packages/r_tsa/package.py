# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsa(RPackage):
	"""Time Series Analysis

	Contains R functions and datasets detailed in the book
        "Time Series Analysis with Applications in R (second edition)" by Jonathan Cryer and Kung-Sik Chan.
	"""
	
	homepage = "https://stat.uiowa.edu/~kchan/TSA.htm"
	cran = "TSA" 

	version("1.3.1", md5="be2afe80b7d712135d8fcbc78efdd7ed")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
