# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHalk(RPackage):
	"""Methods to Create Hierarchical Age Length Keys for Age
Assignment

	Provides methods for implementing hierarchical age length keys
    to estimate fish ages from lengths using data borrowing. Users can create
    hierarchical age length keys and use them to assign ages given length.
	"""
	
	cran = "halk" 

	version("0.0.5", md5="7aeb8180934fe56b4b4295e650ef334a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rlang@1.0.4:", type=("build", "run"))
	depends_on("r-tibble@3.1.7:", type=("build", "run"))
	depends_on("r-dplyr@1.0.9:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
