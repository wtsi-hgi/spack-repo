# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCubble(RPackage):
	"""A Vector Spatio-Temporal Data Structure for Data Analysis

	A spatiotemperal data object in a relational data structure to separate the recording of time variant/ invariant variables.
	"""
	
	homepage = "https://github.com/huizezhang-sherry/cubble"
	cran = "cubble" 

	version("0.3.0", md5="507beb3acc1807759c2f7cd7a1ab776b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tsibble", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
