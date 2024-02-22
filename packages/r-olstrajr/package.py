# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROlstrajr(RPackage):
	"""Ordinary Least Squares Trajectory Analysis

	The 'OLStrajr' package provides comprehensive functions for ordinary
    least squares (OLS) trajectory analysis and case-by-case OLS regression as
    outlined in Carrig, Wirth, and Curran (2004) <doi:10.1207/S15328007SEM1101_9>
    and Rogosa and Saner (1995) <doi:10.3102/10769986020002149>. It encompasses two
    primary functions, OLStraj() and cbc_lm(). The OLStraj() function simplifies
    the estimation of individual growth curves over time via OLS regression, with
    options for visualizing both group-level and individual-level growth trajectories
    and support for linear and quadratic models. The cbc_lm() function facilitates
    case-by-case OLS estimates and provides unbiased mean population intercept and
    slope estimators by averaging OLS intercepts and slopes across cases. It further
    offers standard error calculations across bootstrap replicates and computation
    of 95% confidence intervals based on empirical distributions from the resampling
    processes.
	"""
	
	homepage = "https://github.com/mightymetrika/OLStrajr"
	cran = "OLStrajr" 

	version("0.1.0", md5="acd66779afc794dd2210ebfa1c449528")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
