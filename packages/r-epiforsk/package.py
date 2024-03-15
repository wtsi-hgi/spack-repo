# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpiforsk(RPackage):
	"""Code Sharing at the Department of Epidemiological Research at
Statens Serum Institut

	This is a collection of assorted functions and examples collected 
    from various projects. Currently we have functionalities for simplifying 
    overlapping time intervals, Charlson comorbidity score constructors for 
    Danish data, getting frequency for multiple variables, getting standardized
    output from logistic and log-linear regressions, sibling design linear 
    regression functionalities a method for calculating the confidence intervals 
    for functions of parameters from a GLM, Bayes equivalent for hypothesis 
    testing with asymptotic Bayes factor, and several help functions for 
    generalized random forest analysis using 'grf'. 
	"""
	
	cran = "EpiForsk" 

	version("0.1.1", md5="8ffd20c3dc359ae88757281fa7396509")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-grf", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-matchit", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-policytree", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-svyvgam", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
