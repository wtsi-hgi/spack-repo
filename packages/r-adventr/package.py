# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdventr(RPackage):
	"""Interactive R Tutorials to Accompany Field (2016), "An Adventure
in Statistics"

	Interactive 'R' tutorials written using 'learnr' for Field (2016), "An Adventure in Statistics", <ISBN:9781446210451>.
    Topics include general workflow in 'R' and 'Rstudio', the 'R' environment and 'tidyverse', summarizing data, model fitting, central tendency, 
    visualising data using 'ggplot2', inferential statistics and robust estimation, hypothesis testing, the general linear model, comparing means,
    repeated measures designs, factorial designs, multilevel models, growth models, and generalized linear models (logistic regression).
	"""
	
	cran = "adventr" 

	version("0.1.8", md5="e693efb50579a01c5e8d9de42dbfb574")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-learnr", type=("build", "run"))
	depends_on("r-bayesfactor", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-effsize", type=("build", "run"))
	depends_on("r-effects", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-lm-beta", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-robust", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-sjstats", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-wrs2", type=("build", "run"))
