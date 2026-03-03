# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWhen(RPackage):
	"""Definition of Date and Time Dimension Tables

	In Multidimensional Systems the When dimension allows us to
    express when the analysed facts have occurred. The purpose of this
    package is to provide support for implementing this dimension in the
    form of date and time tables for Relational On-Line Analytical Processing 
    star database systems.
	"""
	
	homepage = "https://josesamos.github.io/when/"
	cran = "when" 

	version("1.0.0", md5="4f76f34988d59b571de3f699fc6294d1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dm", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
