# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScpi(RPackage):
	"""Prediction Intervals for Synthetic Control Methods with Multiple
Treated Units and Staggered Adoption

	Implementation of prediction and inference procedures for Synthetic Control methods using least square, lasso, ridge, or simplex-type constraints. Uncertainty is quantified with prediction intervals as developed in Cattaneo, Feng, and Titiunik (2021) <https://nppackages.github.io/references/Cattaneo-Feng-Titiunik_2021_JASA.pdf> for a single treated unit and in Cattaneo, Feng, Palomba, and Titiunik (2023) <arXiv:2210.05026> for multiple treated units and staggered adoption. More details about the software implementation can be found in Cattaneo, Feng, Palomba, and Titiunik (2022) <arXiv:2202.05984>.
	"""
	
	homepage = "https://nppackages.github.io/scpi/"
	cran = "scpi" 

	version("2.2.5", md5="64b3d66e9e6e0b7358af9360ad0c38d2")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-abind@1.4.5:", type=("build", "run"))
	depends_on("r-cvxr@1.0.10:", type=("build", "run"))
	depends_on("r-dosnow@1.0.19:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-ecosolver@0.5.4:", type=("build", "run"))
	depends_on("r-fastdummies@1.6.3:", type=("build", "run"))
	depends_on("r-foreach@1.5.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.3:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-matrix@1.3.3:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-qtools@1.5.6:", type=("build", "run"))
	depends_on("r-reshape2@1.4.4:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@3.1.2:", type=("build", "run"))
	depends_on("r-tidyr@1.1.3:", type=("build", "run"))
