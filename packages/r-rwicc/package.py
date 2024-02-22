# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwicc(RPackage):
	"""Regression with Interval-Censored Covariates

	Provides functions to simulate and analyze data for a regression model with an interval censored covariate, as described in Morrison et al. (2021) <doi:10.1111/biom.13472>.
	"""
	
	homepage = "https://d-morrison.github.io/rwicc/"
	cran = "rwicc" 

	version("0.1.3", md5="aa550e42af1131c9bd21c9e53b05821e")

	depends_on("r-biglm", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
