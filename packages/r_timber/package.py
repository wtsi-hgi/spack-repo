# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimber(RPackage):
	"""Calculate Wood Volumes from Taper Functions

	Functions for estimation of wood volumes, number of logs, diameters along the stem and heights at which certain diameters occur, based on taper functions and other parameters. References: McTague, J. P., & Weiskittel, A. (2021). <doi:10.1139/cjfr-2020-0326>.
	"""
	
	cran = "timbeR" 

	version("2.0.1", md5="146c5705f4b67ca56f227c618e81c7d9")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
