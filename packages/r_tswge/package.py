# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTswge(RPackage):
	"""Time Series for Data Science

	Accompanies the texts Time Series for Data Science with R by Woodward, Sadler and Robertson & Applied Time Series Analysis with R, 2nd edition by Woodward, Gray, and Elliott.  It is helpful for data analysis and for time series instruction.
	"""
	
	cran = "tswge" 

	version("2.1.0", md5="b877b7f32f879e9984733c7f696a82ce")

	depends_on("r-signal", type=("build", "run"))
	depends_on("r-polynomf", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-waveslim", type=("build", "run"))
	depends_on("r-astsa", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-nnfor", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
