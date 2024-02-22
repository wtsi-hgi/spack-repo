# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStabiliser(RPackage):
	"""Stabilising Variable Selection

	A stable approach to variable selection through stability selection and the use of a permutation-based objective stability threshold. Lima et al (2021) <doi:10.1038/s41598-020-79317-8>, Meinshausen and Buhlmann (2010) <doi:10.1111/j.1467-9868.2010.00740.x>.
	"""
	
	cran = "stabiliser" 

	version("1.0.6", md5="21f7f24e5eef6dfa2b49af99aaf99b9a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-bigstep", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-expss", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-recipes", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
