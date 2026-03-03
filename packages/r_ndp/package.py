# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNdp(RPackage):
	"""Interactive Presentation for Working with Normal Distribution

	An interactive presentation on  the topic of normal distribution using 'rmarkdown' and 'shiny' packages. It is helpful to those who want to learn normal distribution quickly and get a hands on experience. The presentation has a template for solving problems on normal distribution. Runtime examples are provided in the package function as well as at  <https://kartikeyastat.shinyapps.io/NormalDistribution/>. 
	"""
	
	cran = "NDP" 

	version("0.1.0", md5="fde8f32182b882d1f803715520ecffdb")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
