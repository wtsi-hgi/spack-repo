# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRolap(RPackage):
	"""Obtaining Star Databases from Flat Tables

	Data in multidimensional systems is obtained from operational
    systems and is transformed to adapt it to the new structure.
    Frequently, the operations to be performed aim to transform a flat
    table into a ROLAP (Relational On-Line Analytical Processing) star
    database. The main objective of the package is to allow the definition
    of these transformations easily. The implementation of the
    multidimensional database obtained can be exported to work with
    multidimensional analysis tools on spreadsheets or relational
    databases.
	"""
	
	homepage = "https://josesamos.github.io/rolap/"
	cran = "rolap" 

	version("2.5.1", md5="c5c394bde50b96dfd8b8f1b192462942")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dm", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
	depends_on("r-starschemar", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-when", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
