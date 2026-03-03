# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAllestimates(RPackage):
	"""Effect Estimates from All Models

	Estimates and plots effect estimates from models with all possible 
    combinations of a list of variables. It can be used for assessing treatment 
    effects in clinical trials or risk factors in bio-medical and epidemiological 
    research. Like Stata command 'confall' (Wang Z (2007) <doi:10.1177/1536867X0700700203> ), 
    'allestimates' calculates and stores all effect estimates, and plots them against p values or 
    Akaike information criterion (AIC) values. It currently has functions for linear 
    regression: all_lm(), logistic and Poisson regression: all_glm(), 
    and Cox proportional hazards regression: all_cox(). 
	"""
	
	cran = "allestimates" 

	version("0.2.3", md5="6859433d64aa517fb1f71ea8c4aae6f6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
