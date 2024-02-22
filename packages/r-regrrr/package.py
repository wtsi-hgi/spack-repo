# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegrrr(RPackage):
	"""Toolkit for Compiling, (Post-Hoc) Testing, and Plotting
Regression Results

	Compiling regression results into a publishable format, conducting post-hoc hypothesis testing, and plotting moderating effects (the effect of X on Y becomes stronger/weaker as Z increases).
	"""
	
	cran = "regrrr" 

	version("0.1.3", md5="3e3d2d7fd26bc573142ec367dea1c333")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-usdm", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-mumin", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lspline", type=("build", "run"))
