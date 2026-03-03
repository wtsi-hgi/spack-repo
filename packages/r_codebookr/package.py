# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodebookr(RPackage):
	"""Create Codebooks from Data Frames

	Quickly and easily create codebooks (i.e. data dictionaries) directly from a data frame.
	"""
	
	homepage = "https://github.com/brad-cannell/codebookr"
	cran = "codebookr" 

	version("0.1.8", md5="289634eb48c1d599debb5d09b3f4ccec")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-haven@2.5:", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
