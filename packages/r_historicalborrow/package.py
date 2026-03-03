# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHistoricalborrow(RPackage):
	"""Non-Longitudinal Bayesian Historical Borrowing Models

	Historical borrowing in clinical trials can improve
  precision and operating characteristics. This package supports
  a hierarchical model and a mixture model to borrow historical
  control data from other studies to better characterize the
  control response of the current study. It also quantifies
  the amount of borrowing through benchmark models (independent
  and pooled). Some of the methods are discussed by
  Viele et al. (2013) <doi:10.1002/pst.1589>.
	"""
	
	homepage = "https://wlandau.github.io/historicalborrow/"
	cran = "historicalborrow" 

	version("1.0.4", md5="64cf0800d3a97dbd860d63569e4f9a83")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-posterior", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
