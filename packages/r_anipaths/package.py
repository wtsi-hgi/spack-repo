# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnipaths(RPackage):
	"""Animation of Multiple Trajectories with Uncertainty

	Animation of observed trajectories using spline-based interpolation (see for example, Buderman, F. E., Hooten, M. B., Ivan, J. S. and Shenk, T. M. (2016), <doi:10.1111/2041-210X.12465> "A functional model for characterizing long-distance movement behaviour". Methods Ecol Evol). Intended to be used exploratory data analysis, and perhaps for preparation of presentations.
	"""
	
	cran = "anipaths" 

	version("0.10.3", md5="2541e31f7025c6a7efa2eee8c8f36f8e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-animation", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-crawl", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-ggmap", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
