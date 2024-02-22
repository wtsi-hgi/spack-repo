# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnimbook(RPackage):
	"""Visualizing Changes in Performance Measures and Demographic
Affiliations using Animation

	Create an interactive visualization to be used for communication purposes. Providing the function for preparing, plotting, and animating the data.
	"""
	
	homepage = "https://github.com/KrisanatA/animbook"
	cran = "animbook" 

	version("1.0.0", md5="2e95128e419e63052a416ed3451a5843")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gganimate", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
