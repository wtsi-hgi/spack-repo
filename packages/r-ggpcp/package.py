# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgpcp(RPackage):
	"""Parallel Coordinate Plots in the 'ggplot2' Framework

	Modern Parallel Coordinate Plots have been introduced in the 1980s as 
    a way to visualize arbitrarily many numeric variables. This Grammar of Graphics implementation
    also incorporates categorical variables into the plots in a principled manner. 
    By separating the data managing part from the visual rendering, we give full access
    to the users while keeping the number of parameters manageably low.  
	"""
	
	homepage = "https://github.com/heike/ggpcp"
	cran = "ggpcp" 

	version("0.2.0", md5="e0152992c9cb6c8912eabe0b7f2067f2")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-tibble@3.1.4:", type=("build", "run"))
	depends_on("r-tidyselect@1.1.1:", type=("build", "run"))
	depends_on("r-tidyr@1.1.3:", type=("build", "run"))
