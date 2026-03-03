# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcvis(RPackage):
	"""Multi-Collinearity Visualization

	Visualize the relationship between linear regression variables and causes of multi-collinearity. 
    Implements the method in Lin et. al. (2020) <doi:10.1080/10618600.2020.1779729>. 
	"""
	
	cran = "mcvis" 

	version("1.0.8", md5="699a47f12bdf4daee7d07107e92cff51")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
