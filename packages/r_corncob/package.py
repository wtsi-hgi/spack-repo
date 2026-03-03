# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorncob(RPackage):
	"""Count Regression for Correlated Observations with the
Beta-Binomial

	Statistical modeling for correlated count data using the beta-binomial distribution, described in Martin et al. (2020) <doi:10.1214/19-AOAS1283>. It allows for both mean and overdispersion covariates.
	"""
	
	homepage = "https://github.com/statdivlab/corncob"
	cran = "corncob" 

	version("0.4.1", md5="050e514bd0806ade62b58aba13f15cf1")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-trust", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-detectseparation", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
