# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKssa(RPackage):
	"""Known Sub-Sequence Algorithm

	Implements the Known Sub-Sequence Algorithm <doi:10.1016/j.aaf.2021.12.013>, which helps to automatically identify and validate the best method for missing data imputation in a time series. Supports the comparison of multiple state-of-the-art algorithms.
	"""
	
	homepage = "https://github.com/pipeben/kssa"
	cran = "kssa" 

	version("0.0.1", md5="9b7693b90e2d8058ba950451de7cdd2c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-imputets", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-missmethods", type=("build", "run"))
