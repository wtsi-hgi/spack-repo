# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWqtrends(RPackage):
	"""Assess Water Quality Trends with Generalized Additive Models

	Assess Water Quality Trends for Long-Term Monitoring Data in Estuaries using
  Generalized Additive Models following Wood (2017) <doi:10.1201/9781315370279> and Error
  Propagation with Mixed-Effects Meta-Analysis following Sera et al. (2019) <doi:10.1002/sim.8362>.
  Methods are available for model fitting, assessment of fit, annual and seasonal trend tests, and
  visualization of results.
	"""
	
	homepage = "<https://github.com/tbep-tech/wqtrends/>"
	cran = "wqtrends" 

	version("1.4.2", md5="e24a59b9fae7a9df622bb778fd2a03e4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mixmeta", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
