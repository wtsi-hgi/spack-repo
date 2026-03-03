# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrucer(RPackage):
	"""Broadly Useful Convenient and Efficient R Functions

	
    Broadly useful convenient and efficient R functions
    that bring users concise and elegant R data analyses.
    This package includes easy-to-use functions for
    (1) basic R programming
    (e.g., set working directory to the path of currently opened file;
    import/export data from/to files in any format;
    print tables to Microsoft Word);
    (2) multivariate computation
    (e.g., compute scale sums/means/... with reverse scoring);
    (3) reliability analyses and factor analyses;
    (4) descriptive statistics and correlation analyses;
    (5) t-test, multi-factor analysis of variance (ANOVA),
    simple-effect analysis, and post-hoc multiple comparison;
    (6) tidy report of statistical models
    (to R Console and Microsoft Word);
    (7) mediation and moderation analyses (PROCESS);
    and (8) additional toolbox for statistics and graphics.
	"""
	
	homepage = "https://psychbruce.github.io/bruceR/"
	cran = "bruceR" 

	version("2023.9", md5="dc8018081d512b4a599fc4309cbf1fac")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-afex", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-effectsize", type=("build", "run"))
	depends_on("r-performance", type=("build", "run"))
	depends_on("r-mediation", type=("build", "run"))
	depends_on("r-interactions", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-jtools", type=("build", "run"))
	depends_on("r-texreg", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-mumin", type=("build", "run"))
