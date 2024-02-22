# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScatr(RPackage):
	"""Create Scatter Plots with Marginal Density or Box Plots

	Allows you to make clean, good-looking scatter plots with the option to 
    easily add marginal density or box plots on the axes. It is also available as a module for 'jamovi'
    (see <https://www.jamovi.org> for more information). 'Scatr' is based on the 
    'cowplot' package by Claus O. Wilke and the 'ggplot2' package by Hadley Wickham.
	"""
	
	homepage = "https://github.com/raviselker/scatr"
	cran = "scatr" 

	version("1.0.1", md5="b040983eb0bd9902e7dea2684a41638c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-jmvcore@0.8:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggstance", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
