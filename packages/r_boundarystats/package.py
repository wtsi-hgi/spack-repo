# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoundarystats(RPackage):
	"""Boundary Overlap Statistics

	Analysis workflow for finding geographic boundaries of ecological or landscape traits and comparing the placement of geographic boundaries of two traits. If data are trait values, trait data are transformed to boundary intensities based on approximate first derivatives across latitude and longitude. The package includes functions to create custom null models based on the input data. The boundary statistics are described in: Fortin, Drapeau, and Jacquez (1996) <doi:10.2307/3545584>.
	"""
	
	cran = "BoundaryStats" 

	version("2.1.1", md5="ae91e49078e5686dd0b04a90d15c0722")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-pdqr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-rgeoda", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
