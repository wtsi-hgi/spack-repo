# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXgxr(RPackage):
	"""Exploratory Graphics for Pharmacometrics

	Supports a structured approach
    for exploring PKPD data <https://opensource.nibr.com/xgx/>. It also
    contains helper functions for enabling the modeler to follow best R
    practices (by appending the program name, figure name location, and
    draft status to each plot). In addition, it enables the modeler to
    follow best graphical practices (by providing a theme that
    reduces chart ink, and by providing time-scale, log-scale, and
    reverse-log-transform-scale functions for more readable axes).
    Finally, it provides some data checking and summarizing functions for
    rapidly exploring pharmacokinetics and pharmacodynamics (PKPD) datasets.
	"""
	
	homepage = "https://opensource.nibr.com/xgx/"
	cran = "xgxr" 

	version("1.1.2", md5="49a2947c949d3410a752b4bb8b4549e4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-binom", type=("build", "run"))
	depends_on("r-deriv", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-labeling", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
