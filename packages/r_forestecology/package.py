# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForestecology(RPackage):
	"""Fitting and Assessing Neighborhood Models of the Effect of
Interspecific Competition on the Growth of Trees

	Code for fitting and assessing models for the growth of trees. In 
    particular for the Bayesian neighborhood competition linear regression model 
    of Allen (2020): methods for model fitting and generating fitted/predicted 
    values, evaluating the effect of competitor species identity using 
    permutation tests, and evaluating model performance using spatial 
    cross-validation. 
	"""
	
	homepage = "https://github.com/rudeboybert/forestecology"
	cran = "forestecology" 

	version("0.2.0", md5="6d49d640685b233eaaedb2f17758c1fb")

	depends_on("r@3.2.4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-mvnfast", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sfheaders", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-yardstick", type=("build", "run"))
	depends_on("r-blockcv", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
