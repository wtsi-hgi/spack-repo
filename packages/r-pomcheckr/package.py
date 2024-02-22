# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPomcheckr(RPackage):
	"""Graphical Check for Proportional Odds Assumption

	Implements the method described at the UCLA Statistical
    Consulting site <https://stats.idre.ucla.edu/r/dae/ordinal-logistic-regression/>
    for checking if the proportional odds assumption holds for a 
    cumulative logit model.
	"""
	
	cran = "pomcheckr" 

	version("0.1.1", md5="07be85b10e59eadb3109f63caac87e30")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
