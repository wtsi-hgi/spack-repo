# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLabourmarketareas(RPackage):
	"""Identification, Tuning, Visualisation and Analysis of Labour
Market Areas

	Produces Labour Market Areas from commuting flows available at elementary territorial units. It provides tools for automatic tuning based on spatial contiguity. It also allows for statistical analyses and visualisation of the new functional geography.
	"""
	
	cran = "LabourMarketAreas" 

	version("3.4", md5="d8f70b776c0852202be7bfdd7bdbae3d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-tmap", type=("build", "run"))
