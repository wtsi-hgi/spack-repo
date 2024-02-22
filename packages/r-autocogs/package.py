# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutocogs(RPackage):
	"""Automatic Cognostic Summaries

	Automatically calculates cognostic groups for plot objects and list column plot objects.  Results are returned in a nested data frame.
	"""
	
	homepage = "https://github.com/schloerke/autocogs"
	cran = "autocogs" 

	version("0.1.4", md5="edead90b73fc9ed56615b37383c2a148")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-diptest", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
