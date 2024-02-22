# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStickyr(RPackage):
	"""Data Frames with Persistent Columns and Attributes

	Provides data frames that hold certain columns and attributes 
    persistently for data processing in 'dplyr'.
	"""
	
	homepage = "https://github.com/UchidaMizuki/stickyr"
	cran = "stickyr" 

	version("0.1.2", md5="f3f0753815adf4fc89f784c302369d01")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
