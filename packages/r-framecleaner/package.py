# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFramecleaner(RPackage):
	"""Clean Data Frames

	Provides a friendly interface for modifying data frames with a sequence of piped commands built upon the 'tidyverse' Wickham et al., (2019) <doi:10.21105/joss.01686> . The majority of commands wrap 'dplyr' mutate statements in a convenient way to concisely solve common issues that arise when tidying small to medium data sets. Includes smart defaults and allows flexible selection of columns via 'tidyselect'. 
	"""
	
	homepage = "https://harrison4192.github.io/framecleaner/"
	cran = "framecleaner" 

	version("0.2.1", md5="a6512724d42ab8458b5747f8759dee00")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-fastdummies", type=("build", "run"))
