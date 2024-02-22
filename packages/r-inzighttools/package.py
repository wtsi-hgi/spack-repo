# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInzighttools(RPackage):
	"""Tools for 'iNZight'

	Provides a collection of wrapper functions for common variable and dataset manipulation workflows primarily used by 'iNZight', a graphical user interface providing easy exploration and visualisation of data for students of statistics, available in both desktop and online versions. Additionally, many of the functions return the 'tidyverse' code used to obtain the result in an effort to bridge the gap between GUI and coding.
	"""
	
	homepage = "https://inzight.nz"
	cran = "iNZightTools" 

	version("2.0.1", md5="9e48df5d7feab1c6debb431877ea3f5a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-readr@1.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.9:", type=("build", "run"))
	depends_on("r-srvyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
