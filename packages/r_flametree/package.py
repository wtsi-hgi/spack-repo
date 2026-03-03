# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlametree(RPackage):
	"""Generate Random Tree-Like Images

	A generative art system for producing tree-like
    images using an L-system to create the structures. The package 
    includes tools for generating the data structures and visualise
    them in a variety of styles.
	"""
	
	homepage = "https://github.com/djnavarro/flametree"
	cran = "flametree" 

	version("0.1.3", md5="d39de8a5eaf1ca79868c316a0a8d3ff9")

	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
