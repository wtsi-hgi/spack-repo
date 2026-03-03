# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlsimcpp(RPackage):
	"""Methods for Partial Linear Single Index Model

	Estimation, hypothesis tests, and variable selection in partially linear single-index models. Please see H. (2010) at <doi:10.1214/10-AOS835> for more details.
	"""
	
	cran = "PLSiMCpp" 

	version("1.0.4", md5="bb7e222f4bb4b378beff392fc9ed95f5")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
