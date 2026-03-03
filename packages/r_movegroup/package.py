# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMovegroup(RPackage):
	"""Visualizing and Quantifying Space Use Data for Groups of Animals

	Offers an easy and automated way to scale up individual-level space use analysis to 
    that of groups. Contains a function from the 'move' package to calculate a dynamic Brownian 
    bridge movement model from movement data for individual animals, as well as functions to 
    visualize and quantify space use for individuals aggregated in groups. Originally written with 
    passive acoustic telemetry in mind, this package also provides functionality to account for
    unbalanced acoustic receiver array designs, and satellite tag data.
	"""
	
	cran = "movegroup" 

	version("2024.03.05", md5="da6d9ca10f6593149ae63dc0c64d006e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-beepr@1.3:", type=("build", "run"))
	depends_on("r-dplyr@1.0.8:", type=("build", "run"))
	depends_on("r-ggmap@3:", type=("build", "run"))
	depends_on("r-knitr@1.45:", type=("build", "run"))
	depends_on("r-lubridate@1.8:", type=("build", "run"))
	depends_on("r-magick@2.8.2:", type=("build", "run"))
	depends_on("r-move@4.1.6:", type=("build", "run"))
	depends_on("r-purrr@1.0.2:", type=("build", "run"))
	depends_on("r-raster@3.5.15:", type=("build", "run"))
	depends_on("r-rlang@1.0.2:", type=("build", "run"))
	depends_on("r-sf@1.0.7:", type=("build", "run"))
	depends_on("r-sp@1.4.6:", type=("build", "run"))
	depends_on("r-stars@0.5.5:", type=("build", "run"))
	depends_on("r-starsextra@0.2.7:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-terra@1.7.39:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-viridis@0.6.4:", type=("build", "run"))
