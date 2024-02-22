# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDibble(RPackage):
	"""Dimensional Data Frames

	Provides a 'dibble' that implements data cubes (derived from 
    'dimensional tibble'), and allows broadcasting by dimensional names.
	"""
	
	homepage = "https://github.com/UchidaMizuki/dibble"
	cran = "dibble" 

	version("0.2.2", md5="cbf361dbd8ed03c5bda95c6b637c6c80")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
