# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgblanket(RPackage):
	"""Simplify 'ggplot2' Visualisation

	Simplify 'ggplot2' visualisation with 'ggblanket' wrapper
    functions.
	"""
	
	homepage = "https://davidhodge931.github.io/ggblanket/"
	cran = "ggblanket" 

	version("7.0.0", md5="d4cfa24df286215bf152b209cb8da885")

	depends_on("r-dplyr@1.0.4:", type=("build", "run"))
	depends_on("r-farver", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2@3.5:", type=("build", "run"))
	depends_on("r-hms@0.5:", type=("build", "run"))
	depends_on("r-lubridate@1.7.8:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-scales@1.3:", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
	depends_on("r-stringr@1.3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-viridislite@0.4:", type=("build", "run"))
