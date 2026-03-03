# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTongfen(RPackage):
	"""Make Data Based on Different Geographies Comparable

	Several functions to allow comparisons of data across different geographies, in particular for Canadian census data from different censuses.
	"""
	
	homepage = "https://github.com/mountainMath/tongfen"
	cran = "tongfen" 

	version("0.3.5", md5="3b1df8c37da958f147a5834f42aef28a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
