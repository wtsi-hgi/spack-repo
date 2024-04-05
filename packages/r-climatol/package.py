# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClimatol(RPackage):
	"""Climate Tools (Series Homogenization and Derived Products)

	Functions for the quality control, homogenization and missing data filling of climatological series and to obtain climatological summaries and grids from the results. Also functions to display wind-roses, meteograms, Walter&Lieth diagrams, and more.
	"""
	
	homepage = "https://climatol.eu"
	cran = "climatol" 

	version("4.1.0", md5="f74c025c677d7353ca8981d6ef6d0f17")
	version("4.0.0", md5="15e768f957df77168c0aa4a5f94caea4")

	depends_on("r@3.6:", type=("build", "run"))
