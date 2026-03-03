# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgmosaic(RPackage):
	"""Mosaic Plots in the 'ggplot2' Framework

	Mosaic plots in the 'ggplot2' framework. Mosaic
    plot functionality is provided in a single 'ggplot2' layer by calling
    the geom 'mosaic'.
	"""
	
	homepage = "https://github.com/haleyjeppson/ggmosaic"
	cran = "ggmosaic" 

	version("0.3.3", md5="b877c91ccb3b55cf7e90c02a7b5bd927")

	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-productplots", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plotly@4.5.5:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
