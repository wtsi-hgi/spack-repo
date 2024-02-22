# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmisc(RPackage):
	"""Turner Miscellaneous

	Miscellaneous utility functions for data manipulation,
    data tidying, and working with gene expression data.
	"""
	
	homepage = "https://github.com/stephenturner/Tmisc"
	cran = "Tmisc" 

	version("1.0.1", md5="a584deb52ad71eca8dc09ff02c694942")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
