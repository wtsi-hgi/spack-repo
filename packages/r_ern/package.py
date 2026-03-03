# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErn(RPackage):
	"""Effective Reproduction Number Estimation

	Estimate the effective reproduction number from wastewater
    and clinical data sources.
	"""
	
	cran = "ern" 

	version("1.3.1", md5="9c6e4b352b4078c55348a6a753047bf6")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-epiestim", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-runjags", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
