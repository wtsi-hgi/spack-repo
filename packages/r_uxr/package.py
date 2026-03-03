# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUxr(RPackage):
	"""User Experience Research

	Provides convenience functions for user experience research
    with an emphasis on quantitative user experience testing and reporting.
    The functions are designed to translate statistical approaches to 
    applied user experience research.
	"""
	
	homepage = "https://joe-chelladurai.github.io/uxr/"
	cran = "uxr" 

	version("0.2.0", md5="02d79649794875a43572aa08e35b392e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-huxtable", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
