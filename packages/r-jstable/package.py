# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJstable(RPackage):
	"""Create Tables from Different Types of Regression

	Create regression tables from generalized linear model(GLM), generalized estimating equation(GEE), generalized linear mixed-effects model(GLMM), Cox proportional hazards model, survey-weighted generalized linear model(svyglm) and survey-weighted Cox model results for publication.
	"""
	
	homepage = "https://github.com/jinseob2kim/jstable"
	cran = "jstable" 

	version("1.1.7", md5="495ad623639ba817192dd6ef10280f7a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-labelled", type=("build", "run"))
	depends_on("r-tableone", type=("build", "run"))
	depends_on("r-coxme", type=("build", "run"))
	depends_on("r-survival@3:", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
