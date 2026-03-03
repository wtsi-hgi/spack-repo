# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScva(RPackage):
	"""Single-Case Visual Analysis

	Make graphical representations of single case data and transform graphical displays back to raw data, as discussed in Bulte and Onghena (2013) <doi:10.22237/jmasm/1383280020>. The package also includes tools for visually analyzing single-case data, by displaying central location, variability and trend.
	"""
	
	cran = "SCVA" 

	version("1.3.1", md5="1bc922d3ebe56d082a80d2088104a56d")

	depends_on("r-ggextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
