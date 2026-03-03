# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdamr(RPackage):
	"""Statistics: Data Analysis and Modelling

	Data sets and functions to support the books "Statistics: Data 
        analysis and modelling" by Speekenbrink, M. (2021) 
        <https://mspeekenbrink.github.io/sdam-book/> and "An R companion to 
        Statistics: data analysis and modelling" by Speekenbrink, M. (2021) 
        <https://mspeekenbrink.github.io/sdam-r-companion/>. All datasets 
        analysed in these books are provided in this package. In addition, the 
        package provides functions to compute sample statistics (variance, 
        standard deviation, mode), create raincloud and enhanced Q-Q plots, and 
        expand Anova results into omnibus tests and tests of individual 
        contrasts. 
	"""
	
	homepage = "https://mspeekenbrink.github.io/sdam-r/"
	cran = "sdamr" 

	version("0.2.0", md5="89a2947309331814678f0aa398d50dc9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
