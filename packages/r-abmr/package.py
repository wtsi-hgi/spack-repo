# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbmr(RPackage):
	"""Agent-Based Models in R

	Supplies tools for running agent-based models (ABM) in R, as discussed in Gochanour et al. (2022) <doi:10.1111/2041-210X.14014>. The package contains two movement functions, each of which is based on the Ornstein-Uhlenbeck (OU) model (Ornstein & Uhlenbeck, 1930) <doi:10.1103/PhysRev.36.823>. It also contains several visualization and data summarization functions to facilitate the presentation of simulation results.
	"""
	
	cran = "abmR" 

	version("1.0.10", md5="bb47b010ed03573cea3ad57722d36c30")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-table1", type=("build", "run"))
	depends_on("r-googledrive", type=("build", "run"))
	depends_on("r-swfscmisc", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-gtsummary", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tmap", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rnaturalearth", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
