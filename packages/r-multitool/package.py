# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultitool(RPackage):
	"""Run Multiverse Style Analyses

	Run the same analysis over a range of arbitrary data processing 
    decisions. 'multitool' provides an interface for creating alternative 
    analysis pipelines and turning them into a grid of all possible pipelines. 
    Using this grid as a blueprint, you can model your data across all possible 
    pipelines and summarize the results.
	"""
	
	homepage = "https://ethan-young.github.io/multitool/"
	cran = "multitool" 

	version("0.1.4", md5="f4b39f73ba4a38cac7a21bdb0b633fe1")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-correlation", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-ggdist", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-parameters", type=("build", "run"))
	depends_on("r-performance", type=("build", "run"))
