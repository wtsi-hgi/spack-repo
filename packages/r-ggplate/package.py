# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgplate(RPackage):
	"""Create Layout Plots of Biological Culture Plates and Microplates

	Enables users to create simple plots of biological culture plates as well as microplates. Both continuous and discrete values can be plotted onto the plate layout. 
	"""
	
	homepage = "https://github.com/jpquast/ggplate"
	cran = "ggplate" 

	version("0.1.1", md5="ee8603ffcc93b77468fac66ab738999e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-farver", type=("build", "run"))
