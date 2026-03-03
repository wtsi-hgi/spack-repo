# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQacbase(RPackage):
	"""Functions to Facilitate Exploratory Data Analysis

	Functions for descriptive statistics,
  data management, and data visualization.
	"""
	
	homepage = "https://github.com/rkabacoff/qacBase"
	cran = "qacBase" 

	version("1.0.3", md5="bd1eaf0aabea0ed00b41427ff32e7448")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggcorrplot", type=("build", "run"))
	depends_on("r-multcompview", type=("build", "run"))
	depends_on("r-pmcmrplus", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggextra", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
