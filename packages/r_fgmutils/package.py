# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFgmutils(RPackage):
	"""Forest Growth Model Utilities

	Growth models and forest production require existing data
    manipulation and the creation of new data, structured from basic forest
    inventory data. The purpose of this package is provide functions to support
    these activities.
	"""
	
	cran = "Fgmutils" 

	version("0.9.5", md5="7fea74c408bac1355a583b7723990173")

	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r@3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-devemf", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
