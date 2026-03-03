# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatsindf(RPackage):
	"""Matrices in Data Frames

	Provides functions to collapse a tidy data frame into matrices in a data frame
    and expand a data frame of matrices into a tidy data frame.
	"""
	
	homepage = "https://github.com/MatthewHeun/matsindf"
	cran = "matsindf" 

	version("0.4.8", md5="35acd330ba6b93e88e43e584b9336afe")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matsbyname", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
