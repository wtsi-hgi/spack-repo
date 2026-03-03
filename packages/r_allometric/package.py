# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAllometric(RPackage):
	"""Structured Allometric Models for Trees

	Access allometric models used in forest resource analysis, such as
    volume equations, taper equations, biomass models, among many others. Users
    are able to efficiently find and select allometric models suitable for their
    project area and use them in analysis. Additionally, 'allometric' provides a
    structured framework for adding new models to an open-source models
    repository.
	"""
	
	cran = "allometric" 

	version("2.1.0", md5="c0af4c7329f7260ee5e2030d6d5a0f9a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-refmanager", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-isocodes", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
