# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyfit(RPackage):
	"""Regularized Linear Modeling with Tidy Data

	An extension to the 'R' tidy data environment for automated machine learning. The package allows fitting and cross validation of linear regression and classification algorithms on grouped data. 
	"""
	
	homepage = "https://tidyfit.residualmetrics.com"
	cran = "tidyfit" 

	version("0.6.5", md5="50baaa278aee9338e0a7a604441e8ba9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dials", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-yardstick", type=("build", "run"))
