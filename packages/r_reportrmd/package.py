# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReportrmd(RPackage):
	"""Tidy Presentation of Clinical Reporting

	Streamlined statistical reporting in 'Rmarkdown' environments. 
    Facilitates the automated reporting of descriptive statistics, multiple 
    univariate models, multivariable models and tables combining these outputs. 
    Plotting functions include customisable survival curves, forest plots from 
    logistic and ordinal regression and bivariate comparison plots.
	"""
	
	cran = "reportRmd" 

	version("0.1.0", md5="759f804ab969e85cb972cf4927e08dd0")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-aod", type=("build", "run"))
	depends_on("r-cmprsk", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstatix", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
