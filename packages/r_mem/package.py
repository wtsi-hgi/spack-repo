# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMem(RPackage):
	"""The Moving Epidemic Method

	The Moving Epidemic Method, created by T Vega and JE Lozano (2012, 2015) <doi:10.1111/j.1750-2659.2012.00422.x>, <doi:10.1111/irv.12330>, allows the weekly assessment of the epidemic and intensity status to help in routine respiratory infections surveillance in health systems. Allows the comparison of different epidemic indicators, timing and shape with past epidemics and across different regions or countries with different surveillance systems. Also, it gives a measure of the performance of the method in terms of sensitivity and specificity of the alert week.
	"""
	
	homepage = "https://github.com/lozalojo/mem"
	cran = "mem" 

	version("2.18", md5="dc2c24ca475e577539d787ab60730869")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-sm", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
