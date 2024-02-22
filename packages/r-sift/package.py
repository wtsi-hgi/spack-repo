# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSift(RPackage):
	"""Intelligently Peruse Data

	Facilitate extraction of key information from common datasets.
	"""
	
	cran = "sift" 

	version("0.1.0", md5="c8e67523f3c669cafde0598e0a9fb776")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-pastecs@1.3.21:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-rlang@0.4.3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
