# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapcan(RPackage):
	"""Tools for Plotting Canadian Choropleth Maps and Choropleth
Alternatives

	A variety of functions that make it easy to plot standard choropleth maps as well as choropleth alternatives in 'ggplot2'.
	"""
	
	cran = "mapcan" 

	version("0.0.1", md5="55948a6b57f3af4dee4d33fc38553c58")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
