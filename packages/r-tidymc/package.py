# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidymc(RPackage):
	"""Monte Carlo Simulations Made Easy and Tidy

	Framework to run Monte Carlo simulations over a parameter grid. 
             Allows to parallelize the simulations. 
             Generates plots and 'LaTeX' tables
             summarizing the results from the simulation. 
	"""
	
	homepage = "https://github.com/stefanlinner/tidyMC"
	cran = "tidyMC" 

	version("1.0.0", md5="9210f327c4de1a0b570f5eb9040f34bd")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
